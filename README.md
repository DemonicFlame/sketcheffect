# Sketch Effect

This project converts an image into a sketch-like effect using OpenCV.

## Features
- Converts images into a black-and-white pencil sketch.
- Uses adaptive thresholding for better edge detection.
- Works well for various image types.

## Requirements
Make sure you have the following installed:

- Python 3.x
- OpenCV
- NumPy

Install dependencies using:
```sh
pip install opencv-python numpy
```

## Usage
1. Place the image you want to convert in the project directory.
2. Replace the image path in the script with the name and file type of your image.
3. Set the name and file type of the output image in the output path.
4. Run the script:
   ```sh
   python sketchmaker.py
   ```
5. The output image will be saved in the same directory.

   
## Customization
- Adjust the `cv2.adaptiveThreshold()` parameters for different effects.
- Experiment with Gaussian blur or bilateral filtering for smoother results.

