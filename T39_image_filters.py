# Milestone 3, P8
# Team 39
# Date of submission: Thursday, April 2, 2020

# Authors: Shahrik Amin 10115583, Hayden Arms 101143346,
#          Ryan Burry 101155625, Sathvik Villuri 101171739


from Cimpl import *
from simple_Cimpl_filters import grayscale

#---------------------------MAIN CODE-------------------------------------------

def red_channel(image):
    """ (Cimpl.Image) -> Image
    
    Returns and adds a red filter on top of the specified
    image.
    
    >>> red_channel(image)
    >>> new_image = copy(image)
    >>> set_color(new_image, x, y, red_colour)
    >>> show(new_image)
    """
    new_image = copy(image)
    
    for (x, y, (r, g, b)) in image:
        red_colour = create_color(r,0,0)
        set_color(new_image, x, y, red_colour)
    
    return new_image

def green_channel(image):
    """ (Cimpl.Image) -> Image
    
    Returns and adds a green filter on top of the specified
    image.
        
    >>> green_channel(image)
    >>> new_image = copy(image)
    >>> set_color(new_image, x, y, green_colour)
    >>> show(new_image)
    """
    new_image = copy(image)
    
    for (x, y, (r, g, b)) in image:
        green_colour = create_color(0,g,0)
        set_color(new_image, x, y, green_colour)
    
    return new_image 

def blue_channel(image):
    """ (Cimpl.Image) -> Image
    
    Returns and adds a blue filter on top of the specified
    image.
    
    >>> blue_channel(image)
    >>> new_image = copy(image)
    >>> set_color(new_image, x, y, blue_colour)
    >>> show(new_image)
    """
    new_image = copy(image)
    
    for (x, y, (r, g, b)) in image:
        blue_colour = create_color(0,0,b)
        set_color(new_image, x, y, blue_colour)
    
    return new_image


def combine(image_red, image_green, image_blue):
    ''' (Cimpl.Image) -> Image
    
    Returns an image which combines the three colour components of three other
    images, it takes a red, green and blue image and combines them to create a
    full colour image.
   
    No examples can be provided as it returns an image not a numericalvalue or
    a boolean
    '''
    
    combined = create_image((get_width(image_red)), (get_height(image_red))) #creates blank image to work with
    
    for x, y, (r, g, b) in combined:
        redcolour = get_color(image_red,x,y) #gets the red, green, and blue colours from the respective image for each position of the image
        greencolour = get_color(image_green,x,y)
        bluecolour = get_color(image_blue,x,y)
        combo_colour = create_color(redcolour[0], greencolour[1], bluecolour[2]) #creates a combination of all three components at each point
        set_color(combined, x, y, combo_colour) #sets the colour at that point to the combo colour
        
    return combined   


def posterize(image):
    """ (Cimpl.Image) -> Image
    
    Posterizes and returns the specified image, modifying all RGB 
    values based on to it's midpoint value for the 
    quadrant it belongs in.
        
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image)     
        
    """
    
    new_image = copy(image)    
    
    for (x, y, (r, g, b)) in image:
        posterized_color = create_color(_adjust_component(r),_adjust_component(g),_adjust_component(b))
        set_color(new_image, x, y, posterized_color)
    
    return new_image

# Function below for posterize() function
def _adjust_component(color):
    """ (Cimpl.Image) -> Image
    
    Takes a specified r g b and returns
    it's midpoint color of that quadrant.
        
    >>> adjust_image(30)
    31
    >>> adjust_image(100)
    95
    >>> adjust_image(150)
    159
    >>> adjust_image(229)
    223
    
    """

    if 0 <= color <= 63:
        color = 31
    elif 64 <= color <= 127:
        color = 95
    elif 128 <= color <= 191:
        color = 159
    elif 192 <= color <= 255:
        color = 223
    
    return color


def two_tone(image, black, white):
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to a black-and-white
    (two-shade) image and returns it.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)   
    
    """
    
    black = create_color(0, 0, 0) # creates the black color
    white = create_color(255, 255, 255) # creates the white color
    gray = create_color(128, 128, 128) # creates the gray color    

    new_image = copy(image)    
    
    for (x, y, (r, g, b)) in image:
        
        brightness = (r + g + b) / 3
        
        if 0 <= brightness <= 127:
            set_color(new_image, x, y, black)
        else:  
            set_color(new_image, x, y, white)
    
    return new_image


def three_tone(image, black, white, gray):
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image and converts it.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)   
    
    """
    
    black = create_color(0, 0, 0) # creates the black color
    white = create_color(255, 255, 255) # creates the white color
    gray = create_color(128, 128, 128) # creates the gray color    
    
    new_image = copy(image)    
    
    for (x, y, (r, g, b)) in image:
        
        brightness = (r + g + b) / 3
        
        if 0 <= brightness <= 84:
            set_color(new_image, x, y, black)
        elif 85 <= brightness <= 170: 
            set_color(new_image, x, y, white)
        else:                  
            set_color(new_image, x, y, gray)
    
    return new_image


def sepia(image):
    """ (Cimpl.Image) -> Image
    
    Filters out all the red and green values of the image and returns only the 
    blue.
    
    >>> image = load_image(choose_file()) 
    >>> sepia(image)
    >>> show(image) 
 
    """
 
    new_image = grayscale(image)
 
    for pixel in new_image:
        x, y, (r, g, b) = pixel 
        if (r < 63 and b < 63):
   
            darkgray = create_color(r*1.1, g, b*0.9)
            set_color(new_image, x, y, darkgray)
        elif (63<= r <= 191 and 63 <= b <= 191):
            medgray = create_color(r*1.15, g, b*0.85)
            set_color(new_image, x, y, medgray)
        elif (r > 191 and b > 191):
            lightgray = create_color(r*1.08, g, b*0.93)
            set_color(new_image, x, y, lightgray)
    
    return new_image


def extreme_contrast(mod_image):
    ''' (Cimpl.Image) -> Image
    
    Returns an image with the extreme lowest or extreme highest 
    value for each pixel dependant on whether the pixel had a value higher 
    than 128 or lower. Pushing each colour to its extreme value.
    
    >>> image = load_image(choose_file()) 
    >>> extreme_contrast(image)
    >>> show(image) 
    '''
    for x, y, (r, g, b) in mod_image:
        if r < 128: #for low red values
            r = 0
        else:       # for high red values
            r = 255
        if g < 128: # for low green values
            g = 0
        else:       # for high green values
            g = 255
        if b < 128: #for low blue values
            b = 0
        else:       #for high blue values
            b = 255
        contrast_colour = create_color(r, g, b) #creates a combination of all three components at each point
        set_color(mod_image, x, y, contrast_colour) #sets the colour at that point to the contrast colour 
    return mod_image    


def flip_vertical(image):
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to vertically flipped 
    copy of that image.
    
    >>> image = load_image(choose_file()) 
    >>> flip_vertical(image)
    >>> show(image)   
    
    """
    
    new_image = copy(image)
    temp_image = copy(image)
    WIDTH = get_width(image) - 1
    
    for x, y, color in temp_image:
        set_color(new_image, WIDTH-x, y, color)
        
    return new_image

def flip_horizontal(image):
    """ (Cimpl.Image) -> Image
    
    Takes an image and returns the flipped version of that image
    along a horizontal line.
    
    >>> image = load_image(choose_file()) 
    >>> flip_horizontal(image)
    >>> show(image) 
    
    """
    
    new_image = copy(image)
    temp_image = copy(image)
    HEIGHT = get_height(image) - 1
    
    for x,y, color in temp_image:
        set_color(new_image,x,HEIGHT-y,color)
        
    return new_image


def detect_edge(pass_image,threshold):
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to an image with changed
    pixels' colors to black and white.
    
    >>> image = load_image(choose_file()) 
    >>> detect_edge(image)
    >>> show(image) 
    
    """
    
    image_height =  get_height(pass_image)   #gets height and width and sets them to variables
    image_width = get_width(pass_image)
    loop_variable = 0
    
    for x,y,(r,g,b) in pass_image:
        col_average_top =  (r + g + b) /  3     #gets average of the colour
        if (y + 1 < image_height) and (x + 1 <= image_width):    #staying within image borders
            col_und = get_color(pass_image,x,y+1)  #get the colour below it
            col_average_und = (col_und[0] + col_und[1] + col_und[2]) / 3    #average the colour below it
            cont_compare = abs(col_average_top - col_average_und)   #compare the colours brightness
            if cont_compare > threshold:    # if its greater than threshold set top to black
                pix_col = create_color(0,0,0)   #makes black colour
                set_color(pass_image,x,y,pix_col)    #sets it to  black
            elif cont_compare < threshold:  #if its less than threshold set top to white
                pix_col = create_color(255,255,255)     #makes white colour
                set_color(pass_image,x,y,pix_col)    #sets it to white
            else:
                pix_col = create_color(0,0,0)   #if theyre the same colour, set to black anyway
                set_color(pass_image,x,y,pix_col)
        if (x == image_width) and (y == image_height):  #once the image reaches the border, as x and y in for loop will, return the image
            loop_varible += 1
    while loop_variable != 1:
        return pass_image


def detect_edges_better(image: Image, threshold: int) -> Image:
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to an image with changed
    pixels' colors to black and white, improved version
    of the detect_edges filter.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image) 
    
    """
    new_image = image

    for x,y, col in image:
        maxy = y
        maxx = x

    for x,y, (r,g,b) in image:

        brightness = (r + g + b) // 3
        
        if y + 1 < maxy:
            (r1, g1, b1) = get_color(image, x, y+1)
        else:
            (r1, g1, b1) = (r, g, b)
        if x + 1 <= maxx:
            (r2, g2, b2) = get_color(image, x+1, y)
        else:
            (r2, g2, b2) = (r, g, b)
            
        below_brightness = (r1 + g1 + b1) // 3
        right_brightness = (r2 + g2 + b2) // 3
        below_contrast = abs(brightness - below_brightness)
        right_contrast = abs(brightness - right_brightness)
        
        if  threshold <= below_contrast and right_contrast:
            pixel_color = create_color(0, 0, 0)
        else:
            pixel_color = create_color(255, 255, 255)
            
        set_color(new_image, x, y, pixel_color)

    return new_image
