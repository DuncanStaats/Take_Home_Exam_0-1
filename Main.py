def fun_1(province, region):
    province = {"Newfoundland": "A", "Nova Scotia": "B", "Prince Edward Island": "C", "New Brunswick": "E",
                "Quebec": "GHJ", "Ontario": "KLMNP", "Manitoba": "R", "Saskatchewan": "S","Alberta": "T", 
                "British Columbia": "V", "Nunavat": "X", "Northwest Territories": "X", "Yukon": "Y"}
    region = {"Urban": "123456789", "Rural": "0"}
    return province, region

def fun_2(province, region):
    while True: 
        code = input("Enter in your postal code: ")
        code = code.split()
        if code[0][0] == province.values() and code[0][1] == region.values():
            break
        else:
            print("This postal code is invalid and does not have the proper order of characters. Please enter in an accurate code.")
            continue
""" 
check after asked and before split, if code length == 6 then break, else prompt user to enter in the correct amount of characters.
check if it is: character digit, charctaer, space, digit, charcter, digit
"""

def fun_3(province, region):
    pass
"""
find out the characters in the list and print the corresponing dictionary key to the value
"""


def main():
    fun_2(province=any, region=any)
    fun_3(province=any, region=any)

if __name__ == '__main__':
    main()