import cv2
class Tools:
    
    def rotate(self, img, angle):
        img = cv2.rotate(img, angle)
        return img