import subprocess
import os
import keyboard

def find_folder(path, folder_name):
    for root, dirs, files in os.walk(path):
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None

def run_cmd_command(command):
    subprocess.call(command, shell=True)

# Replace 'path_to_search' with the root directory where you want to search for the folder
path_to_search = 'C:\\'
# Replace 'folder_to_find' with the name of the folder you want to find
folder_to_find = 'EcoNet_Edge'

folder_path = find_folder(path_to_search, folder_to_find)

if folder_path is not None:
    print("Press F9 to continue...")
    keyboard.wait('F9')
    openwsl = "wsl"
    change_dir_command = f"cd /d {folder_path} && "
    docker_commands = "docker-compose up && docker-compose build"
    run_cmd_command(openwsl + change_dir_command + docker_commands)
else:
    print(f"Folder not found: {folder_to_find}")
