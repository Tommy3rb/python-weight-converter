while True:
    unit = input("Lbs or Kg? ").lower()

    if unit == "lbs":
        lbs = float(input("Weight: "))
        print(f"{lbs * 0.453592:.2f} kg")
        break

    elif unit == "kg":
        kg = float(input("Weight: "))
        print(f"{kg / 0.453592:.2f} lbs")
        break

    else:
        print("Invalid input.")
