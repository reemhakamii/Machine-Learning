import numpy as np

# Task 3.1
img = np.arange(36).reshape(6, 6)
print("Original Image:\n", img)
print("-" * 40)

# Task 3.2
center = img[1:5, 1:5]
print("Center Region:\n", center)
print("-" * 40)

# Task 3.3
bright_center = center + 10
print("Brightened Center:\n", bright_center)
print("-" * 40)

# Task 3.4
img[1:5, 1:5] = bright_center
print("Updated Image:\n", img)
print("-" * 40)

# Task 3.5
print("Mean Intensity:", img.mean())
print("Max Intensity:", img.max())
print("Min Intensity:", img.min())
print("-" * 40)

# Lab question 4
border_mask = np.ones((6, 6), dtype=bool)
border_mask[1:5, 1:5] = False
img[border_mask] -= 5

print("Image after decreasing border brightness by 5:\n", img)
print("-" * 40)

# Lab question 5
print("Standard Deviation of Final Image:", img.std())