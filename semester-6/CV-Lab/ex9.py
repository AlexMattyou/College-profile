import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

# Define the circular grid size (columns, rows)
grid_size = (4, 11)  # Update based on your printed pattern

# Arrays to store object points and image points
object_points = []  # 3D points in real world
image_points = []   # 2D points in image plane

# Prepare object points (e.g., (0,0,0), (1,0,0), ..., (3,10,0))
objp = np.zeros((grid_size[0] * grid_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:grid_size[0], 0:grid_size[1]].T.reshape(-1, 2)

# Load all images from folder
image_folder = "D:/CV-Lab/CalibrationImgs/*.jpg"  # ← Update this path
images = glob.glob(image_folder)

if not images:
    print("Error: No calibration images found!")
    exit()

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the circle grid
    ret, centers = cv2.findCirclesGrid(gray, grid_size, flags=cv2.CALIB_CB_SYMMETRIC_GRID)

    if ret:
        object_points.append(objp)
        image_points.append(centers)

        # Draw and show the pattern
        img_vis = cv2.drawChessboardCorners(img, grid_size, centers, ret)
        cv2.imshow('Detected Pattern', img_vis)
        cv2.waitKey(100)

cv2.destroyAllWindows()

# Calibrate the camera
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    object_points, image_points, gray.shape[::-1], None, None
)

print("\n--- Calibration Results ---")
print("Camera Matrix:\n", camera_matrix)
print("Distortion Coefficients:\n", dist_coeffs)

# Undistort one sample image
sample_img = cv2.imread(images[0])
h, w = sample_img.shape[:2]
new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w,h), 1, (w,h))
undistorted = cv2.undistort(sample_img, camera_matrix, dist_coeffs, None, new_camera_mtx)

# Show original vs undistorted
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title("Undistorted")
plt.imshow(cv2.cvtColor(undistorted, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
