def main():
    text = input("Input: ")
    output = ""

    for character in text:
        if character.lower() not in "aeiou":
            output += character

    print("Output:", output)


if __name__ == "__main__":
    main()