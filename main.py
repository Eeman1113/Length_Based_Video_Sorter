#___________________________________________________________________________________________________________________________________
import os
import glob
import shutil
import subprocess
import json
#___________________________________________________________________________________________________________________________________
def checkduration(path):
    out = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", path])
    ffprobe_data = json.loads(out)
    duration_seconds = float(ffprobe_data["format"]["duration"])*0.0166667
    return duration_seconds
#___________________________________________________________________________________________________________________________________
def find_mp4_files(folder_path):
    mp4_files = []
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return mp4_files
#___________________________________________________________________________________________________________________________________
    # Use glob to find all .mp4 files in the folder and its subfolders
    search_pattern = os.path.join(folder_path, '**/*.mp4')
    mp4_files.extend(glob.glob(search_pattern, recursive=True))

    return mp4_files
#___________________________________________________________________________________________________________________________________
user_folder_path = input("Enter the folder path: ")
mp4_files_list = find_mp4_files(user_folder_path)

for i in range(0,len(mp4_files_list)):
    print(mp4_files_list[i])
    if checkduration(mp4_files_list[i])>=60:
        os.rename(f"{mp4_files_list[i]}", f"./videos_longer_than_60/{mp4_files_list[i].split('/')[-1]}")
        # os.replace(f"{mp4_files_list[i]}", f"./videos_longer_than_60/{mp4_files_list[i].split('/')[-1]}")
        # shutil.move((f"{mp4_files_list[i]}", f"./videos_longer_than_60/{mp4_files_list[i].split('/')[-1]}"))
    elif checkduration(mp4_files_list[i])<=60:
        os.rename(f"{mp4_files_list[i]}", f"./videos_less_than_60/{mp4_files_list[i].split('/')[-1]}")
        # os.replace(f"{mp4_files_list[i]}", f"./videos_less_than_60/{mp4_files_list[i].split('/')[-1]}")
        # shutil.move(f"{mp4_files_list[i]}", f"./videos_less_than_60/{mp4_files_list[i].split('/')[-1]}")
#___________________________________________________________________________________________________________________________________