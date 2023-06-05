import cv2
import numpy as np

def enhance_sharpness(image, mtf_curve, sharpening_factor):
    # Perform Fourier Transform on the image
    image_fft = np.fft.fft2(image)
    image_fft_shifted = np.fft.fftshift(image_fft)

    # Get the frequency grid for the image
    rows, cols = image.shape
    frequency_grid = np.fft.fftfreq(rows, 1 / rows)[:rows // 2]

    # Calculate the MTF correction curve
    mtf_correction = np.interp(frequency_grid, mtf_curve[:, 0], mtf_curve[:, 1], left=0, right=0)
    mtf_correction = np.tile(mtf_correction, (cols, 1)).T

    # Apply the MTF correction to the frequency domain
    sharpened_fft_shifted = image_fft_shifted * mtf_correction

    # Perform inverse Fourier Transform to obtain the sharpened image
    sharpened_fft = np.fft.ifftshift(sharpened_fft_shifted)
    sharpened_image = np.fft.ifft2(sharpened_fft).real

    # Apply sharpening factor to enhance sharpness
    enhanced_image = (image + sharpening_factor * sharpened_image).clip(0, 255).astype(np.uint8)

    return enhanced_image

# Example usage
image_path = 'path/to/your/image.jpg'
mtf_curve = np.loadtxt('path/to/your/mtf_curve.txt')  # Load the MTF curve (frequency, MTF) from a text file
sharpening_factor = 0.5

# Load the image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Enhance sharpness using MTF
enhanced_image = enhance_sharpness(image, mtf_curve, sharpening_factor)

# Display the original and enhanced images
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
