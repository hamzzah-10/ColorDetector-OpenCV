import cv2
import numpy as np

def get_limits(color_name):
    if color_name == 'red':
        # Red has two ranges in HSV
        lowerLimit1 = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit1 = np.array([10, 255, 255], dtype=np.uint8)

        lowerLimit2 = np.array([160, 100, 100], dtype=np.uint8)
        upperLimit2 = np.array([179, 255, 255], dtype=np.uint8)

        return [lowerLimit1, lowerLimit2], [upperLimit1, upperLimit2]
    
    elif color_name == 'green':
        lowerLimit = np.array([50, 100, 100], dtype=np.uint8)
        upperLimit = np.array([70, 255, 255], dtype=np.uint8)

        return [lowerLimit], [upperLimit]

    elif color_name == 'yellow':
        lowerLimit = np.array([20, 100, 100], dtype=np.uint8)
        upperLimit = np.array([30, 255, 255], dtype=np.uint8)

        return [lowerLimit], [upperLimit]
    
    else:
        raise ValueError("Unsupported color! Please use 'red', 'green', or 'yellow'.")
