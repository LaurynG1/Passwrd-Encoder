def encode_password(password):
    encoded_password = ''
    password_nums = [int(i) for i in passwrd]
    for i in password_nums:
        i += 3
        encoded_password += str(i)
    return encoded_password


if __name__ == "__main__":

    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        menu_sel = int(input('Please enter an option: '))
        if menu_sel == 1:
            global passwrd
            passwrd = input('Please enter your password to encode: ')
            global encoder
            encoder = encode_password(passwrd)
            print('Your password has been encoded and stored!')
        if menu_sel == 2:
            decoder = decode_password(passwrd)
            print('The encoded password is', encoder,
                  ', and the original password is', decoder, '.')
        if menu_sel == 3:
            break
