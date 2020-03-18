from Cimpl import * 

image = load_image(choose_file())

black = create_color(0, 0, 0) # Creates the black color
white = create_color(255, 255, 255) # Creates the white color
gray = create_color(128, 128, 128) # Creates the gray color

def two_tone(image):
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to a black-and-white
    (two-shade) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)   
    
    """

    new_image = copy(image)    
    
    for (x, y, (r, g, b)) in image:
        
        brightness = (r + g + b) / 3
        
        if 0 <= brightness <= 127:
            set_color(new_image, x, y, black)
        else:  
            set_color(new_image, x, y, white)
    
    return new_image

def three_tone(image):
    """ (Cimpl.Image) -> Image
    
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)   
    
    """

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

two_toned_image = two_tone(image)
show(two_toned_image) # Shows the two_toned_image

three_toned_image = three_tone(image)
show(three_toned_image) # Shows the three_toned_image
