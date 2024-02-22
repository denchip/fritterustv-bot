import random


def format_string(pattern: str, text: str = None, unique_hash: int = None) -> str:
    if '{text}' in pattern:
        pattern = pattern.replace('{text}', text)
    if '{rand1-100}' in pattern:
        pattern = pattern.replace('{rand1-100}', str(random.randint(1, 100)))
    if '{dayrand1-100}' in pattern:
        pattern = pattern.replace('{dayrand1-100}', str(unique_hash % 101))
    return pattern
