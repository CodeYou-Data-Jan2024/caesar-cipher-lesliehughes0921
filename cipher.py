def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char.lower()) + shift
            if shifted > ord('z'):
                shifted -= 26  
            encrypted_text += chr(shifted) 
        else:
            encrypted_text += char 
    return encrypted_text

sentence = input("Please enter a sentence: ")

encrypted_sentence = caesar_cipher(sentence, 5)

print("The encrypted sentence is:", encrypted_sentence)