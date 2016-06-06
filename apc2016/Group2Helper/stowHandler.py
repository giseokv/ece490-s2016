CONST_ITEM_NAMES = ["i_am_a_bunny_book",
"laugh_out_loud_joke_book",
"scotch_bubble_mailer",
"scotch_bubble_mailer",
"up_glucose_bottle",
"dasani_water_bottle",
"dasani_water_bottle",
"rawlings_baseball",
"folgers_classic_roast_coffee",
"elmers_washable_no_run_school_glue",
"elmers_washable_no_run_school_glue",
"hanes_tube_socks",
"womens_knit_gloves",
"cherokee_easy_tee_shirt",
"peva_shower_curtain_liner",
"cloud_b_plush_bear",
"barkely_hide_bones",
"kyjen_squeakin_eggs_plush_puppies",
"cool_shot_glue_sticks",
"creativity_chenille_stems",
"creativity_chenille_stems",
"soft_white_lightbulb",
"safety_first_outlet_plugs",
"oral_b_toothbrush_green",
"oral_b_toothbrush_red",
"dr_browns_bottle_brush",
"command_hooks",
"easter_turtle_sippy_cup",
"fiskars_scissors_red",
"scotch_duct_tape",
"scotch_duct_tape",
"woods_extension_cord",
"platinum_pets_dog_bowl",
"fitness_gear_3lb_dumbbell",
"rolodex_jumbo_pencil_cup",
"clorox_utility_brush",
"kleenex_paper_towels",
"expo_dry_erase_board_eraser",
"expo_dry_erase_board_eraser",
"kleenex_tissue_box",
"ticonderoga_12_pencils",
"crayola_24_ct",
"jane_eyre_dvd",
"dove_beauty_bar",
"staples_index_cards",
"staples_index_cards"]
CONST_ITEM_WEIGHTS=[3.2, 2.9, 1.6, 1.6, 11.2, 16.9, 16.9,
6, 11.3, 4, 4, 16, 2,
1, 11.8, 3.2, 4, 3.2,
2.4, 4, 4, 3, 0.3, 0.5, 0.5,
4.2, 1.6, 12, 1.4, 2, 2,
6.4, 1.6, 48, 3.2, 7,
12.8, 0.3, 0.3, 10, 2.1, 8,
5.12, 4, 3, 3] 

import sys

sys.path.insert(0, "../../common")
sys.path.insert(0, "..")
from Sensors import scale
import json
import json_parser_stow

class stowHandler:
    def __init__(self,filename=None):
        self.parser=json_parser_stow.json_parser_stow()
        
        self.scale = None
        self.currentWeight = 100
        try:
            self.scale=scale.Scale()
            self.currentWeight=self.scale.read().split(' ')[0]
            print 'Initial Reading', self.currentWeight
            self.currentWeight = self.currentWeight.split(' ')[0]
            print 'Numeric Reading', self.currentWeight
        except:
            print 'Scale not connected'

        if filename is not None:
            (binContents, toteContents)=self.parser.readInFile(filename)
            print toteContents
    def pickWhichObj(self, debug=False):
    	newWeight=self.scale.read()
        #newWeight=100
    	objWeight=self.currentWeight-newWeight

    	
        if (debug):
            print "Object Weight is ",objWeight
            print "Because old weight was ", self.currentWeight, " & new weight is ", newWeight

        self.currentWeight=newWeight

    	if objWeight<22:
    		return ["expo_dry_erase_board_eraser","scotch_bubble_mailer","oral_b_toothbrush_green", "oral_b_toothbrush_red"]
    	elif objWeight<28:
    		return ["fiskars_scissors_red"]
    	elif objWeight<37:
    		return ["cloud_b_plush_bear","womens_knit_gloves"]
    	elif objWeight<47:
    		return ["safety_first_outlet_plugs","platinum_pets_dog_bowl"]
    	elif objWeight<55:
    		return ["kyjen_squeakin_eggs_plush_puppies"]
    	elif objWeight<60:
    		return ["cherokee_easy_tee_shirt"]
    	elif objWeight<66:
    		return ["cool_shot_glue_sticks"]
    	elif objWeight<73:
    		return ["dr_browns_bottle_brush","soft_white_lightbulb"]
    	elif objWeight<90:
    		return ["ticonderoga_12_pencils","barkely_hide_bones","laugh_out_loud_joke_book","command_hooks","jane_eyre_dvd"]
    	elif objWeight<105:
    		return ["rolodex_jumbo_pencil_cup","creativity_chenille_stems"]
    	elif objWeight<116:
    		return ["i_am_a_bunny_book"]
    	elif objWeight<125:
    		return ["dove_beauty_bar","staples_index_cards"]
    	elif objWeight<132:
    		return ["crayola_24_ct"]
    	elif objWeight<137:
    		return ["easter_turtle_sippy_cup","woods_extension_cord"]
    	elif objWeight<156:
    		return ["rawlings_baseball","clorox_utility_brush","elmers_washable_no_run_school_glue","scotch_duct_tape"]
    	elif objWeight<211:
    		return ["kleenex_tissue_box"]
    	elif objWeight<262:
    		return ["peva_shower_curtain_liner"]
    	elif objWeight<296:
    		return ["up_glucose_bottle"]
    	elif objWeight<354:
    		return ["kleenex_paper_towels"]
    	elif objWeight<402:
    		return ["folgers_classic_roast_coffee"]
    	elif objWeight<514:
    		return ["hanes_tube_socks"]
    	elif objWeight<998:
    		return ["dasani_water_bottle"]
    	else:
    		return ["fitness_gear_3lb_dumbbell"]


    def updateTote(self,objRemoved):
        if objRemoved in self.toteContents: 
            self.toteContents.remover(objRemoved)
            return True
        else:
            return False
    def jsonOutput(self, filename, shelfMap, toteContents):
        self.parser.writeOutFile(filename, self.binContents, self.toteContents)

if __name__ == "__main__":
    FILE_NAME="apc_stow_task.json"
    a=stowHandler(FILE_NAME)
    print a.pickWhichObj()

