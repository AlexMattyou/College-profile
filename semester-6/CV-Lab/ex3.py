import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the image with proper path handling
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "test.jpg")  # Using test.jpg as requested
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image not found at {image_path}!")

# Draw a line (blue)
cv2.line(image, (10, 70), (250, 70), (255, 0, 0), 5)

# Draw a rectangle (green)
cv2.rectangle(image, (470, 180), (560, 400), (0, 255, 0), 3)

# Draw a circle (red, filled)
cv2.circle(image, (600, 100), 50, (0, 100, 255), -1)

# Draw an ellipse (yellow)
cv2.ellipse(image, (300, 200), (100, 50), 45, 0, 180, (255, 255, 0), 2)

# Add text to the image (cyan)
cv2.putText(image, "Vinland Saga", (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

# Display the image using Matplotlib (with BGR to RGB conversion)
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis("off")
plt.title("Annotated Image")
plt.show()