def fun_1():
    province = {
        "Newfoundland": ["A"], 
        "Nova Scotia": ["B"], 
        "Prince Edward Island": ["C"], 
        "New Brunswick": ["E"],
        "Quebec": ["G", "H", "J"], 
        "Ontario": ["K", "L", "M", "N", "P"], 
        "Manitoba": ["R"], 
        "Saskatchewan": ["S"],
        "Alberta": ["T"], 
        "British Columbia": ["V"], 
        "Nunavut": ["X"], 
        "Northwest Territories": ["X"], 
        "Yukon": ["Y"]
    }
    return province

def fun_2(province):
    check_1 = {char for chars in province.values() for char in chars}
    
    while True: 
        code = input("Enter your postal code: ")
        code = code.strip()
        code = code.title()
        
        if len(code) == 7 and code[3] == ' ':
            if code[0] in check_1:
                region = "Urban" if code[1] != '0' else "Rural"
                name = next(name for name, chars in province.items() if code[0] in chars)
                print(f"The postal code is for a {region} region in {name}.")
                break
            else:
                print("Invalid starting character. Please enter a valid postal code.")
        else:
            print("Incorrect format. It should be: Letter-Digit-Letter Space Digit-Letter-Digit.")

def main():
    province = fun_1()
    fun_2(province)

if __name__ == '__main__':
    main()