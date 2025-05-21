import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Load the image with proper path handling
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "test.jpg")  # Assuming rose.jpg is in the same directory
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Crop the image (Region of Interest)
cropped = image[50:300, 100:400]  # Crop (y1:y2, x1:x2)

# Step 4: Resize the image
resized = cv2.resize(image, (300, 300))

# Step 5: Apply thresholding
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 6: Contour detection
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Step 7: Blob detection
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100  # Minimum blob size
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(thresholded)
blob_image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Step 8: Display all images
titles = ["Original", "Grayscale", "Cropped", "Resized", "Thresholded", "Contours", "Blobs"]
images = [image, gray, cropped, resized, thresholded, contour_image, blob_image]

fig, axs = plt.subplots(2, 4, figsize=(15, 8))
for i, ax in enumerate(axs.flat[:7]):
    cmap = "gray" if len(images[i].shape) == 2 else None
    if cmap is None:
        ax.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    else:
        ax.imshow(images[i], cmap=cmap)
    ax.set_title(titles[i])
    ax.axis("off")

plt.tight_layout()
plt.show()