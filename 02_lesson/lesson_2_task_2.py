def is_year_leap(year):
    return True if year % 4 == 0 else False


year = int(input("Введите год: "))
print(f"год {year}: {is_year_leap(year)}")
