data1 = input("data_user_input_string_1: " )
data2 = input("data_user_input_string_2: " )

def common_characters(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")

def main():
   common_characters(data1, data2)

if __name__ == "__main__":
    main()


# Output example
#Character 'o' is found in both the strings
#Character 's' is found in both the strings
#Character 'e' is found in both the strings
