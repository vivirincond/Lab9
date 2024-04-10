from vvr_encode import encode

def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            pass_word = str(input("Please enter your password to encode: "))
            encode(pass_word)
            print("Your password has been encoded and sorted!\n")
        if option==2:
            print(f"The encoded password is {encode(pass_word)}, and the original password is {pass_word}")
        if option==3:
            exit(1)

if __name__ == "__main__":
    main()
