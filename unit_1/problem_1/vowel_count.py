vowels = "aeiou"

def count_in_substring(text: str) -> int:
    final_count = [char for char in text if char in vowels]
    return len(final_count)


