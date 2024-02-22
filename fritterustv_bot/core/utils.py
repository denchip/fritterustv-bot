def format_string(pattern: str, text: str = None) -> str:
    if '{text}' in str:
        pattern = pattern.replace('{text}', text)
