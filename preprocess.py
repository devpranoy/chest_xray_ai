import pandas as pd
import os
import shutil
data =pd.read_csv("data.csv")
images = data['Image Index']
#print(images)
disease = data['Finding Labels']
directory = "/Users/pranoy/Desktop/chestxray/data/"
image_directory = "/Users/pranoy/Desktop/chestxray/images/"
def move(path_from, path_to):
    try:
        shutil.move(path_from,path_to)
    except:
        print("Image does not exist/ Error?")
def create_folder(path):
    if not os.path.exists(path):
            os.makedirs(path)

for col in range(len(disease)):
    if disease[col] == 'Pneumonia':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Atelectasis':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Cardiomegaly':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Effusion':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Infiltration':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Mass':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Nodule':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Pneumothorax':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Consolidation':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Edema':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Emphysema':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Fibrosis':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Pleural_Thickening':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'Hernia':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])
    if disease[col] == 'No Finding':
        create_folder(directory+disease[col])
        move(image_directory+images[col],directory+disease[col])