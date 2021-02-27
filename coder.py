#Cesar Code

def new_message(message):
    # create a empty message
    encrypted_message = ''
    #define the alphabet
    lower_alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    upper_alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    #Examine all letter in the message
    for letter in message :
        if letter in lower_alphabet: #if it is lowercase
            new_letter = lower_alphabet.index(letter) #find index of it
            encrypted_message += lower_alphabet[new_letter+2] #use the index  two more from letter
            # and add a new letter  to new message
        elif letter in upper_alphabet:
            new_letter = upper_alphabet.index(letter)
            encrypted_message += upper_alphabet[new_letter+2]
        else: #if letter is nor in alphabet thet you define print '*'
            encrypted_message += '*'
    print(encrypted_message)

message = input('Your Message => ')
new_message(message)