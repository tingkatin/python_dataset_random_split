import os
import random
import shutil


def collect_class_folders(parent_dir):
    class_folders = []
    print('Collecting class folders...')
    for name in os.listdir(parent_dir):
        if name not in ignore_folders:
            class_folders.append(name)

    print(class_folders)
    return class_folders

def move_to(files, from_dir, to_dir):
    for file in files:
        shutil.move(from_dir + "/" + file, to_dir)

def collect_data_to(parent_dir, destination_dir, split_ratio):
    files = [file for file in os.listdir(parent_dir)]
    num_files = int(len(files) * split_ratio)
    selected_files = random.sample(files, num_files)

    print("Moving data to " + destination_dir + "...")
    move_to(selected_files, parent_dir, destination_dir)







if __name__ == "__main__":
    ignore_folders = [ 'train', 'test', 'validation', 'split_script.py' ]
    parent_dir = "D://DATASET//cocoa-ripeness-dataset-v3"
    train_split = 0.8
    validation_split = 0.5
    test_split = 1

    os.makedirs("./train", exist_ok=True)
    os.makedirs("./validation", exist_ok=True)
    os.makedirs("./test", exist_ok=True)

    class_folders = collect_class_folders(parent_dir)

    for class_name in class_folders:
        class_dir = parent_dir + "/" + class_name
        train_dir = parent_dir + "/train" + "/" + class_name
        validation_dir = parent_dir + "/validation" + "/" + class_name
        test_dir = parent_dir + "/test" + "/" + class_name

        dirs_to_create = [class_dir, train_dir, validation_dir, test_dir]

        for dir in dirs_to_create:
            print("Creating necessary folders...")
            os.makedirs(dir, exist_ok=True)

        collect_data_to(class_dir, train_dir, train_split)
        collect_data_to(class_dir, validation_dir, validation_split)
        collect_data_to(class_dir, test_dir, test_split)

    print("Tasks done!")


    

