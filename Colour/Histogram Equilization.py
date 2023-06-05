import cv2

# Load the image
image_path = 'path/to/your/image.jpg'
image = cv2.imread(image_path)

# Convert the image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Split the LAB image into L, A, and B channels
l_channel, a_channel, b_channel = cv2.split(lab_image)

# Apply histogram equalization to the L channel
equ_l_channel = cv2.equalizeHist(l_channel)

# Merge the equalized L channel with the original A and B channels
enhanced_lab_image = cv2.merge([equ_l_channel, a_channel, b_channel])

# Convert the enhanced LAB image back to BGR color space
enhanced_bgr_image = cv2.cvtColor(enhanced_lab_image, cv2.COLOR_LAB2BGR)

# Display the enhanced image
cv2.imshow('Enhanced Image', enhanced_bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
