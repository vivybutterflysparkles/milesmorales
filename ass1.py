# a python program that prompts a user to enter a letter then checks if the letter is a consonant or a vowel

def check_vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"

    if len(letter) == 1:
        if letter.isalpha():
            if letter in vowels:
                print(f"The letter '{letter}' is a vowel.")
            else:
                print(f"The letter '{letter}' is a consonant.")
        else:
            print(f"'{letter}' is not a valid letter.")
    else:
        print("Please enter exactly one letter.")

def main():
    letter = input("Enter a letter: ")
    check_vowel_or_consonant(letter)

if __name__ == "__main__":
    main()
