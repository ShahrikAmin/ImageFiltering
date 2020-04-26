# Milestone 3, P8
# Team 39
# Date of completion: Thursday, April 2, 2020
# Author of this file: Shahrik Amin and Sathvik Villuri 

# Note: Make sure to have the required files in the same folder before
# running this program. These files consist of Cimpl, simple_Cimpl_filters
# and T39_image_filters

from Cimpl import *
from T39_image_filters import *

#---------------------------MAIN CODE-------------------------------------------

def user_interface():
    
    userinput = None
    image = None 
    
    while userinput != "Q":
        print("L)oad image S)ave as \n 2)-tone 3)-tone X)treme contrast \
T)int sepia P)osterize \n E)dge detect I)mproved edge detect \
V)ertical flip H)orizontal flip \n Q)uit \n")
    
        userinput = input(":").upper()
    
        if userinput == "L":
            file = choose_file()
            image = load_image(file)
        elif image == None: 
            print("No image loaded. Please load an image before entering a command.\n")
            continue
        elif userinput =="S":
            filename = input("Please enter a filename to save as:")
            save_as(image, filename)            
        elif userinput == "2":
            image = two_tone(image, "black", "white")
        elif userinput == "3":
            image = three_tone(image, "black", "white", "grey")
        elif userinput == "X":
            image = extreme_contrast(image)
        elif userinput == "T":
            image = sepia(image)
        elif userinput == "P":
            image = posterize(image)
        elif userinput == "E":
            image = detect_edge(image, 10)
        elif userinput == "I":
            image = detect_edges_better(image, 10)
        elif userinput == "V":
            image = flip_vertical(image)
        elif userinput == "H":
            image = flip_horizontal(image)
        elif userinput == "Q":
            return
        else: 
            print("No such command\n")
            continue
        
        show(image)
        
user_interface()
