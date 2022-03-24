import os
from datetime import datetime

def retrieve_images_files_times(path):
    image_dict={}

    for file in os.listdir(path):
        fullpath=os.path.join(path, file)
        if os.path.isfile(fullpath):
            image_dict.update({datetime.fromtimestamp(os.path.getctime(fullpath)): file})

    return image_dict

def search_for_new_image(path):
    # Get dict of images-times
    image_dict = retrieve_images_files_times(path)

    # Get last image:
    last_time = max(image_dict.keys())

    return image_dict[last_time]