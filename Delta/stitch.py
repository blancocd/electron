import numpy as np
import cv2
import os
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 1 and len(sys.argv) != 2 and len(sys.argv) != 3):
        print("usage:")
        print("python3 ./stitch.py \nuses default configuration: 3 columns and 'stitched' as the output directory \n")
        print("otherwise specify these options as follows or only do columns")
        print("python3 ./stitch.py #columns output_directory")

    cols = 3
    output_dir = "stitched"
    if len(sys.argv) > 1:
        cols = int(sys.argv[1])
    if len(sys.argv) == 3:
        output_dir = sys.argv[2]

    # Use the next two lines to include all directories in current directory
    dirs = list(filter(os.path.isdir, os.listdir()))
    img_dirs = [dirc for dirc in dirs if dirc != output_dir]

    # Useful lists
    # img_dirs = ['frames_log_Te_Sharma_poloidal', 'frames_log_Te_Kawazura_22_poloidal', 'frames_log_Te_Werner_poloidal', 'frames_log_Te_Rowan_poloidal', 'frames_log_Te_Kawazura_18_poloidal', 'frames_log_Te_Howes_poloidal']
    # img_dirs = ['frames_log_Te_Rowan_poloidal', 'frames_log_sigma_w_poloidal', 'frames_log_Thetae_Rowan_poloidal']
    # img_dirs = ['frames_log_Thetae_Sharma_poloidal', 'frames_log_Thetae_Kawazura_22_poloidal', 'frames_log_Thetae_Werner_poloidal', 'frames_log_Thetae_Rowan_poloidal', 'frames_log_Thetae_Kawazura_18_poloidal', 'frames_log_Thetae_Howes_poloidal']

    rows = np.ceil(len(img_dirs)/cols).astype(int)

    list_files = os.listdir(img_dirs[0])
    list_files.sort()

    full_path = os.path.join(img_dirs[0], list_files[0])
    img = cv2.imread(full_path)
    in_shape = img.shape
    out_shape = (in_shape[0]*rows, in_shape[1]*cols, 3)
    
    for filename in list_files:
        output_image = np.zeros(out_shape)
        count = 0
        for directory in img_dirs:
            row = count//cols
            col = count%cols
            full_path = os.path.join(directory, filename)
            img = cv2.imread(full_path)
            output_image[in_shape[0]*row:in_shape[0]*(row+1), in_shape[1]*col:in_shape[1]*(col+1)] = img
            output_file = os.path.join(output_dir, filename)
            cv2.imwrite(output_file, output_image)
            count = count + 1

# ffmpeg -pattern_type glob -i '*.png' -framerate 30 -s 1800x1200 -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p thels.mp4