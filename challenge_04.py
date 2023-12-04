"""Challenge 04"""

from collections import Counter


def main():
    """Main function"""
    with open("data/challenge_04.txt", "r", encoding="utf8") as f:
        read_data = f.read().splitlines()
    true_docs = 0
    for line in read_data:
        file, checksum = line.split("-")
        singles = "".join(
            letter for letter, count in Counter(file).items() if count == 1
        )
        if singles == checksum:
            true_docs += 1
        if true_docs == 32:
            return checksum
        if true_docs == 13:
            return file
    return None


if __name__ == "__main__":
    print(main())
