# functions to match patterns -> not optimal 
def match_pattern(text: str, subpattern: str) -> dict:
    # empty subpattern string
    if not subpattern:
        return {"Empty subpattern" : [-1, -1]}  # Return no match for empty pattern
        
    text_length = len(text)
    subpattern_length = len(subpattern)
    text_index = 0
    subpattern_index = 0


    while text_index < text_length:  # Iterate through the main text
        # Attempt to match the pattern
        while subpattern_index < subpattern_length and text_index < text_length:
            if text[text_index] == subpattern[subpattern_index]:
                text_index += 1
                subpattern_index += 1  # Move forward in both text and pattern
            else:
                subpattern_index = 0  # Reset pattern index on mismatch
                break

        if subpattern_index == subpattern_length:  # Full pattern matched
            return {f"Match \"{subpattern}\" found": [text_index - subpattern_length, text_index - 1]}  # Return match start & end indices

        text_index += 1  # Move to the next character in the text
        
    return {f"No match \"{subpattern}\" found" : [-1, -1]} # No match found

print(match_pattern("10001001111", "00"))



# IMPLEMENT ONE TO RETURN ALL MATCHES 


