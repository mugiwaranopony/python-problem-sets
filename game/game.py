import random


def main():
    while True:
        try:
            level = int(input("Level: "))

            if level > 0:
                break

        except ValueError:
            continue

    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0:
                continue

        except ValueError:
            continue

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()