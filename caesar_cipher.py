# The main Caesar Cipher function that handles both encryption and decryption
def caesar(text, shift, encrypt=True):
    # Validation: Ensures that the provided shift value is a whole number (integer)
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    # Validation: Ensures the shift is within the standard English alphabet range (1 to 25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    # The standard lowercase English alphabet used as the reference base
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # If encrypt is False, it means we want to decrypt. 
    # Turning the shift negative moves the alphabet backward instead of forward.
    if not encrypt:
        shift = - shift   
    # Creates the shifted version of the alphabet using string slicing.
    # For a shift of 13, it cuts the alphabet and wraps the first part to the end.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # Creates a 1-to-1 character mapping table. 
    # It combines lowercase and uppercase alphabets so that letter casing is preserved during translation.
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    # Applies the mapping table to the input text. 
    # Symbols, spaces, and punctuation remain untouched because they are not in the translation table.
    encrypted_text = text.translate(translation_table)
    return encrypted_text
# A helper function that calls the main caesar function for encryption
def encrypt(text, shift):
    return caesar(text, shift)
    # A helper function that calls the main caesar function with encrypt=False for decryption
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
# The original encrypted ciphertext provided in your query
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
# Calls the decrypt function with a shift of 13
decrypted_text = decrypt(encrypted_text, 13)# Prints the final decoded text to the console
# Output: Courage is found in unlikely places.
print(decrypted_text)
