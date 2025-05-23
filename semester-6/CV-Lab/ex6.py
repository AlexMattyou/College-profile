import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load stereo images from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
left_img_path = os.path.join(script_dir, "in1.png")  # Left image
right_img_path = os.path.join(script_dir, "in2.png")  # Right image

# Load images in grayscale
left_img = cv2.imread(left_img_path, cv2.IMREAD_GRAYSCALE)
right_img = cv2.imread(right_img_path, cv2.IMREAD_GRAYSCALE)

# Check if images loaded correctly
if left_img is None or right_img is None:
    print("Error: Could not load one or both images!")
    print(f"Looking for: {left_img_path} and {right_img_path}")
    exit()

# Ensure both images have the same size
height = min(left_img.shape[0], right_img.shape[0])
width = min(left_img.shape[1], right_img.shape[1])
left_img = cv2.resize(left_img, (width, height))
right_img = cv2.resize(right_img, (width, height))

# Create StereoBM object with optimized parameters
stereo = cv2.StereoBM_create(numDisparities=64, blockSize=15)

# Compute the disparity map (depth map)
disparity = stereo.compute(left_img, right_img)

# Normalize for visualization
disparity_norm = cv2.normalize(
    disparity, None, 
    alpha=0, 
    beta=255,
    norm_type=cv2.NORM_MINMAX
)
disparity_norm = np.uint8(disparity_norm)

# Apply colormap for better visualization
disparity_colored = cv2.applyColorMap(disparity_norm, cv2.COLORMAP_JET)

# Display the results
plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
plt.imshow(left_img, cmap='gray')
plt.title("Left Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(right_img, cmap='gray')
plt.title("Right Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(disparity_colored)
plt.title("Depth Map (Disparity)")
plt.axis("off")
plt.colorbar(label="Depth Level")

plt.tight_layout()
plt.show()