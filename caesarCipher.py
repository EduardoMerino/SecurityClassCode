##Global variables:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_length = len(letters)

## Functions:
def caesar_cipher(msg, shift):
    cipher_message = ""
    msg = msg.lower()

    ## assuming that the message only contains letters from the english
    ## alphabet
    for word in msg.split():
        for c in word:
            current_index = letters.index(c)
            new_index = (current_index + shift) % letters_length
            cipher_message = cipher_message + letters[new_index]
        cipher_message = cipher_message + " "
    return cipher_message


## Main Code:
not_a_number = True
shift_text = ""
shift_numb = 0

while (not_a_number):
    shift_text = raw_input("Please enter a positive integer number cipher your message: ")
    try:
        shift_numb = int(shift_text)
        if (shift_numb <= 0):
            print("number isn't positive. Please try again.")
            not_a_number = True
        else:
            not_a_number = False
    except ValueError:
        print("Value isn't integer number. Please try again.")

message = raw_input("Please enter message to cipher: ")
coded_msg = caesar_cipher(message, shift_numb)
print("coded message: " + coded_msg)

#print("shift number: " + str(shift_numb) + ", message: " + message)
