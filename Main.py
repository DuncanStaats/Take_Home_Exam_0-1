def fun_1(province, region):
    province = {"Newfoundland": "A", "Nova Scotia": "B", "Prince Edward Island": "C", "New Brunswick": "E",
                "Quebec": "GHJ", "Ontario": "KLMNP", "Manitoba": "R", "Saskatchewan": "S","Alberta": "T", 
                "British Columbia": "V", "Nunavat": "X", "Northwest Territories": "X", "Yukon": "Y"}
    region = {"Urban": "123456789", "Rural": "0"}
    return province, region

def fun_2(province,region):
    while True:
        code = input("Enter in your postal code: ")
        code = code.split()
        for i in range(len(code)):
            if code[0][0] == province and code[0][1] == region:
                print(code)
                break
            else:
                print("This postal code is invalid and cannot be used. Please enter in an accurate code.")
                continue

def fun_3(province, region):
    """
    find out the characters in the list and print the corresponing dictionary key to the value
    get rid of whitespace
    cehck for 6 charachtesrs
    """


def main():
    pass

if __name__ == '__main__':
    main()