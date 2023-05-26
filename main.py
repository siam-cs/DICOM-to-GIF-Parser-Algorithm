import os
import pydicom
import numpy as np
import imageio

# Path to the folder containing DICOM files
input_folder = "C:\Users\user\Desktop\CC\LIDC-IDRI-1011\01-01-2000-NA-CT THORAX WCONTRAST-94040\2.000000-CHEST-06815"

# Path to the folder where the GIF files will be saved
output_folder = "C:/Users/user/Desktop/CC/image convert/06815"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the DICOM files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".dcm"):
        # Load the DICOM file into memory
        ds = pydicom.dcmread(os.path.join(input_folder, filename))

        # Convert the pixel values to uint8
        pixel_array = ds.pixel_array.astype(np.float32)
        pixel_array -= pixel_array.min()
        pixel_array /= pixel_array.max() / 255.0
        pixel_array = pixel_array.astype(np.uint8)

        # Generate the output filename
        output_filename = os.path.splitext(filename)[0] + ".gif"
        output_path = os.path.join(output_folder, output_filename)

        # Save the DICOM file as a GIF file
        imageio.imwrite(output_path, pixel_array)
