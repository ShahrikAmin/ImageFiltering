# Milestone 3, P8
# Team 39
# Date of completion: Thursday, April 2, 2020
# Author of this file: Ryan Burry and Hayden Arms

# Note: Make sure to have the required files in the same folder before
# running this program. These files consist of Cimpl, simple_Cimpl_filters
# and T39_image_filters

from Cimpl import *
from T39_image_filters import *

#---------------------------MAIN CODE-------------------------------------------

def batch_interface(inputfile):
    print('Hello, Welcome to the Batch Interface')
    batch_file = open(inputfile)
    f = batch_file.readlines()
    failure_var = 0
    for line in f:
        variables = line.split(" ")
        failure_var += 1
        command_filename = variables[0]
        command_savename = variables[1]
        commands = []
        i = 2
        while i < len(variables):
            if ('\n' in variables[i]):
                newvar = variables[i].strip('\n')
                commands.append(newvar)
            else:
                commands.append(variables[i])
            i += 1
        print(commands)
        i = 0
        while i < len(commands):
            image = copy(load_image(command_filename))
            if commands[i] == '2':
                image = two_tone(image)
                print("two tone applied")
            elif commands[i] == '3':
                image = three_tone(image)
                print("three tone applied")
            elif commands[i] == 'X':
                image = extreme_contrast(image)
                print("extreme applied")
            elif commands[i] == 'T':
                image = sepia(image)
                print("sep applied")
            elif commands[i] == 'P':
                image = posterize(image)
                print("post applied")
            elif commands[i] == 'E':
                image = detect_edge(image, 10)
                print("detect applied, with threshold 10")
            elif commands[i] == 'I':
                image = detect_edges_better(image,10)
                print("better detect applied, with threshold 10")
            elif commands[i] == 'V':
                image = flip_vertical(image)
                print("vertical flip applied")
            elif commands[i] == 'H':
                image = flip_horizontal(image)
                print("horizontal flip applied")
            else:
                print('Filter unapplicable, No such command')
            i +=1
        save_as(image, command_savename)
        show(image)
        print('Done line')
    if failure_var == 0:
        print('No-image-loaded')
    print('Done File')

print('Please input the name of the batch file:')
batch_interface(input())
