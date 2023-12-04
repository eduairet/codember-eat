"""Challenge 05"""

import re


def main():
    """Main function"""

    with open("data/challenge_05.txt", "r", encoding="utf8") as f:
        read_data = f.read().splitlines()

    result = ""

    for line in read_data:
        entry_id, username, email, age, location = re.split(",", line)
        id_pattern = re.compile(r"^[0-9a-zA-Z]+$")
        username_pattern = re.compile(r"^[0-9a-zA-Z]+$")
        email_pattern = re.compile(r"^[A-Za-z0-9]+@[a-z]+\.[a-z]+$")
        age_pattern = re.compile(r"^\d+$")
        is_valid = (
            re.match(id_pattern, entry_id)
            and re.match(username_pattern, username)
            and re.match(email_pattern, email)
            and (age == "" or re.match(age_pattern, age))
            and (location == "" or isinstance(location, str))
        )
        if not is_valid:
            result += username[0]

    print(result)
    email_pattern = re.compile(r"^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$")


if __name__ == "__main__":
    main()
