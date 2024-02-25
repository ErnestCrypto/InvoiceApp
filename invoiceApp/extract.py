import pytesseract
import cv2
import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe "
data = []


def extract_img(file):
    img = cv2.imread(file)
    d = pytesseract.image_to_string(img,output_type=Output.DICT)
    lines = d['text'].split('\n')
    for line in lines:
        if line:
            data.append(line)
    return data