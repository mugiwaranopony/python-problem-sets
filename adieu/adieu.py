import inflect


def main():
    names = []
    engine = inflect.engine()

    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break

    joined_names = engine.join(names)
    print(f"Adieu, adieu, to {joined_names}")


if __name__ == "__main__":
    main()