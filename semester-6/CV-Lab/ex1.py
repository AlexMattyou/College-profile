import os
import cv2
import matplotlib.pyplot as plt

# Load the image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "test.jpg")
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to RGB for correct Matplotlib display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Display images using Matplotlib
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    axs[0, 0].imshow(image_rgb)
    axs[0, 0].set_title("Original Image")
    axs[0, 1].imshow(gray, cmap="gray")
    axs[0, 1].set_title("Grayscale Image")
    axs[1, 0].imshow(blurred, cmap="gray")
    axs[1, 0].set_title("Blurred Image")
    axs[1, 1].imshow(edges, cmap="gray")
    axs[1, 1].set_title("Edge Detected Image")

    for ax in axs.flat:
        ax.axis("off")
    
    plt.show()