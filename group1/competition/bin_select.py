#The class that selects which bin to put items in
#  Description: Mantains a python dictionary which notes where every item is stored and quick statistics about the bins

import time
import json
from json_handler import jsonHandler
class binSelector:
    
    
    def __init__(self):
        #Create empty bin objects
        self.bin_dict={};
        #Keys are the number of the bin and the value is a list
        #The list contains a list of items, current number of items,points score, total volume, percent free, strikes, number
        self.bin_dict['bin_A']=[[],0,0,0,float(100),0,1];
        self.bin_dict['bin_B']=[[],0,0,0,float(100),0,2];
        self.bin_dict['bin_C']=[[],0,0,0,float(100),0,3];
        self.bin_dict['bin_D']=[[],0,0,0,float(100),0,4];
        self.bin_dict['bin_E']=[[],0,0,0,float(100),0,5]; 
        self.bin_dict['bin_F']=[[],0,0,0,float(100),0,6];
        self.bin_dict['bin_G']=[[],0,0,0,float(100),0,7]; 
        self.bin_dict['bin_H']=[[],0,0,0,float(100),0,8];
        self.bin_dict['bin_I']=[[],0,0,0,float(100),0,9]; 
        self.bin_dict['bin_J']=[[],0,0,0,float(100),0,10];
        self.bin_dict['bin_K']=[[],0,0,0,float(100),0,11]; 
        self.bin_dict['bin_L']=[[],0,0,0,float(100),0,12];
        self.maxbinvolume=1485 #total volume constant for each bin
        self.addItemLookup();
        
    def addtoBin(self,itemid,itembin):
        itemvol=self.item_lookup[itemid];
        binlist=self.bin_dict[str(itembin)]; #convert to temp local var 
        binlist[0].append(itemid); #add itemid to contents list
        binlist[1]=binlist[1]+1; #add item to number of items 
        binlist[3]=binlist[3]+itemvol; #add volume to total volume
        binlist[4]=100-binlist[3]*100/self.maxbinvolume; #recalculate percentage free
        self.bin_dict[str(itembin)]=binlist;
        
    def addStrike(self,itembin):
        self.bin_dict[itembin]=self.bin_dict[itembin]+1;
        
    def chooseBin(self,itemid):
        #This method selects a bin and returns that to the caller.
        itemvol=self.item_lookup[itemid];
        validlist=[];
        for key in self.bin_dict.keys():
            prediction=self.addPredict(key,itemvol);
            if prediction[3]>20: #If there is less than 10% free space in the bin don't add it to the list to be considered 
                validlist.append(prediction);
        validlist.sort(cmp=self.comparator);
        return validlist[0][5]

    
    def comparator(self, a,b):
        #Comparator for the bin sort module
        if b[4]-a[4]!=0: #Compare strikes
            return b[4]-a[4];
        if b[2]-a[2]!=0: #Compare score
            return b[2]-a[2];
        if b[3]-a[3]!=0: #Compare freedom
            return b[3]-a[3];
        if b[1]-a[1]!=0: #compare number of elements 
            return a[1]-b[1];
        return 0
        
    def addPredict(self,itembin,itemvol):
        #Predicts the free space in a bin after a particular item is added to a specified bin. Returns total volume and percentage free 
        estnumel=self.bin_dict[itembin][1]+1;#number of elements after addition
        points=self.bin_dict[itembin][2];#points level (higher is better)
        estvol=self.bin_dict[itembin][3]+itemvol;
        estpf=100-estvol*100/self.maxbinvolume;
        strikes=self.bin_dict[itembin][5]; #gets strikes
        num=self.bin_dict[itembin][6]; #Gets number since supervisor is stupid and takes numbers
        return itembin, estnumel, points, estpf,strikes,num

    def start(self):
        #copy the value of Calculate score of each bin and write it to position 2
        for key in self.bin_dict.keys():
            orgnum=self.bin_dict[key][1];
            if orgnum>=5:
                self.bin_dict[key][2]=20;
                continue;
            elif orgnum>=3 and orgnum<5:
                self.bin_dict[key][2]=15;
                continue;
            elif orgnum>=1 and orgnum<3:
                self.bin_dict[key][2]=10;
                continue;
            self.bin_dict[key][2]=0
        print("Bin Selector has been intialized")
            
    def printBin(self):
        for key in self.bin_dict.keys():
            binlist=self.bin_dict[key];
            print ("bin ",key," contains ",binlist[0]," w/ ",binlist[1]," items ",binlist[4],"% free for ",binlist[2],"points with ",binlist[5]," strikes");

    def initialize(self,filename):
        jH=jsonHandler()
        binlist=jH.readInFile(filename)[0];
        for key in binlist:
            for item in binlist[key]:
                self.addtoBin(item,key)
        self.start();

    def addItemLookup(self):
        self.item_lookup={};
        self.item_lookup["i_am_a_bunny_hardcover_book"]=7*8*1;
        self.item_lookup["laugh_out_loud_jokes_for_kids_paperback_book"]=7*4.5*1;
        self.item_lookup["scotch_bubble_mailer"]=1*10*12;
        self.item_lookup["up_and_up_glucose_tablets"]=3*3*6;
        self.item_lookup["dasani_water_bottle"]=3*3*8;
        self.item_lookup["rawlings_recreational_use_baseball"]=3.5*3.5*3.5;
        self.item_lookup["folgers_classic_roast_coffee"]=4*4*5.5;
        self.item_lookup["elmers_glue_all"]=3*1*6;
        self.item_lookup["hanes_tube_socks"]=8*10*4;
        self.item_lookup["womens_knit_gloves"]=4*1*7;#Permeable Object
        self.item_lookup["cherokee_easy_tee_t_shirt"]=20;#Permeable object
        self.item_lookup["peva_shower_curtain_liner"]=1*6.5*11; 
        self.item_lookup["cloud_b_plush_bear"]=6.5*3*2;
        self.item_lookup["boots_and_barkley_beefhide_bones"]=7*5*2;
        self.item_lookup["plush_puppies_squeakin_eggs"]=3*6*7;
        self.item_lookup["cool_shot_mini_glue_sticks"]=1*3*6;
        self.item_lookup["creativity_street_chenille_stems_100_count"]=1.5*4*14.5;
        self.item_lookup["40w_soft_white_lightbulb"]=2.5*2.5*5;
        self.item_lookup["safety_1st_ultra_clear_outlet_plugs"]=4*2*8;
        self.item_lookup["oral_b_cavity_defense_toothbrush"]=1*1*8;
        self.item_lookup["dr_browns_natural_flow_bottle_brush"]=5*3*12;
        self.item_lookup["command_hooks"]=2*5*7;
        self.item_lookup["easter_turtle_figural_sippy_cup"]=6*3*7;
        self.item_lookup["fiskars_scissors_5inch_blunt_tip_red"]=1*3.5*7;
        self.item_lookup["scotch_cloth_duct_tape"]=4*4*2;
        self.item_lookup["woods_6ft_extension_cord"]=1.5*3*7;
        self.item_lookup["platinum_pets_dog_bowl"]=5*5*2;
        self.item_lookup["fitness_gear_3lb_neoprene_dumbbell"]=3*3*6;
        self.item_lookup["rolodex_wire_mesh_jumbo_pencil_holder"]=4.5*4.5*5.5;
        self.item_lookup["clorox_utility_brush"]=3*4*8;
        self.item_lookup["kleenex_viva_paper_towels"]=5*5*2;
        self.item_lookup["expo_white_board_care_eraser"]=1*5*12;
        self.item_lookup["kleenex_cool_touch_tissue_box"]=4.5*4.5*5;
        self.item_lookup["ticonderoga_#2_pencils_12_count"]=1*4*8;
        self.item_lookup["crayola_crayons"]=3*1*4;
        self.item_lookup["jane_eyre_dvd"]=1*5*7.5;
        self.item_lookup["dove_dry_oil_beauty_bar"]=4*0.5*2.5;
        self.item_lookup["staples_3x5_ruled_index_cards"]=1*3*5;
        
