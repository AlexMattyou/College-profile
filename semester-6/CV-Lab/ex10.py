import cv2
import numpy as np

# Start capturing from webcam (use CAP_DSHOW backend for Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame = cap.read()
if not ret:
    print("Error: Cannot read video frame")
    exit()

# Select ROI (Region of Interest) manually
roi_box = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
x, y, w, h = roi_box
roi = frame[y:y+h, x:x+w]
cv2.destroyWindow("Select Object")

# Convert ROI to HSV and create mask
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# CamShift criteria
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
track_window = (x, y, w, h)

# Kalman Filter setup
kalman = cv2.KalmanFilter(4, 2)
kalman.measurementMatrix = np.array([[1, 0, 0, 0],
                                     [0, 1, 0, 0]], np.float32)
kalman.transitionMatrix = np.array([[1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]], np.float32)
kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    back_proj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply CamShift
    ret_camshift, track_window = cv2.CamShift(back_proj, track_window, term_criteria)
    pts = cv2.boxPoints(ret_camshift)
    pts = np.intp(pts)
    center_x = int(np.mean(pts[:, 0]))
    center_y = int(np.mean(pts[:, 1]))

    # Kalman prediction and correction
    prediction = kalman.predict()
    kalman.correct(np.array([[np.float32(center_x)], [np.float32(center_y)]]))

    # Draw tracking result
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
    cv2.circle(frame, (int(prediction[0]), int(prediction[1])), 5, (0, 0, 255), -1)

    cv2.imshow("Object Tracking", frame)
    key = cv2.waitKey(30)
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
