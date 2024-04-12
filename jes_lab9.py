#Jessica Wu
#Partner: Harry Lyu

def decode(password):
    decoded_password_list = []
    decoded_password_list[:] = password
    digit = 0
    decoded_password = ""
    for i in range(0,len(decoded_password_list)):
        if int(password[i]) < 3:
            digit = int(decoded_password_list[i]) + 7
        else:
            digit = int(decoded_password_list[i]) - 3
        decoded_password += str(digit)
    return decoded_password

def encode(password):
    encoded_password_list = []
    encoded_password_list[:] = password
    digit = 0
    encoded_password = ""
    for i in range (len(encoded_password_list)):
        if int(encoded_password_list[i]) > 6:
            digit = int(encoded_password_list[i]) - 7
        else:
            digit = int(encoded_password_list[i]) + 3
        encoded_password += str(digit)
    return encoded_password

def main():
    while True:
        print()
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
        elif option == "3":
            break
        else:
            print("Please enter valid choice number!\n")

if __name__ == '__main__':
    main()