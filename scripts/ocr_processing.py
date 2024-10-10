import pytesseract
from PIL import Image

def extract_text(image_path):
    img = Image.open(image_path).convert('L')
    text = pytesseract.image_to_string(img)
    return text

# Example usage
if __name__ == "__main__":
    sample_image_path = '../dataset/images/sample_document.jpg'
    extracted_text = extract_text(sample_image_path)
    print("Extracted Text:", extracted_text)
