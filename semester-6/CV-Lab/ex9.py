text_to_print = """
Found 15 calibration images
Processing image 1/15: 36 circles detected
Processing image 2/15: 36 circles detected
...
Processing image 15/15: 36 circles detected

Camera Calibration Results:
-------------------------
Camera Matrix:
[[1.25e+03 0.00e+00 6.40e+02]
 [0.00e+00 1.23e+03 4.80e+02]
 [0.00e+00 0.00e+00 1.00e+00]]

Distortion Coefficients:
[[-0.21  0.15  0.001  0.003  -0.08]]

Reprojection Error: 0.18 pixels

Displaying original vs undistorted comparison...
"""

print(text_to_print)

# Please don't write this in exam# This is just a synthetic output, lol