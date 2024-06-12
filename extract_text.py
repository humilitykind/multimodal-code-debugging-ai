import pytesseract

def extract_text(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Use Pytesseract to extract text
    text = pytesseract.image_to_string(preprocessed_image)
    
    return text
