import cv2
import numpy as np

class Rem2:

    def bgremove2(myimage):
        # First Convert to Grayscale
        myimage_grey = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)

        ret, baseline = cv2.threshold(myimage_grey, 150, 255, cv2.THRESH_TRUNC)

        ret, background = cv2.threshold(baseline, 126, 255, cv2.THRESH_BINARY)

        ret, foreground = cv2.threshold(baseline, 126, 255, cv2.THRESH_BINARY_INV)

        foreground = cv2.bitwise_and(myimage, myimage,
                                     mask=foreground)  # Update foreground with bitwise_and to extract real foreground

        # Convert black and white back into 3 channel greyscale
        background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)

        # Combine the background and foreground to obtain our final image
        finalimage = background + foreground
        return finalimage