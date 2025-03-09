import cv2
import numpy as np
import os


def image_to_sketch(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Bilateral filter to smooth but keep edges
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # Adaptive Threshold instead of Canny
    sketch = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 3
    )

    # Reduce noise using median blur
    # gray = cv2.medianBlur(gray, 5)

    # Apply canny edge detection
    # edges = cv2.Canny(gray, threshold1=30, threshold2=100)

    # Dilate the edges to make them bolder
    # kernel = np.ones((2, 2), np.uint8)
    # edges = cv2.dilate(edges, kernel, iterations=2)

    # Invert the edges image
    # sketch = cv2.bitwise_not(edges)

    # Invert the grayscale image
    # inverted = 255 - gray
    # inverted = cv2.bitwise_not(gray)

    # Apply Gaussian blur to the inverted image
    # blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)
    # blurred = cv2.GaussianBlur(inverted, (21, 21), 10)

    # Invert the blurred image
    # inverted_blurred = 255 - blurred
    # inverted_blurred = cv2.bitwise_not(blurred)

    # Create the pencil sketch using the dodge blend technique
    # sketch = cv2.divide(gray, inverted_blurred, scale=255.0)

    # Improve the contrast of the sketch with adaptive thresholding
    # sketch = cv2.adaptiveThreshold(
    #     sketch, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2
    # )

    # Save the result
    cv2.imwrite(output_path, sketch)
    print(f"Sketch saved to {output_path}")


# Example usage
image_path = "image.jpg"  # Input image path
output_path = "sketch.jpg"  # Output sketch path
# print("File exists:", os.path.exists(image_path))
# print("Files in script directory:", os.listdir(os.path.dirname(__file__)))
# print("Current Working Directory:", os.getcwd())
image_to_sketch(image_path, output_path)
