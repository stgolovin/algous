import os
import re
import json

from make_a_movie import start_script


pattern = r'^[.\/]?\/\w+\/|_\d+.jpg$'
dictionary = {}


def iterate_folder(path, dictionary):  
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            raw_names = re.split(pattern, item_path)
            for name in raw_names:
                if name:
                    if name not in dictionary:
                        dictionary[name] = [item_path]
                    else:
                        dictionary[name].append(item_path)
        elif os.path.isdir(item_path):
            iterate_folder(item_path, dictionary)


# записать словарь в JSON файл;
def burn_to_JSON(dictionary):
    with open('dictionaries.json', 'w') as f:
        json.dump(dictionary, f, indent=4)
# служебная функция для удобства подготовки файлов;
# burn_to_JSON(dictionary)


# сортируем последовательнрость
def sort_sequence(key):
    sequence = dictionary[key]
    sequence.sort()
    return sequence

pattern_2 = r'\w+$'
# обновляем имена секвенций; сортируем секвенции;
def prepare_data():
    for key in dictionary.keys():
        return sort_sequence(key)


# folder_path = './jpegs'
def start_sequence(path):
    iterate_folder(path, dictionary)
    del dictionary[".DS_Store"]
    del dictionary["sea/.DS_Store"]
    prepare_data()
    start_script(dictionary, path)