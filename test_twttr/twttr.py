def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    output = ""

    for character in word:
        if character.lower() not in "aeiou":
            output += character

    return output


if __name__ == "__main__":
    main()