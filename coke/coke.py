def main():
    amount_due = 50
    accepted_coins = [5, 10, 25]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            amount_due -= coin

    print(f"Change Owed: {-amount_due}")


if __name__ == "__main__":
    main()