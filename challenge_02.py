"""
"#" Increases the numeric value by 1.
"@" Decreases the numeric value by 1.
"*" Multiplies the numeric value by itself.
"&" Prints the current numeric value.
"""

COMMANDS = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"


def main():
    """Main function"""
    number = 0
    for command in COMMANDS:
        if command == "#":
            number += 1
        elif command == "@":
            number -= 1
        elif command == "*":
            number *= number
        elif command == "&":
            print(number, end="")
        else:
            break


if __name__ == "__main__":
    main()
