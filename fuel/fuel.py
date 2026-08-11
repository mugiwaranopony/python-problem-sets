def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            percentage = round((x / y) * 100)

            if x < 0 or x > y:
                continue

            break

        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()