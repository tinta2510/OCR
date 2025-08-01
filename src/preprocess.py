import numpy as np
import cv2
from deskew import determine_skew
    
def convert_bgr2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def denoise(gray):
    return cv2.medianBlur(gray, 3)

def binarize(gray):
    # _, img = cv2.threshold(gray, 210, 230, cv2.THRESH_BINARY)
    # img = cv2.adaptiveThreshold(
    #     gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #     cv2.THRESH_BINARY, 11, 2
    # )
    _, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return img

def deskew(image):
    angle = determine_skew(image)
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# def preprocess_image(image):

    
#     # Denoise
#     denoised = cv2.medianBlur(gray, 3)
    
    