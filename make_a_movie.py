import os
import re
import shutil


pattern = r'\w+$'
array_of_folders = []
def preassembling_video(dictionary):
    for key, values in dictionary.items():
        result = re.search(pattern, key)
        new_key = result.group(0)
        array_of_folders.append(new_key)
        folder = f'{new_key}'
        if not os.path.exists(folder):
                os.mkdir(folder)
        for photo in values:
            shutil.copy(photo, folder)
        

def assemble_video():
    for item in array_of_folders:
        command = (
            f"ffmpeg -f image2 -pattern_type glob -framerate 24 -i './{item}/*.jpg' -c:v mjpeg {item}.mov"
            )
        os.system(command)


def move_video(path):
    for item in array_of_folders:     
        source_file = f'{item}.mov'
        destination_directory = path
        shutil.move(source_file, destination_directory)


def remove_unnecessary_folders():  
    for item in array_of_folders:   
        directory_to_delete = f'./{item}'
        shutil.rmtree(directory_to_delete)


def start_script(dictionary, path):
     preassembling_video(dictionary)
     assemble_video()
     move_video(path)
     remove_unnecessary_folders()
     