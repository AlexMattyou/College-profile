import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load images from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
img1_path = os.path.join(script_dir, "a.jpg")  # First image
img2_path = os.path.join(script_dir, "a2.jpg")  # Second image

# Load images
image1 = cv2.imread(img1_path)
image2 = cv2.imread(img2_path)

if image1 is None or image2 is None:
    print("Error: One or both images not found!")
    print(f"Looking for: {img1_path} and {img2_path}")
    exit()

# Convert to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Step 1: Fourier Transform
def show_fourier_transform(gray_img):
    f = np.fft.fft2(gray_img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = np.abs(fshift)
    return np.log(magnitude_spectrum + 1)

fourier_spectrum = show_fourier_transform(gray1)

# Step 2: Hough Transform for Line Detection
def detect_lines(img):
    edges = cv2.Canny(img, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    line_img = img.copy()
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return line_img

hough_image = detect_lines(image1)

# Step 3: ORB Feature Extraction
orb = cv2.ORB_create(nfeatures=500)
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

orb_image = cv2.drawKeypoints(image1, keypoints1, None, color=(0, 255, 0), flags=0)

# Step 4: Feature Matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1, descriptors2) if descriptors1 is not None and descriptors2 is not None else []

match_image = None
if len(matches) > 10:
    matches = sorted(matches, key=lambda x: x.distance)
    match_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, 
                                matches[:10], None,
                                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Step 5: Image Alignment
aligned_image = None
if len(matches) > 10:
    src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)
    
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    if H is not None:
        h, w = image2.shape[:2]
        aligned_image = cv2.warpPerspective(image1, H, (w, h))

# Step 6: Image Cloning (Poisson Blending)
cloned_image = None
if aligned_image is not None:
    # Create a simple mask (center rectangle)
    h, w = gray2.shape
    mask = np.zeros(gray2.shape, dtype=np.uint8)
    cv2.rectangle(mask, (w//4, h//4), (3*w//4, 3*h//4), 255, -1)
    
    center = (w//2, h//2)
    cloned_image = cv2.seamlessClone(aligned_image, image2, mask, center, cv2.NORMAL_CLONE)

# Display results
titles = ["Original Image", "Fourier Spectrum", "Hough Lines", 
          "ORB Keypoints", "Feature Matches", "Aligned Image", "Cloned Image"]
images = [image1, fourier_spectrum, hough_image, 
          orb_image, match_image, aligned_image, cloned_image]

# Filter valid images
valid_images = [(img, title) for img, title in zip(images, titles) if img is not None]
rows = (len(valid_images) // 4) + 1

plt.figure(figsize=(20, 5*rows))
for i, (img, title) in enumerate(valid_images):
    plt.subplot(rows, 4, i+1)
    if len(img.shape) == 2:  # Grayscale
        plt.imshow(img, cmap='gray')
    else:  # Color
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()