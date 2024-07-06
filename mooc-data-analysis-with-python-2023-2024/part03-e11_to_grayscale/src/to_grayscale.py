#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    """
    Convert an RGB image to grayscale by applying weights to each color channel.

    Parameters:
    image (ndarray): RGB image with shape (height, width, 3)

    Returns:
    ndarray: Grayscale image with shape (height, width)
    """
    # Print the shape of the input image
    print("Input image shape:", image.shape)

    # Define the weights for each color channel
    weights = [0.2126, 0.7152, 0.0722]
    print("Weights:", weights)

    # Apply the weights to each color channel and sum along the third axis
    grayscale_image = np.sum(weights * image, axis=2)
    print("Grayscale image shape:", grayscale_image.shape)

    return grayscale_image

def to_red(image):
    weights = [1,0,0]
    return image * weights

def to_green(image):
    weights = [0,1,0]
    return image * weights

def to_blue(image):
    weights = [0,0,1]
    return image * weights


def main():
    """
    Load a sample image, convert it to different color channels and grayscale,
    and display the results.
    """
    # Load the image
    print("Loading image...")
    painting = plt.imread("src/painting.png")
    print("Image loaded.")

    # Convert the image to different color channels
    print("Converting to different color channels...")
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(painting))  # Red channel
    ax[1].imshow(to_green(painting))  # Green channel
    ax[2].imshow(to_blue(painting))  # Blue channel
    plt.show()
    print("Color channels converted.")

    # Convert the image to grayscale
    print("Converting to grayscale...")
    greyscaled = to_grayscale(painting)
    print("Grayscaled.")

    # Display the grayscale image
    print("Displaying grayscale image...")
    plt.imshow(greyscaled, cmap='gray')
    plt.show()
    print("Grayscale image displayed.")

if __name__ == "__main__":
    main()
