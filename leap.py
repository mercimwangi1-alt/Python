def is_leap_year(year):
    """
    Return True if `year` is a leap year, else False.

    Rules (Gregorian calendar):
      1. A year divisible by 400 is a leap year.
      2. Otherwise, a year divisible by 100 is NOT a leap year.
      3. Otherwise, a year divisible by 4 IS a leap year.
      4. All other years are not leap years.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def get_year():
    """Keep asking until the user enters a valid positive whole number."""
    while True:
        text = input("Enter a year (e.g. 2024): ").strip()
        try:
            year = int(text)
            if year <= 0:
                print("Please enter a positive year (1 or greater).")
                continue
            return year
        except ValueError:
            print("Invalid input. Please enter a whole number like 2024.")


def main():
    print("=== Leap Year Checker ===")
    while True:
        year = get_year()

        if is_leap_year(year):
            print(f"{year} is a leap year. (February has 29 days)")
        else:
            print(f"{year} is NOT a leap year. (February has 28 days)")

        again = input("\nCheck another year? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()