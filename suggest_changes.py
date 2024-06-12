from transformers import pipeline

# Initialize a pipeline for text generation (this requires a pre-trained or fine-tuned model)
suggestion_pipeline = pipeline('text-generation', model='gpt-4')

def suggest_changes(code_snippet, error_type):
    prompt = f"Code Snippet:\n{code_snippet}\n\nError Type: {error_type}\n\nSuggest changes to resolve the error:"
    suggestions = suggestion_pipeline(prompt, max_length=200)
    
    return suggestions[0]['generated_text']

# Update the extract_info function to include suggested changes
def extract_info(text):
    ide_pattern = r'IDE:\s*(\w+)'
    language_pattern = r'Language:\s*(\w+)'
    error_type_pattern = r'Error Type:\s*(\w+)'
    code_snippet_pattern = r'Code Snippet:\s*(.*?)(Error|$)'
    file_structure_pattern = r'File Structure:\s*(.*?)(Error|$)'

    ide = re.search(ide_pattern, text)
    language = re.search(language_pattern, text)
    error_type = re.search(error_type_pattern, text)
    code_snippet = re.search(code_snippet_pattern, text, re.DOTALL)
    file_structure = re.search(file_structure_pattern, text, re.DOTALL)

    code_snippet_text = code_snippet.group(1).strip() if code_snippet else None
    error_type_text = error_type.group(1) if error_type else None

    suggested_changes = suggest_changes(code_snippet_text, error_type_text) if code_snippet_text and error_type_text else None

    info = {
        "IDE": ide.group(1) if ide else None,
        "Language": language.group(1) if language else None,
        "Code Snippet": code_snippet_text,
        "Error Type": error_type_text,
        "File Structure": file_structure.group(1).strip() if file_structure else None,
        "Suggested Changes": suggested_changes
    }
    
    return info
