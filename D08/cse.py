# caser cipher: is a way of encrypt the sentence by shift in some amount
from art import logos

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z']
print(logos)

# encrypted_text=[]
# decrypt_text=[]
# def encrypt_palintext(text,shift):
#     for letter in text:
#         if letter in alphabet:
#             index_of_letter=alphabet.index(letter)
#             index_of_letter=(shift + index_of_letter)%26
#             encrypted_text.append(alphabet[index_of_letter])
#         else:
#             encrypted_text.append(letter)
#     print(f"The encode message {"".join(encrypted_text)}") 

# def decrypt_ciphertext(text,shift):

#     for letter in text:
#         if letter in alphabet:
#             index_of_letter=alphabet.index(letter)
#             new_shift=(index_of_letter-shift)%26
#             decrypt_text.append(alphabet[new_shift])
#         else:
#             decrypt_text.append(letter)
#     print(f"The decode message is {"".join(decrypt_text)}")

# match direction:
#     case "encode":
#         encrypt_palintext(shift=shift,text=text)
#     case "decode":
#         decrypt_ciphertext(shift=shift,text=text)
#     case _:
#         print("Pleas enter the correct match!")

cipher_text=[]
def caesar(text,shift,direction):
        
        for letter in text:
            if letter in alphabet:
                 index_of_letter=alphabet.index(letter)
                 if direction=="encode":
                      index_of_letter=(shift + index_of_letter)%26
                      cipher_text.append(alphabet[index_of_letter])
                 elif direction=="decode":
                      new_shift=(index_of_letter-shift)%26
                      cipher_text.append(alphabet[new_shift])       
            else:
                 cipher_text.append(letter)
        print(f"The {direction} message {"".join(cipher_text)}") 

shouls_continue=True
while shouls_continue:
     direction=input("Type either encode or decode what you want!")
     text=input("Enetr your message?").lower()
     shift=int(input("Enter your shift amount?"))
     caesar(text=text,shift=shift,direction=direction)
     restart = input("Do you want to try again? (yes/no): ").lower()
     if restart != "yes":
        shouls_continue=False
        print("Goodbye!")
        
    

