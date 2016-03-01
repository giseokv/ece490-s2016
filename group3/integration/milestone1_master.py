import sys
sys.path.insert(0, "..")

import rospy
import baxter_interface
from klampt import *
from klampt.glprogram import *
from klampt import vectorops,so3,se3,gldraw,ik,loader
from util.constants import *
from perception.pc import PCProcessor
import random

baxter_rest_config = [0.0]*54


class MyGLViewer(GLNavigationProgram):
    """Visualization of robot"""
    def __init__(self,world):
        GLNavigationProgram.__init__(self,"My GL program")
        self.world = world
        self.draw_gripper_and_camera = True

    def display(self):
        self.world.drawGL()

        glBegin(GL_LINE_LOOP)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 0, 0)
        glEnd()

        #show gripper and camera frames
        if self.draw_gripper_and_camera:
            left_camera_link = self.world.robot(0).link(LEFT_CAMERA_LINK_NAME)
            right_camera_link = self.world.robot(0).link(RIGHT_CAMERA_LINK_NAME)
            left_gripper_link = self.world.robot(0).link(LEFT_GRIPPER_LINK_NAME)
            right_gripper_link = self.world.robot(0).link(RIGHT_GRIPPER_LINK_NAME)
            gldraw.xform_widget(left_camera_link.getTransform(),0.1,0.01)
            gldraw.xform_widget(right_camera_link.getTransform(),0.1,0.01)
            gldraw.xform_widget(se3.mul(left_gripper_link.getTransform(),LEFT_GRIPPER_CENTER_XFORM),0.05,0.005)
            gldraw.xform_widget(se3.mul(right_gripper_link.getTransform(),RIGHT_GRIPPER_CENTER_XFORM),0.05,0.005)

class Milestone1Master:
    def __init__(self, world):
        self.world = world
        self.robot = world.robot(0)
        self.config = self.robot.getConfig()
        self.left_camera_link = self.robot.link(LEFT_CAMERA_LINK_NAME)
        self.right_camera_link = self.robot.link(RIGHT_CAMERA_LINK_NAME)
        self.left_gripper_link = self.robot.link(LEFT_GRIPPER_LINK_NAME)
        self.right_gripper_link = self.robot.link(RIGHT_GRIPPER_LINK_NAME)
        self.left_arm_links = [self.robot.link(i) for i in LEFT_ARM_LINK_NAMES]
        self.right_arm_links = [self.robot.link(i) for i in RIGHT_ARM_LINK_NAMES]
        id_to_index = dict([(self.robot.link(i).getID(),i) for i in range(self.robot.numLinks())])
        self.left_arm_indices = [id_to_index[i.getID()] for i in self.left_arm_links]
        self.right_arm_indices = [id_to_index[i.getID()] for i in self.right_arm_links]

    def right_arm_ik(self, right_target):
        """Solves IK to move the right arm to the specified
            right_target ([x, y, z] in world space
        """
        qmin,qmax = self.robot.getJointLimits()
        for i in range(100):
            q = baxter_rest_config[:]
            for j in self.right_arm_indices:
                q[j] = random.uniform(qmin[j],qmax[j])
            #goal = ik.objective(self.right_gripper_link,local=[vectorops.sub(right_gripper_center_xform[1],[0,0,0.1]),right_gripper_center_xform[1]],world=[vectorops.add(target,[0,0,0.1]),target])
            goal = ik.objective(self.right_gripper_link,local=RIGHT_GRIPPER_CENTER_XFORM[1],world=right_target)
            if ik.solve(goal,tol=0.1):
                #self.config = self.robot.getConfig()
                print "ik done"
                print self.robot.getConfig()
                return True
            else:
                print "ik failed"
        return False

    def start(self):
        rospy.init_node("milestone1_master", anonymous=True)
        limb_left = baxter_interface.Limb('left')
        limb_right = baxter_interface.Limb('right')
        pc_processor = PCProcessor()
        #rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback)
        #rospy.spin()

        # print "Moving Left limb to 0"
        # limb_left.move_to_joint_positions(Q_LEFT_ZEROS)

        # print "Moving right limb to 0"
        # limb_right.move_to_joint_positions(Q_RIGHT_ZEROS)

        print "Scanning bin for point cloud"
        limb_right.move_to_joint_positions(Q_SCAN_BIN)
        cloud = "hi"
        cloud = pc_processor.subtractShelf(cloud)
        centroid = pc_processor.getCentroid(cloud)

        # print "Moving to centroid of cloud"
        # Calculate IK for cloud centroid
        # Move to the IK solution

        # print "Moving spatula to bin"
        # limb_left.move_to_joint_positions(Q_SPATULA_AT_BIN)

        # print "Scanning spatula"
        # limb_right.move_to_joint_positions(Q_SCAN_SPATULA)
        

if __name__ == '__main__':
    print "Starting Milestone1Master"
    
    world = WorldModel()
    #print "Loading full Baxter model (be patient, this will take a minute)..."
    #world.loadElement(os.path.join(model_dir,"baxter.rob"))
    print "Loading simplified Baxter model..."
    world.loadElement(os.path.join(KLAMPT_MODELS_DIR,"baxter_col.rob"))
    print "Loading Kiva pod model..."
    world.loadElement(os.path.join(KLAMPT_MODELS_DIR,"kiva_pod/model.obj"))
    print "Loading plane model..."
    world.loadElement(os.path.join(KLAMPT_MODELS_DIR,"plane.env"))
    
    #shift the Baxter up a bit (95cm)
    Rbase,tbase = world.robot(0).link(0).getParentTransform()
    world.robot(0).link(0).setParentTransform(Rbase,(0,0,0.95))
    world.robot(0).setConfig(world.robot(0).getConfig())
    
    #translate pod to be in front of the robot, and rotate the pod by 90 degrees 
    Trel = (so3.rotation((0,0,1),-math.pi/2),[1.2,0,0])
    T = world.rigidObject(0).getTransform()
    world.rigidObject(0).setTransform(*se3.mul(Trel,T))

    global baxter_rest_config
    f = open(KLAMPT_MODELS_DIR+'baxter_rest.config','r')
    baxter_rest_config = loader.readVector(f.readline())
    f.close()
    world.robot(0).setConfig(baxter_rest_config)
    
    # Initialize master
    master = Milestone1Master(world)
    master.right_arm_ik([50, 0, 0])
    #master.start()

    #run the visualizer
    visualizer = MyGLViewer(world)
    visualizer.run()
