# Experiment 1: Caesar, Vigenere, and Rail Fence Ciphers
# Aim: To encrypt and decrypt the plaintext "HELLO WORLD"
# using three classical encryption algorithms.


def ceaser_encrypt(text,shift):
    result=""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-base+shift)%26+base)
        else:
            result+=char
    return result

def ceaser_decrypt(text,shift):
    return(ceaser_encrypt(text,-shift))
text = input("enter the text:")
shift = int(input("enter the shift number:"))



choice =(input("enter E for enc and D for dec:"))

if choice.upper() == "E":
    encrypted= ceaser_encrypt(text,shift)
    print("encrypted text:",encrypted)
elif choice.upper() == "D":
    decrypted= ceaser_decrypt(text,shift)
    print("decrypted shift:",decrypted)
else :
    print("invalid choice")




