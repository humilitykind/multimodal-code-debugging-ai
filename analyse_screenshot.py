def analyze_screenshot(image_path):
    text = extract_text(image_path)
    info = extract_info(text)
    return info

# Example usage
image_path = 'screenshot.png'
info = analyze_screenshot(image_path)
print(info)
