def encode_password(password): # encode password function
    encoded_password = ''
    password_nums = [int(i) for i in password]
    for i in password_nums:
        i += 3
        encoded_password += str(i)
    return encoded_password

def decode_password(password): # Shaina D
    decoded_password = ''
    password_nums = [int(i) for i in password]
    for i in password_nums:
        i -= 3  # reverses the changes made by the encoder
        decoded_password += str(i)
    return decoded_password

if __name__ == "__main__":

    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        menu_sel = int(input('Please enter an option: '))
        if menu_sel == 1:
            global password  # global use to use in other menu option
            password = input('Please enter your password to encode: ')
            global encoder  # global use to use in other menu option
            encoder = encode_password(password)
            print('Your password has been encoded and stored!')
        if menu_sel == 2:
            decoder = decode_password(encoder)  # decode function will be added by partner
            # calls back the original password
            print('The encoded password is', encoder,
                  ', and the original password is', decoder, '.')
        if menu_sel == 3:
            break
