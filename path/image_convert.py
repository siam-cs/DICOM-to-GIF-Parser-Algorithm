import os
import pydicom
import numpy as np
import imageio

# Path to the root folder containing the input directories
input_folder = "C:/Users/user/Desktop/CC"

# Path to the root folder where the output directories and GIF files will be saved
output_folder = "C:/Users/user/Desktop/output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the directories in the input folder
for root, dirs, files in os.walk(input_folder):
    # Create the corresponding output directory
    output_dir = os.path.join(output_folder, os.path.relpath(root, input_folder))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all the files in the current directory
    for filename in files:
        if filename.endswith(".dcm"):
            # Load the DICOM file into memory
            ds = pydicom.dcmread(os.path.join(root, filename))

            # Convert the pixel values to uint8
            pixel_array = ds.pixel_array.astype(np.float32)
            pixel_array -= pixel_array.min()
            pixel_array /= pixel_array.max() / 255.0
            pixel_array = pixel_array.astype(np.uint8)

            # Generate the output filename
            output_filename = os.path.splitext(filename)[0] + ".gif"
            output_path = os.path.join(output_dir, output_filename)

            # Save the DICOM file as a GIF file
            imageio.imwrite(output_path, pixel_array)