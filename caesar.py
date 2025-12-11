import string
import collections

# Standard English letter frequencies
ENGLISH_FREQS = {
    'a': 0.0816, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270,
    'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015,
    'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751,
    'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0905,
    'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197,
    'z': 0.0007
}

def decrypt(text, shift):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - shift - 65) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - shift - 97) % 26 + 97))
        else:
            result.append(char)
    return "".join(result)

def calculate_chi_square(text):
    text_only_letters = [c.lower() for c in text if c.isalpha()]
    total_count = len(text_only_letters)
    
    if total_count == 0:
        return 999999
        
    observed_counts = collections.Counter(text_only_letters)
    chi_sq_score = 0.0
    
    for char in string.ascii_lowercase:
        observed = observed_counts.get(char, 0)
        expected = total_count * ENGLISH_FREQS[char]
        if expected > 0:
            difference = observed - expected
            chi_sq_score += (difference * difference) / expected
            
    return chi_sq_score

def break_caesar_chi_square(ciphertext):
    best_shift = 0
    lowest_chi_score = float('inf')
    best_decryption = ""
    
    # Just for the preview length
    preview_len = len(ciphertext)
    
    print(f"\nAnalyzing '{ciphertext[:20]}...' using Chi-Square:\n")
    print(f"{'Shift':<6} | {'Chi-Square Score':<18} | {'Preview'}")
    print("-" * 50)

    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        score = calculate_chi_square(decrypted_text)
        
        # Determine if we should print this line
        # If text is short (<40 chars), PRINT ALL to help the human
        if len(ciphertext) < 40:
             print(f"{shift:<6} | {score:<18.4f} | {decrypted_text}")
        # If text is long, only print good scores to keep terminal clean
        elif score < 100: 
             print(f"{shift:<6} | {score:<18.4f} | {decrypted_text[:30]}...")
        
        if score < lowest_chi_score:
            lowest_chi_score = score
            best_shift = shift
            best_decryption = decrypted_text
            
    return best_shift, best_decryption, lowest_chi_score

if __name__ == "__main__":
    print("--- Chi-Square Frequency Analysis ---")
    print("Enter text manually")
    target_text = input("Enter Encrypted Text: ")
    if target_text:
        shift, result, score = break_caesar_chi_square(target_text)
        
        print(f"\nSTATISTICAL BEST MATCH (Computer's Guess):")
        print(f"Shift: {shift}")
        print(f"Score: {score:.4f}")
        print(f"Message: {result}")
        
        # --- THE WARNING LOGIC ---
        if len(target_text) < 40:
            print(" WARNING: SHORT TEXT DETECTED!")
            print(" The 'Best Match' above is purely mathematical.")
            print(" Because the text is short, the computer often guesses wrong.")
            print(" (Example: It prefers 'wtaad' over 'hello' due to probability).")
            print("\n -> PLEASE SCROLL UP AND READ THE TABLE FOR THE REAL MESSAGE.")
            