"""Challenge 3"""


def is_valid_key(policy, key, password):
    """Check if a key is valid according to the policy"""
    min_count, max_count = policy.split("-")
    min_count = int(min_count)
    max_count = int(max_count)
    count = [*password].count(key)
    return min_count <= count <= max_count


def count_valid_keys(data):
    """Count the number of valid keys"""
    invalid_count = 0
    for line in data:
        policy, key, password = line.split(" ")
        key = key.replace(":", "")
        if invalid_count == 12:
            return password
        if not is_valid_key(policy, key, password):
            invalid_count += 1


def main():
    """Main function"""
    with open("data/challenge_03.txt", "r", encoding="utf8") as f:
        read_data = f.read().splitlines()
    print(count_valid_keys(read_data))


if __name__ == "__main__":
    main()
