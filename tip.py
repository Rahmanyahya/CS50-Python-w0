def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    temp = str(d).removeprefix('$')
    return float(temp)


def percent_to_float(p):
    # TODO
    temp = str(p).removesuffix('%')
    return int(temp) / 100
    
    
    


main()