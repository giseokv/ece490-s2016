#ifndef APC_MOTION_H
#define APC_MOTION_H

/** @file motion.h
 * @brief DLL interface to almost all of the APC motion functionality
 * (excluding sensors).  
 * 
 * Backend implementations can use ROS, kinematic simulation, Klamp't physics
 * etc.
 */

#ifndef BOOL
typedef int BOOL;
#endif

#define APIENTRY extern "C"

///Limb indices
enum { LEFT=0, RIGHT=1, BOTH=2 };

///Constants
const static int numLimbs = 2;
const static int numLimbDofs = 7;

////// CONFIGURATION ///////

///If you wish to use the motion queue or the planner, you must 
///call this before calling startup.  This loads the Klampt baxter.rob model
///from the given file
APIENTRY BOOL setKlamptModel(const char* klampt_model);

/** @brief Tell the robot to publish state to the state server on 
 * the given address.  Must be called before calling sendStartup()
 * 
 * Published state topics:
 * - .robot.t: time
 *         .dt: Controller command time step
 *         .sensors.q: sensed Klamp't joint configuration
 *                 .dq: sensed Klamp't joint velocity
 *                 *.base.odometry: estimated odometry of the base
 *                       .velocity: estimated velocity of the base
 *                 .head.pan: Baxter's head pan
 *                      .nodding: whether Baxter's head is nodding
 *                 .left.q: sensed Baxter limb joint configuration
 *                      .dq: sensed Baxter limb joint velocity
 *                      *.gripper.value: sensed gripper configuration
 *                               .force: sensed gripper force
 *                 .right... (same as above)
 *         .command.q: commanded Klamp't joint configuration
 *                 .dq: commanded Klamp't joint configuration
 *                 *.base.target: commanded position of the base (odometry coords)
 *                       .velocity: commanded velocity of the base
 *                 .head.pan: commanded pan target
 *                      .panspeed: commanded pan speed
 *                 .left.q: commanded Baxter limb joint configuration
 *                      .dq: commanded Baxter limb joint velocity
 *                      *.gripper.value: commanded gripper configuration
 *                               .speed: commanded gripper speed
 *                               .force: commanded gripper force
 *                 .right... (same as above)
 *         .endEffectors[0,1].xform.commanded: end effector transform of commanded config
 *                                 .sensed: end effector transform of sensed config
 *                                 .traj_end: final end effector transform, if using motion queu mode
 * - .controller.left.traj_t_end: the end time of the queued left arm motion
 *                   .traj_q_end: the end configuation of the queued motion
 *                   .traj.times: the trajectory milestone times of the queued motion (20 / s)
 *                   .traj.milestones: the trajectory milestones of the queued motion (20 / s)
 *              .right... (same as above)
 */
APIENTRY BOOL publishState(const char* system_state_addr="tcp://localhost:4568");


////// OVERALL ROBOT ///////

///Starts up the robot
APIENTRY BOOL sendStartup();
///Returns true if the robot is started
APIENTRY BOOL isStarted();
///Shuts down the robot
APIENTRY BOOL sendShutdown();
///Gets the time since startup
APIENTRY double getTime();
///Stops all motion
APIENTRY BOOL stopMotion();


////// HEAD ///////

///Returns true if the head is nodding
APIENTRY BOOL isHeadNodding();
///Returns the head pan angle
APIENTRY double getHeadPan();
///Moves the head to a given pan angle at the given speed
APIENTRY BOOL sendHeadPan(double target,double speed);


////// MOBILE BASE ///////

///Returns true if the mobile base is enabled
APIENTRY BOOL isMobileBaseEnabled();
///Returns true if the mobile base is moving
APIENTRY BOOL isMobileBaseMoving();
///Returns the time until the mobile base stops, or -1 if it's doing a velocity command
APIENTRY double getMobileBaseMoveTime();
///Returns the target for the mobile base in local coordinates
APIENTRY BOOL getMobileBaseTarget(double* xrel,double* yrel,double* thetarel);
///Returns the target for the mobile base in absolute (odometry) coordinates
APIENTRY BOOL getMobileBaseOdometryTarget(double* x,double* y,double* theta);
///Returns mobile base velocity in local coordinates
APIENTRY BOOL getMobileBaseVelocity(double* dx,double* dy,double* dtheta);
///Returns odometry coordinates of the mobile base
APIENTRY BOOL getMobileBaseOdometry(double* x,double* y,double* theta);
///Sends a move target for the mobile base, in local coordinates
APIENTRY BOOL sendMobileBasePosition(double xrel,double yrel,double thetarel);
///Sends a move target for the mobile base, in absolute (odometry) coordinates
APIENTRY BOOL sendMobileBaseOdometryPosition(double x,double y,double theta);
///Sends a move velocity for the mobile base, in local coordinates
APIENTRY BOOL sendMobileBaseVelocity(double dxrel,double dyrel,double dthetarel);


////// LIMB (LOW-LEVEL) ///////
///Returns true the limb is being commanded in position mode
APIENTRY BOOL isLimbPositionMode(int limb);
///Returns true the limb is being commanded in velocity mode
APIENTRY BOOL isLimbVelocityMode(int limb);
///Returns true the limb is being commanded in effort mode
APIENTRY BOOL isLimbEffortMode(int limb);
///Returns true the limb is being commanded in raw position mode
APIENTRY BOOL isLimbRawPositionMode(int limb);
///Returns the sensed limb position
APIENTRY BOOL getLimbPosition(int limb,double* angles);
///Returns the sensed limb velocity
APIENTRY BOOL getLimbVelocity(int limb,double* dangles);
///Returns the sensed limb effort
APIENTRY BOOL getLimbEffort(int limb,double* efforts);
///Returns the commanded limb position
APIENTRY BOOL getLimbCommandedPosition(int limb,double* angles);
///Returns the commanded limb velocity
APIENTRY BOOL getLimbCommandedVelocity(int limb,double* dangles);
///Sends a limb position command
APIENTRY BOOL sendLimbPosition(int limb,const double* angles);
///Sends a limb raw position command
APIENTRY BOOL sendLimbRawPosition(int limb,const double* angles);
///Sends a limb velocity command
APIENTRY BOOL sendLimbVelocity(int limb,const double* angles);
///Sends a limb effort command
APIENTRY BOOL sendLimbEffort(int limb,const double* efforts);
///If enabled=true, the limb will use Baxter position commands for the
///motion queue and drive modes.  Position commands are filtered using 
///Baxter's internal self-collision avoidance (on by default).
///Otherwise, it will use raw position commands, which do not.  Disable
///only if you are sure that your trajectories are collision free!
APIENTRY BOOL enableLimbSelfCollisionAvoidance(int limb,bool enabled);

////// END EFFECTOR ///////

///Returns the end effector transformation.   The position of the end effector
///is that of the gripper base. The mobile base odometry is ignored. 
///
///rotation is a 9-element array denoting the rotation matrix in world space,
///in column-major form.
///position is a 3-element array denoting the end effector position in world space.
APIENTRY BOOL getEndEffectorSensedTransform(int limb,double* rotation,double* position);
///Returns the end effector velocity.   The position of the end effector
///is that of the gripper base. The mobile base velocity / odometry is ignored. 
///
///angVel is a 3-element array denoting the angular velocity in world space.
///vel is a 3-element array denoting the velocity in world space.
APIENTRY BOOL getEndEffectorSensedVelocity(int limb,double* angVel,double* vel);
///Returns the end effector transformation.   The position of the end effector
///is that of the gripper base. The mobile base odometry is ignored. 
///
///rotation is a 9-element array denoting the rotation matrix in world space,
///in column-major form.
///position is a 3-element array denoting the end effector position in world space.
APIENTRY BOOL getEndEffectorCommandedTransform(int limb,double* rotation,double* position);
///Returns the end effector velocity.   The position of the end effector
///is that of the gripper base. The mobile base velocity / odometry is ignored. 
///
///angVel is a 3-element array denoting the angular velocity in world space.
///vel is a 3-element array denoting the velocity in world space.
APIENTRY BOOL getEndEffectorCommandedVelocity(int limb,double* angVel,double* vel);
///Sends an end effector velocity command.   The position of the end effector
///is that of the gripper base. The mobile base velocity / odometry is ignored. 
///
///angVel is a 3-element array denoting the angular velocity in world space.
///vel is a 3-element array denoting the velocity in world space.
APIENTRY BOOL sendEndEffectorVelocity(int limb,const double* angVel,const double* vel);
///Sends an end effector move-to command.   The position of the end effector
///is that of the gripper base. The mobile base velocity / odometry is ignored. 
///Note: The interpolation is NOT linear in cartesian space.
///
///rotation is a 9-element array denoting the destination rotation matrix in world space,
///in column-major form.
///position is a 3-element array denoting the end effector position in world space.
APIENTRY BOOL sendEndEffectorMoveTo(int limb,const double* rotation,const double* position);
///Sends an end effector "drive" command.   The position of the end effector
///is that of the gripper base. The mobile base velocity / odometry is ignored. 
///
///angVel is a 3-element array denoting the angular velocity in world space.
///vel is a 3-element array denoting the velocity in world space.
///
///This differs from the sendEndEffectorVelocity command in that the end effector is
///consistently driven to follow a screw motion in Cartesian space starting from
///its current commanded transform.  sendEndEffectorVelocity only sends an
///instantaneous velocity which is translated into joint velocities, which drifts
///away from the integrated Cartesian motion over time.
APIENTRY BOOL sendEndEffectorDrive(int limb,const double* angVel,const double* vel);


////// GRIPPER ///////

///Returns true if the gripper is enabled
APIENTRY BOOL isGripperEnabled(int limb);
///Returns the type string of the gripper in the given char* buffer
APIENTRY BOOL getGripperType(int limb,char* buf,int bufsize);
///Returns the number of DOFs for controlling the gripper
APIENTRY int numGripperDofs(int limb);
///Returns true the gripper is moving to the desired setpoint
APIENTRY BOOL isGripperMoving(int limb);
///Returns the estimated time until the gripper stops
APIENTRY double getGripperMoveTime(int limb);
///Returns the gripper position
APIENTRY BOOL getGripperPosition(int limb,double* config);
///Returns the gripper target
APIENTRY BOOL getGripperTarget(int limb,double* config);
///Returns the gripper effort
APIENTRY BOOL getGripperEffort(int limb,double* config);
///Tells the gripper to close
APIENTRY BOOL sendCloseGripper(int limb);
///Tells the gripper to open
APIENTRY BOOL sendOpenGripper(int limb);
///Tells the gripper to open/close to the given position / speed, stopping at the given effort
APIENTRY BOOL sendSetGripper(int limb,const double* position,const double* speed,const double* effort);


////// LIMB MOTION QUEUE ///////

///Returns true if the limb is being controlled by the motion queue
APIENTRY BOOL isMotionQueueEnabled(int limb);
///Returns true if the limb's motion queue currently stores an active motion
APIENTRY BOOL isMotionQueueMoving(int limb);
///Returns the estimated amount of time until the motion queue stops
APIENTRY double getMotionQueueMoveTime(int limb);
///Returns the end configuration of the motion queue
APIENTRY BOOL getMotionQueueTarget(int limb,double* angles);
///Interpolates linearly from the current configuration to the desired angles over the given duration
APIENTRY BOOL sendMotionQueueLinear(int limb,double duration,const double* angles);
///Interpolates cubically from the current config/velocity to the desired config/velocity over the given duration
APIENTRY BOOL sendMotionQueueCubic(int limb,double duration,const double* angles,const double* dangles);
///Moves the limb smoothly from the current config to the desired milestone according to
///the robot's velocity/acceleration limits.  Requires setKlamptModel()
APIENTRY BOOL sendMotionQueueRamp(int limb,const double* angles,double speed=1.0);
///Appends a linear interpolation to the desired angles over the given duration
APIENTRY BOOL sendMotionQueueAppendLinear(int limb,double duration,const double* angles);
///Appends a cubic interpolation  to the desired config/velocity over the given duration
APIENTRY BOOL sendMotionQueueAppendCubic(int limb,double duration,const double* angles,const double* dangles);
///Appends the given milestone to the motion queue
APIENTRY BOOL sendMotionQueueAppendRamp(int limb,const double* angles,double speed=1.0);
///Appends a smooth motion along a straight joint-space path to the desired milestone
///that starts/stops smoothly according to the robot's velocity/acceleration
///limits.  Requires setKlamptModel()
APIENTRY BOOL sendMotionQueueAppendLinearRamp(int limb,const double* angles,double speed=1.0);
///Sends a trajectory starting from the current configuration.  Milestones are given as an array of length
///numPoints*n, where n is the dimensionality of the limb.  If vmilestones is provided, then it is an
///array of the same size designating the velocities at the milestones, and cubic interpolation is performed.
///Otherwise, linear interpolation is performed.
APIENTRY BOOL sendMotionQueueTrajectory(int limb,int numPoints,const double* times,const double* milestones,const double* vmilestones=0);
///Sends a trajectory starting from the end of the current .  Milestones are given as an array of length
///numPoints*n, where n is the dimensionality of the limb.  If vmilestones is provided, then it is an
///array of the same size designating the velocities at the milestones, and cubic interpolation is performed.
///Otherwise, linear interpolation is performed.
APIENTRY BOOL sendMotionQueueAppendTrajectory(int limb,int numPoints,const double* times,const double* milestones,const double* vmilestones=0);

////// LIMB PLANNER  ///////

///Returns true the if limb's motion queue is being controlled by the planner
APIENTRY BOOL isPlannerEnabled(int limb);
///Sends a pointer to a Klampt/Planning/PlannerObjective object to the planner
APIENTRY BOOL sendPlannerObjective(void* pPlannerObjective);
///Sends a string in JSON PlannerObjective format to the planner
APIENTRY BOOL sendPlannerObjectiveStr(const char* pPlannerObjective);
///Stops the planner
APIENTRY BOOL stopPlanner();
///Returns the objective function obtained by the planner
APIENTRY double plannerObjectiveValue();
///Sets the world file used by the planner
APIENTRY BOOL setPlannerWorldFile(const char* worldFile);
///Adds an obstacle to the planner, returns its ID
APIENTRY int addPlannerObstacle(const char* obstacleFile);
///Deletes an obstacle from the planner, given its id
APIENTRY int deletePlannerObstacle(int id);
///Sets the obstacle avoidance margin for the given obstacle
APIENTRY BOOL setPlannerObstacleMargin(int id,double margin);
///Clears the world used by the planner
APIENTRY BOOL clearPlannerWorld();


////// UTILITIES ///////

///Loads a calibration file from disk and enables it.  Only has an effect
///in physical mode.  Uses a JSON file output from
///baxter_motor_calibration/calibrate.py.
///If fn=NULL or loading the calibration failed, returns false and disables
///calibration.
APIENTRY bool loadCalibration(const char* fn);

///Retreives the pointer to the Klamp't Robot model, if using
APIENTRY void* getKlamptModel();
///Retrieves the number of DOFs in the Klamp't model.  setKlamptModel() must be called first.
APIENTRY int getKlamptNumDofs();
///Retrieves the sensed Klamp't configuration.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptSensedPosition(double* klamptConfig);
///Retrieves the sensed Klamp't velocity.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptSensedVelocity(double* klamptVelocity);
///Retrieves the commanded Klamp't configuration.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptCommandedPosition(double* klamptConfig);
///Retrieves the commanded Klamp't velocity.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptCommandedVelocity(double* klamptVelocity);
///Sends a velocity command with the given Klamp't velocities.  setKlamptModel() must be called first.
APIENTRY BOOL sendKlamptMoveVelocity(const double* klamptVelocity);
///Sends a smooth motion command to the given target configuration.  setKlamptModel() must be called first.
APIENTRY BOOL sendKlamptMoveToTarget(const double* klamptConfig);
///Retrieves the limb indices for the Klampt model.  setKlamptModel() must be called first
APIENTRY BOOL getKlamptLimbIndices(int limb,int* indices);
///Retrieves the head pan index for the Klampt model, or -1 if setKlamptModel() was not called first.
APIENTRY int getKlamptHeadPanIndex();
///Retrieves the mobile base indices for the Klampt model, returns 0 if no base is defined or
///setKlamptModel() is not called first
APIENTRY BOOL getKlamptMobileBaseIndices(int* x,int* y,int* theta);
///Retrieves the gripper indices for the Klampt model, or 0 if the gripper is not defined or
///setKlamptModel() was not called first.
APIENTRY BOOL getKlamptGripperIndices(int limb,int* indices);
///Retrieves the limb configuration for a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptLimb(const double* klamptConfig,int limb,double* out);
///Retrieves the head pan for a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptHeadPan(const double* klamptConfig,double* out);
///Retrieves the mobile base coordinates for a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptMobileBase(const double* klamptConfig,double* x,double* y,double* theta);
///Retrieves the gripper config for a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL getKlamptGripper(const double* klamptConfig,int limb,double* out);
///Copies the limb configuration into a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL setKlamptLimb(const double* limbConfig,int limb,double* klamptConfig);
///Copies the head pan into a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL setKlamptHeadPan(double pan,double* klamptConfig);
///Copies the mobile base coordinates for a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL setKlamptMobileBase(double x,double y,double theta,double* klamptConfig);
///Copies the gripper configuration for a given Klamp't configuration.
///Also works for velocities.  setKlamptModel() must be called first.
APIENTRY BOOL setKlamptGripper(const double* gripperConfig,int limb,double* klamptConfig);

#endif
