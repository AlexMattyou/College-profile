import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set up initial tracking window (x, y, width, height)
x, y, w, h = 200, 150, 50, 50  
track_window = (x, y, w, h)

# Take first frame and set up ROI for tracking
ret, frame = cap.read()
if not ret:
    print("Error: Failed to capture initial frame.")
    exit()

# Region of Interest (ROI) for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Create mask and calculate histogram
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup termination criteria (10 iterations or move 1 pixel)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Calculate back projection
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    
    # Apply meanshift to get new location
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)
    
    # Draw the tracking window
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display frame
    cv2.imshow("Object Tracking", frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()