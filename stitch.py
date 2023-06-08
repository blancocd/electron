import numpy as np
import cv2
import os
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 1 and len(sys.argv) != 2 and len(sys.argv) != 3):
        print("stitches together images with the same filename but in all the different directories at current directory")
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

    # A list of strings which are the directories in this directory
    # Should change this to explicitly putting the directories you want if don't want to stitch the images from all directories
    dirs = list(filter(os.path.isdir, os.listdir()))
    img_dirs = [dirc for dirc in dirs if dirc != output_dir]
    rows = np.ceil(len(img_dirs)/cols).astype(int)

    # Assumes all the directories have the same number of images with the same name
    list_files = os.listdir(img_dirs[0])
    list_files.sort()

    # Also assumes that all the images have the same shape/size/resolution
    full_path = os.path.join(img_dirs[0], list_files[0])
    img = cv2.imread(full_path)
    in_shape = img.shape
    out_shape = (in_shape[0]*rows, in_shape[1]*cols, 3)

    # Iterate over same image number across all directories
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