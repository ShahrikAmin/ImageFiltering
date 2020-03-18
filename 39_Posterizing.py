from Cimpl import * 

image = load_image(choose_file())

def posterize(image):
    """ (Cimpl.Image) -> None
    
        Posterizes the specified image, modifying all RGB 
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

def _adjust_component(color):
    """ Takes a specified r g b and returns
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
    
posterized_image = posterize(image)
show(posterized_image) # Shows the posterized image
