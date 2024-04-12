#Jessica Wu
#partner: Harry Lyu

def encode(password):
    encoded_password_list = []
    encoded_password_list[:] = password
    digit = 0
    encoded_password = ""
    for i in range (len(encoded_password_list)):
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
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        if option == "3":
            break



if __name__ == '__main__':
    main()