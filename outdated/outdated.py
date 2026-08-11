def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            elif "," in date:
                month_and_day, year = date.split(", ")
                month_name, day = month_and_day.split(" ")

                if month_name not in months:
                    continue

                month = months.index(month_name) + 1
                day = int(day)
                year = int(year)

            else:
                continue

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break

        except ValueError:
            continue


if __name__ == "__main__":
    main()