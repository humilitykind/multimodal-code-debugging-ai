import re

def extract_info(text):
    # Define regex patterns for different information
    ide_pattern = r'IDE:\s*(\w+)'
    language_pattern = r'Language:\s*(\w+)'
    error_type_pattern = r'Error Type:\s*(\w+)'
    code_snippet_pattern = r'Code Snippet:\s*(.*?)(Error|$)'
    file_structure_pattern = r'File Structure:\s*(.*?)(Error|$)'

    # Extract information using regex
    ide = re.search(ide_pattern, text)
    language = re.search(language_pattern, text)
    error_type = re.search(error_type_pattern, text)
    code_snippet = re.search(code_snippet_pattern, text, re.DOTALL)
    file_structure = re.search(file_structure_pattern, text, re.DOTALL)

    # Prepare the JSON output
    info = {
        "IDE": ide.group(1) if ide else None,
        "Language": language.group(1) if language else None,
        "Code Snippet": code_snippet.group(1).strip() if code_snippet else None,
        "Error Type": error_type.group(1) if error_type else None,
        "File Structure": file_structure.group(1).strip() if file_structure else None,
        "Suggested Changes": None  # Placeholder for suggested changes
    }
    
    return info
