#Linwei Zhang

def encode(password):
    password_list = []
    for each_number in str(password):
        integer = int(each_number)
        password_list.append(integer+3)

    new_password = ""
    for each_digit in password_list:
        new_password += str(each_digit)
        encoded_password = int(new_password)
    return encoded_password



def main():
    while True:
        print("""Menu:
        -------------
        1. Encode
        2. Decode
        3. Quit""")

        option = int(input("Please enter an option: "))

        if option == 1:
            my_password = input("Please enter your password to encode: ")
            encoded_password = encode(my_password)
            print("Your password has been encoded and stored!")
            continue

        if option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        if option == 3:
            break


if __name__ == "__main__":
    main()


