# How to Use the Video Duration Classifier Script

This document provides step-by-step instructions on how to use the "Video Duration Classifier" script. This Python script allows you to classify video files in a folder based on their duration, moving them to either a "videos_longer_than_60" folder or a "videos_less_than_60" folder.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed:

1. **Python**: The script is written in Python. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **FFmpeg**: FFmpeg is required for video duration analysis. You can download it from the official website: [FFmpeg](https://www.ffmpeg.org/download.html).

## Usage

Follow these steps to use the "Video Duration Classifier" script:

1. **Download the Script**: Download the script (or create a Python file) containing the code you provided.

2. **Install FFmpeg**: Ensure FFmpeg is installed on your system. You can check if FFmpeg is installed by opening a terminal or command prompt and running:

   ```bash
   ffmpeg -version
   ```

   If FFmpeg is not installed, follow the instructions on the [FFmpeg download page](https://www.ffmpeg.org/download.html) to install it.

3. **Run the Script**:

   - Open a terminal or command prompt.

   - Navigate to the directory where you saved the script using the `cd` command. For example:

     ```bash
     cd /path/to/script/directory
     ```

   - Run the script by executing the following command:

     ```bash
     python script.py
     ```

4. **Enter the Folder Path**:

   - The script will prompt you to enter the folder path where your video files are located. Provide the full path to the folder containing your video files.

5. **Script Execution**:

   - The script will start processing the video files in the specified folder and its subfolders.

   - It will print the path of each video file as it processes them.

   - Videos longer than or equal to 60 seconds will be moved to the "videos_longer_than_60" folder, and videos shorter than 60 seconds will be moved to the "videos_less_than_60" folder. These folders will be created in the same directory where the script is located.

6. **View the Results**:

   - After the script finishes, you can find the classified video files in the "videos_longer_than_60" and "videos_less_than_60" folders.

## Example

Suppose you have a folder named "videos" containing various video files. After running the script and providing the folder path, the classified videos will be moved to the "videos_longer_than_60" and "videos_less_than_60" folders accordingly.

## License

This script is open-source and available under the MIT License. You can find the license details in the script's source code or by referring to the included license file.

Now you are ready to use the "Video Duration Classifier" script to classify your video files based on their duration.
