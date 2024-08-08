# CaesarCipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(org_text, shift_amount):
    encrypt_text = ""
    for char in org_text:
        if char not in alphabet:
            encrypt_text += char
        char_index = alphabet.index(char) + shift_amount
        if char_index >= len(alphabet):
            char_index -= len(alphabet)
        encrypt_text += alphabet[char_index]
    print(f"Here is encoded result : {encrypt_text}")


def decrypt(org_text, shift_amount):
    decrypt_text = ""
    for char in org_text:
        if char not in alphabet:
            decrypt_text += char
        char_index = alphabet.index(char) - shift_amount
        if char_index < 0:
            char_index += len(alphabet)
        decrypt_text += alphabet[char_index]
    print(f"Here is decoded result : {decrypt_text}")


end_of_caesar_cipher = "yes"

art = '''
        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           '''

print(art)

while end_of_caesar_cipher != "no":
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode' because your input is a invalid pleas try later!")

    end_of_caesar_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if end_of_caesar_cipher == "no":
        print("GoodBye")
