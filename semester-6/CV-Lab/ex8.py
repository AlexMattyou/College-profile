import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the image with proper path handling
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "arima.jpg")  # Change to your image filename
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    print(f"Looking for image at: {image_path}")
    exit()

# Convert to RGB for display purposes (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create an initial mask where everything is marked as probable background
mask = np.full(image.shape[:2], cv2.GC_PR_BGD, dtype=np.uint8)

# Define regions of interest
height, width = image.shape[:2]

# Define sure foreground (center region)
mask[height//4:3*height//4, width//4:3*width//4] = cv2.GC_FGD

# Define sure background (edges)
border_size = 8  # Adjust this value for different border thickness
mask[:height//border_size, :] = cv2.GC_BGD          # Top edge
mask[-height//border_size:, :] = cv2.GC_BGD         # Bottom edge
mask[:, :width//border_size] = cv2.GC_BGD           # Left edge
mask[:, -width//border_size:] = cv2.GC_BGD          # Right edge

# Initialize models for GrabCut
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# Apply GrabCut algorithm
mask, bgd_model, fgd_model = cv2.grabCut(
    image_rgb, 
    mask, 
    None, 
    bgd_model, 
    fgd_model, 
    iterCount=5, 
    mode=cv2.GC_INIT_WITH_MASK
)

# Create final mask (0 and 2 = background, 1 and 3 = foreground)
final_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

# Apply mask to get segmented image
segmented = cv2.bitwise_and(image_rgb, image_rgb, mask=final_mask)

# Display results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title("GrabCut Mask")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(segmented)
plt.title("Segmented Result")
plt.axis('off')

plt.tight_layout()
plt.show()