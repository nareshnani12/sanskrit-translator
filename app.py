
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import cv2
import pytesseract
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

def extract_text(image_path):
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image, lang='san')  # 'san' for Sanskrit
    return text

from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='auto', dest='en')
    return translation.text

import streamlit as st
from PIL import Image

st.title("Sanskrit Image-to-English Translator")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with open("temp.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    extracted_text = extract_text("temp.png")
    translated_text = translate_text(extracted_text)

    st.subheader("Extracted Sanskrit Text:")
    st.write(extracted_text)

    st.subheader("Translated English Text:")
    st.write(translated_text)
