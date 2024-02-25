import os.path

from torchvision import transforms
import json
import datetime

normalize = transforms.Compose([
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

# we use images with size 224
preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

def read_json(config_file_path):
    with open(config_file_path, "r") as config_file:
        config_data = json.load(config_file)
    return config_data


def save_json(file, config_file_path, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs('Results')
    with open(folder_name +'/'+config_file_path, "w") as config_file:
        json.dump(file, config_file, indent=4)

def generate_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%d-%m-%Y_%H-%M-%S")
    experiment_time = f"{formatted_time}"

    return experiment_time