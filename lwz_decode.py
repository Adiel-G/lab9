
def decode(password):
    decoded_password = ""
    for digit in password:
        decoded_password += str(int(digit)-3)
    return decoded_password

