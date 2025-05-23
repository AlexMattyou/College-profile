import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the image with proper path handling
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "test.jpg")  # Using test.jpg as per your request
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image not found at {image_path}!")

# Convert to different color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Histogram Equalization (only on grayscale)
hist_eq = cv2.equalizeHist(gray)

# Convolution (Sharpening)
kernel = np.array([[0, -1, 0], 
                   [-1, 5, -1], 
                   [0, -1, 0]])  # Sharpening kernel
sharpened = cv2.filter2D(image, -1, kernel)

# Image Smoothing (Blurring)
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
median_blur = cv2.medianBlur(image, 5)

# Compute Gradients (Sobel Operator)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)  # Convert to 8-bit

# Edge Detection using Canny
edges = cv2.Canny(gray, 100, 200)

# Display all processed images
titles = [
    "Original", "Grayscale", "HSV", "LAB", "Histogram Equalized",
    "Sharpened", "Gaussian Blur", "Median Blur", 
    "Sobel Gradient", "Canny Edge Detection"
]

images = [
    image, gray, hsv, lab, hist_eq, 
    sharpened, gaussian_blur, median_blur,
    sobel_combined, edges
]

# Create subplots with proper layout
fig, axs = plt.subplots(2, 5, figsize=(20, 10))
for i, ax in enumerate(axs.flat):
    if len(images[i].shape) == 2:  # Grayscale images
        ax.imshow(images[i], cmap="gray")
    else:  # Color images
        # Convert BGR to RGB for proper display
        if images[i].shape[2] == 3:  # Regular color image
            ax.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        elif images[i].shape[2] == 4:  # Image with alpha channel
            ax.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGRA2RGBA))
    
    ax.set_title(titles[i])
    ax.axis("off")

plt.tight_layout()
plt.show()