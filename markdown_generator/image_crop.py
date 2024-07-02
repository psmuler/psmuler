from PIL import Image

def crop_image(image_path, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    width, height = image_obj.size
    h = min(3/5*width,height)
    w = 5/3*h
    cropped_image = image_obj.crop((width/2-w/2, height/2-h/2, width/2+w/2, height/2+h/2))
    cropped_image.resize((500, 300)).save(saved_location)
    cropped_image.show()

crop_image('images/image.png', 'images/cropped_image.png')