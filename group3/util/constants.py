import math
from klampt import vectorops,so3

# Constants that affect the state machine
INITIAL_STATE = "START"
REAL_VACUUM = False
REAL_PERCEPTION = True
SEGMENT = True
CALIBRATE = False
SELECT_REAL_BIN = False
HARDCODED_BIN = 'H'

# Constants related to printing output
PRINT_BLOBS = True
PRINT_LABELS_AND_SCORES = True
VERBOSE = True

# Downsample ratio
STEP = 15

# Right arm configurations
Q_SCAN_BIN_A = [1.0189467371887209, -0.8908593415466309, -0.12118448210449219, 1.5880536088439943, 0.00843689432373047, 0.21514080525512697, 0.7574030131530762]
Q_IK_SEED_A = [1.1109855843566896, -0.7554855371704102, -0.16528642970581056, 0.2442864401916504, 0.120800986907959, -0.04985437554931641, 0.45635928387451175]
Q_AFTER_SCAN_A = []


################################################################################################
Q_SCAN_BIN_B = [0.7681408786560059, -0.9518350777954102, -0.08782040000610353, 1.6386749747863771, 0.06481068821411133, 0.11658253974609376, 0.7823302009277344]
Q_IK_SEED_B = [0.8302671004943848, -0.6741845555053712, 0.04448544279785156, 0.3915485956604004, 0.0019174759826660157, -0.08973787598876953, 0.26384469521484377]
Q_AFTER_SCAN_B = []

################################################################################################
Q_SCAN_BIN_C = [0.5027622026550294, -1.0074418812927246, -0.0011504855895996095, 1.6106798254394532, -0.09932525590209962, 0.06711165939331055, 0.9173205101074219]
Q_IK_SEED_C = [0.5840631843200684, -0.6093738672912598, 0.1464951650756836, 0.5449466742736817, -0.013038836682128907, -0.1223349676940918, 0.09242234236450196]
Q_AFTER_SCAN_C = [0.20133497817993165, -1.3107865817504885, 0.0847524384338379, 0.9422476978820802, 0.14534467948608398, 1.9872721084350586, -0.5687233764587403]
Q_AFTER_SCAN2_C = [-0.2615437240356446, -1.3982234865600587, 0.4743835581115723, 1.05116033369751, 0.7083156279968262, 0.8628641921997071, -0.38848063408813477]

################################################################################################
Q_SCAN_BIN_D = [1.0262331459228515, -0.8402379756042481, -0.13805827075195312, 1.4457768909301758, 0.023393206988525393, 0.10009224629516603, 1.0492428577148438]
Q_IK_SEED_D = [1.2283351144958496, -0.44562141837158203, 0.27189809434204104, 0.1468786602722168, -0.05253884192504883, -0.43143209609985356, 0.462495207019043]

Q_AFTER_SCAN_D = []
#much better if joint 7 is nonzero Q_AFTER_SCAN2_D = [0.5334418183776856, -1.1865341380737306, 1.1385972385070802, 2.0137332769958496, 0.9832816839111329, -1.2103108402587892, -0.6396699878173828]


################################################################################################
Q_SCAN_BIN_E = [0.7919175808410646, -1.0450244105529787, -0.05829126987304688, 1.4499953380920412, -0.03183010131225586, 0.04026699563598633, 1.302349687426758]
Q_IK_SEED_E = [0.9468496402404786, -0.5752427947998048, 0.30717965242309575, -0.06902913537597656, -0.1457281746826172, -0.2914563493652344, 0.7332428157714844]
Q_AFTER_SCAN_E = [-0.2726650847351074, -1.3986069817565918, 0.9970875109863282, 2.3289663285461426, -0.12770390044555666, 0.8471408891418457, 0.018407769433593752]
Q_AFTER_SCAN2_E = [-0.2688301327697754, -1.3982234865600587, 1.0388884874084474, 2.30825758793335, -0.06711165939331055, -0.9138690533386231, 0.00728640873413086]

################################################################################################
Q_SCAN_BIN_F = [0.602087458557129, -1.0204807179748536, -0.10277671267089844, 1.5504710795837404, -0.16106798254394533, -0.05714078428344727, 1.2210487057617188]
Q_IK_SEED_F = [0.6216457135803223, -0.8540438026794435, 0.14802914586181642, -0.1702718672607422, -0.1457281746826172, -0.09587379913330078, 1.1083011179809572]
Q_AFTER_SCAN_F = [-0.06596117380371094, -1.3702283372131348, 0.5065971546203614, 2.4037478918701174, -0.21053886289672852, 0.5786942515686035, -0.16375244891967775]
Q_AFTER_SCAN2_F = [-0.12770390044555666, -1.3805827075195314, 0.6354515406555176, 2.1402866918518066, -0.03873301484985352, -0.7481991284362793, -0.03834951965332031]

###############################################################################################
Q_SCAN_BIN_G = [1.1773302533569336, -0.6876068873840332, 0.04141748122558594, 1.138213743310547, -0.09510680874023437, -0.07401457293090821, 1.2766555092590333]
Q_IK_SEED_G = [1.187301128466797, -0.47668452929077154, 0.17909225678100588, -0.4460049135681153, -0.14266021311035157, -0.15301458341674806, 1.059213732824707]
Q_AFTER_SCAN_G = [1.1036991756225587, -0.8214467109741211, 0.22281070918579102, 2.2327090342163087, 0.33210684019775394, -0.08935438079223633, -0.1852281799255371]
Q_AFTER_SCAN2_G = [0.9384127459167481, -0.9491506114196778, 0.34744664805908204, 2.233476024609375, 0.3804272349609375, -1.2962137642822267, -0.18292720874633792]

################################################################################################
Q_SCAN_BIN_H = [0.979830227142334, -0.8114758358642579, -0.13153885241088867, 1.5163400070922852, 0.0977912751159668, 0.8387039948181153, 0.0]
Q_IK_SEED_H = [0.9019807022460938, -0.8348690428527833, -0.09242234236450196, 2.0056798778686526, 0.04525243319091797, -1.2279516192993165, 0.0]
Q_AFTER_SCAN = [0.5740923092102052, -1.1692768542297365, 0.12923788123168947, 2.5866751006164552, -0.06941263057250976, 0.02185922620239258, 0.0]
Q_AFTER_SCAN2 = [0.22933012752685547, -1.3019661922302248, 0.45674277907104494, 2.476611979211426, -0.21629129084472656, -1.0653496559692384, 0.0]

################################################################################################
Q_SCAN_BIN_I = [0.7106165991760255, -0.6810874690429688, 0.07478156332397462, 1.2256506481201173, -0.10431069345703126, -0.20133497817993165, 1.2409904559814453]
Q_IK_SEED_I = [0.651174843713379, -0.3666214078857422, 0.09970875109863282, -0.4893398707763672, -0.06864564017944337, -0.13307283319702148, 0.9238399284484864]
Q_AFTER_SCAN_I = [0.2653786760009766, -0.5890486218750001, -0.05829126987304688, 1.9358837520996095, -0.6442719301757813, 0.11543205415649414, 0.12962137642822266]
Q_AFTER_SCAN2_I = [-0.05330583231811524, -0.8904758463500977, 0.24313595460205079, 2.1456556246032714, -0.6427379493896485, -1.1681263686401369, 0.07669903930664063]

################################################################################################
Q_SCAN_BIN_J = [1.3936215442016602, -0.04716990917358399, 0.5963350306091308, 1.0319855738708497, -0.19788352141113283, -0.4571262742675782, 0.845606908355713]
Q_IK_SEED_J = [1.1581554935302736, 0.32213596508789066, 0.5756262899963379, -0.33172334500122075, -0.15953400175781252, -0.43373306727905275, 0.16260196333007815]
Q_AFTER_SCAN_J = [1.5125050551269532, -0.42798063933105474, -0.15569904979248048, 1.8346410202148438, 0.5595194917419434, 0.20401944455566406, -0.09472331354370118]
Q_AFTER_SCAN2_J = [1.5523885555664063, -0.05867476506958008, -0.06902913537597656, 1.3986069817565918, 0.8793544856506348, -1.3947720297912598, 0.0038349519653320314]

################################################################################################

Q_SCAN_BIN_K = [0.9031311878356935, -0.2669126567871094, 0.08053399127197267, 0.8122428262573242, -0.05829126987304688, -0.08666991441650392, 1.196505013183594]
Q_IK_SEED_K = [0.9069661398010255, 0.30986411879882814, 0.4613447214294434, -0.46901462536010746, -0.09970875109863282, -0.34936412404174805, 0.2703641135559082]
Q_AFTER_SCAN_K = [0.822980691760254, -1.0285341171020508, -0.07401457293090821, 2.4052818726562504, -0.034898062884521484, 0.2653786760009766, -0.02531068297119141]
Q_AFTER_SCAN2_K = [0.7819467057312012, -0.6914418393493653, -0.04601942358398438, 2.1847721346496582, -0.04026699563598633, -1.2570972542358398, -0.027228158953857422]

################################################################################################
Q_SCAN_BIN_L = [0.4394854952270508, -0.22472818516845705, -0.220893233203125, 0.800354475164795, -0.27765052229003906, 0.09587379913330078, 1.1351457817382813]
Q_IK_SEED_L = [0.5687233764587403, 0.4103398602905274, 0.27381557032470705, -0.33594179216308595, -0.019174759826660157, -0.30027673888549805, -0.010737865502929688]
Q_AFTER_SCAN_L = [-0.03834951965332031, -0.7639224314941406, 0.1560825449890137, 2.1514080525512695, -0.7738933066040039, 0.21322332927246096, 0.02799514934692383]
Q_AFTER_SCAN2_L = [-0.05253884192504883, -0.2285631371337891, 0.23930100263671877, 1.6973497398559572, -0.7282573782165528, -1.3748302795715333, 0.015339807861328126]

################################################################################################
Q_STOW = [1.0, 0.28, 0.0, 0.9, 0.0, 0.0, 0.0]

# Right arm calibration configs, see pics on Google Drive
Q_CALIBRATE_BIN_E = [1.198805984362793, -0.551082597418213, -0.4406359808166504, 1.0392719826049805, 0.42069423059692385, -0.5196359913024903, -0.14189322271728516]
Q_CALIBRATE_BIN_H = [0.9088836157836915, -0.1096796262084961, -0.46364569260864263, 0.6841554306152344, 0.5288398760192872, -0.3531990760070801, -0.15531555459594729]

# 7 list, each element is a 2 list of lower then upper acceptable bound
ELBOW_UP_BOUNDS = [[-10, 10], [-10, 10], [-.3, .3], [-10, 10], [-.5, .5], [-10, 10], [-10, 10]]

# Number of histograms per object
NUM_HIST_PER_OBJECT = 4

# Left arm configurations
Q_SPATULA_AT_BIN = [0.08053399127197267, 0.5610534725280762, -1.4894953433349611, 0.830650595690918, -2.828277074432373, -1.3989904769531252, 0.0]

# Paths
REPO_ROOT = "/home/group3/ece490-s2016"
KLAMPT_MODELS_DIR = REPO_ROOT + "/apc2015/klampt_models/"
LIBPATH = REPO_ROOT + "/common/"
VACUUM_PCD_FILE = REPO_ROOT + "/group3/planning/custom_vacuum.pcd"
PICK_JSON_PATH = REPO_ROOT + '/group3/integration/apc_pick_task.json'
PERCEPTION_DIR = REPO_ROOT + "/group3/perception"
BIN_NPZ_FOLDER = PERCEPTION_DIR + "/empty_bins/" # A.npz, B.npz
MAT_PATH = PERCEPTION_DIR + "/matpcl/"
CLOUD_MAT_PATH = MAT_PATH + "cloud.mat"
CHENYU_GO_PATH = MAT_PATH + "chenyugo.txt"
CHENYU_DONE_PATH = MAT_PATH + "chenyudone.txt"
ARDUINO_SERIAL_PORT = "/dev/ttyACM1"
ROS_DEPTH_TOPIC = "/realsense/pc"
PICK_JSON_PATH = REPO_ROOT + '/group3/planning/apc_pick_task.json'

# Indices in Baxter robot file link
LEFT_CAMERA_LINK_NAME = 'left_hand_camera'
RIGHT_CAMERA_LINK_NAME = 'right_hand_camera'
LEFT_GRIPPER_LINK_NAME = 'left_gripper'
RIGHT_GRIPPER_LINK_NAME = 'right_gripper'
LEFT_ARM_LINK_NAMES = ['left_upper_shoulder','left_lower_shoulder','left_upper_elbow','left_lower_elbow','left_upper_forearm','left_lower_forearm','left_wrist']
RIGHT_ARM_LINK_NAMES = ['right_upper_shoulder','right_lower_shoulder','right_upper_elbow','right_lower_elbow','right_upper_forearm','right_lower_forearm','right_wrist']

# Local transform from right_wrist to vacuum point
VACUUM_POINT_XFORM = (so3.identity(), [.07, 0.02, .38])

# Local transform from right_lower_forearm to F200
RIGHT_F200_CAMERA_CALIBRATED_XFORM =([-0.02003573380863745, 0.008438993066848435, -0.9997636484523572, 0.9007673343323835, 0.4340635880118531, -0.014387875521042898, 0.43383957722928207, -0.9008427082228592, -0.01629835179470207], [0.07999999999999981, -0.1, -0.05])

# Transform of shelf relative to world
SHELF_MODEL_XFORM = [1.43,-.23,-.02]

# Distances (meters)
GRASP_MOVE_DISTANCE = .05
BACK_UP_DISTANCE = .2

# Times (seconds)
MOVE_TIME = 2
SCAN_WAIT_TIME = 0 if REAL_PERCEPTION else 0
GRASP_WAIT_TIME = 2 if REAL_VACUUM else 0


ITEM_SCORES = {
    "i_am_a_bunny_book":1,
    "laugh_out_loud_joke_book":1,
    "scotch_bubble_mailer":1,
    "up_glucose_bottle":1,
    "dasani_water_bottle":1,
    "rawlings_baseball":1,
    "folgers_classic_roast_coffee":1,
    "elmers_washable_no_run_school_glue":1,
    "hanes_tube_socks":1,
    "womens_knit_gloves":1,
    "cherokee_easy_tee_shirt":1,
    "peva_shower_curtain_liner":1,
    "cloud_b_plush_bear":1,
    "barkely_hide_bones":1,
    "kyjen_squeakin_eggs_plush_puppies":1,
    "cool_shot_glue_sticks":1,
    "creativity_chenille_stems":1,
    "soft_white_lightbulb":1,
    "safety_first_outlet_plugs":1,
    "oral_b_toothbrush_green":1,
    "oral_b_toothbrush_red": 1,
    "dr_browns_bottle_brush":1,
    "command_hooks":1,
    "easter_turtle_sippy_cup":1,
    "fiskars_scissors_red":1,
    "scotch_duct_tape":1,
    "woods_extension_cord":1,
    "platinum_pets_dog_bowl":1,
    "fitness_gear_3lb_dumbbell":1,
    "rolodex_jumbo_pencil_cup":1,
    "clorox_utility_brush":1,
    "kleenex_paper_towels":1,
    "expo_dry_erase_board_eraser":1,
    "kleenex_tissue_box":1,
    "ticonderoga_12_pencils":1,
    "crayola_24_ct":1,
    "jane_eyre_dvd":1,
    "dove_beauty_bar":1,
    "staples_index_cards":1
}

ITEM_NUMBERS = {
    "i_am_a_bunny_book":1,
    "laugh_out_loud_joke_book":2,
    "scotch_bubble_mailer":3,
    "up_glucose_bottle":4,
    "dasani_water_bottle":5,
    "rawlings_baseball":6,
    "folgers_classic_roast_coffee":7,
    "elmers_washable_no_run_school_glue":8,
    "hanes_tube_socks":9,
    "womens_knit_gloves":10,
    "cherokee_easy_tee_shirt":11,
    "peva_shower_curtain_liner":12,
    "cloud_b_plush_bear":13,
    "barkely_hide_bones":14,
    "kyjen_squeakin_eggs_plush_puppies":15,
    "cool_shot_glue_sticks":16,
    "creativity_chenille_stems":17,
    "soft_white_lightbulb":18,
    "safety_first_outlet_plugs":19,
    "oral_b_toothbrush_green":20,
    "oral_b_toothbrush_red": 21,
    "dr_browns_bottle_brush":22,
    "command_hooks":23,
    "easter_turtle_sippy_cup":24,
    "fiskars_scissors_red":25,
    "scotch_duct_tape":26,
    "woods_extension_cord":27,
    "platinum_pets_dog_bowl":28,
    "fitness_gear_3lb_dumbbell":29,
    "rolodex_jumbo_pencil_cup":30,
    "clorox_utility_brush":31,
    "kleenex_paper_towels":32,
    "expo_dry_erase_board_eraser":33,
    "kleenex_tissue_box":34,
    "ticonderoga_12_pencils":35,
    "crayola_24_ct":36,
    "jane_eyre_dvd":37,
    "dove_beauty_bar":38,
    "staples_index_cards":39
}