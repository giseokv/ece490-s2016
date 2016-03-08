import math
from klampt import vectorops,so3

INITIAL_STATE = "MOVING_TO_GRASP_OBJECT"

# Old positions for scanning bin when the camera was mounted on the right_lower_forearm rather than the right_lower_elbow
# Q_SCAN_BIN = {'right_s0': 0.6519418341064454, 'right_s1': -0.008820389520263672, 'right_w0': -0.056373793890380865, 'right_w1': -1.1485681136169434, 'right_w2': 0.24620391617431642, 'right_e0': 1.342233187866211, 'right_e1': 1.5010001992309572}
#Q_SCAN_BIN = [0.6519418341064454, -0.008820389520263672, 1.342233187866211, 1.5010001992309572, -0.056373793890380865, -1.1485681136169434, 0.24620391617431642]
# Q_SPATULA_AT_BIN = {'left_w0': -2.828277074432373, 'left_w1': -1.3989904769531252, 'left_w2': -1.193053556414795, 'left_e0': -1.4894953433349611, 'left_e1': 0.830650595690918, 'left_s0': 0.08053399127197267, 'left_s1': 0.5610534725280762}
Q_SPATULA_AT_BIN = [0.08053399127197267, 0.5610534725280762, -1.4894953433349611, 0.830650595690918, -2.828277074432373, -1.3989904769531252, 0.0]
# Q_SCAN_SPATULA = {'right_s0': 1.0864418917785645, 'right_s1': -0.8402379756042481, 'right_w0': -0.19251458865966797, 'right_w1': 1.5585244787109376, 'right_w2': 0.3367087825561524, 'right_e0': 0.2876213973999024, 'right_e1': 0.8034224367370606}

Q_INTERMEDIATE_1 = [-0.1606844873474121, -1.2072428786865235, -0.12003399651489259, 2.585908110223389, -0.17487380961914065, -1.5251603966125489, 0.0]
Q_SCAN_BIN = [0.9648739144775391, -0.930742841986084, -0.0007669903930664063, 1.9638789014465334, -0.12962137642822266, 0.17180584804687501, 0.0]


KLAMPT_MODELS_DIR = "/home/group3/ece490-s2016/apc2015/klampt_models/"
LIBPATH = "../../common/"
SHELF_NPZ_FILE = "/home/group3/ece490-s2016/group3/perception/shelf.npz"

#indices of the left and right cameras in the Baxter robot file
LEFT_CAMERA_LINK_NAME = 'left_hand_camera'
RIGHT_CAMERA_LINK_NAME = 'right_hand_camera'

#indices of the left and right grippers in the Baxter robot file
LEFT_GRIPPER_LINK_NAME = 'left_gripper'
RIGHT_GRIPPER_LINK_NAME = 'right_gripper'

#indices of the left and right arms in the Baxter robot file
LEFT_ARM_LINK_NAMES = ['left_upper_shoulder','left_lower_shoulder','left_upper_elbow','left_lower_elbow','left_upper_forearm','left_lower_forearm','left_wrist']
RIGHT_ARM_LINK_NAMES = ['right_upper_shoulder','right_lower_shoulder','right_upper_elbow','right_lower_elbow','right_upper_forearm','right_lower_forearm','right_wrist']

#local transformations (rotation, translation pairs) of the grasp center
LEFT_GRIPPER_CENTER_XFORM = (so3.identity(),[0,-0.04,0.1])
RIGHT_GRIPPER_CENTER_XFORM = (so3.identity(),[0,-0.04,0.1])

# Local transform from right_wrist to F200
RIGHT_F200_CAMERA_XFORM = (so3.mul(so3.rotation([1, 0, 0], math.pi / 2), so3.rotation([0, 0, 1], 3 * math.pi / 2)), [.07, -.1, 0])
RIGHT_F200_CAMERA_CALIBRATED_XFORM = ([-0.13894635239615533, -0.9886236474475394, 0.05759509409079229, 0.460160658969247, -0.012955497176371563, 0.8877411351457709, -0.8768957059381646, 0.14985138905074202, 0.45672582815817564], [0.07, -0.1, 0])



# Local transform from right_wrist to vacuum point
VACUUM_POINT_XFORM = (so3.identity(), [.07, 0, .43])

# Transform from right_wrist to end of pencil
RIGHT_PENCIL_XFORM = (so3.identity(), [0, 0, 0])

ROS_DEPTH_TOPIC = "/camera/depth/points"