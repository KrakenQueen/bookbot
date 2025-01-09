def main():
    char_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for char in file_contents:
            if char.isalpha():
                if char.lower() in char_count:
                    char_count[char.lower()] += 1
                else:
                    char_count[char.lower()] = 1
    # To sort by keys (alphabetically):
    sorted_chars = dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
    print("--- Character Counts in Frankenstein ---")
    for char, count in sorted_chars.items():
        print(f"The '{char}' character was found {count} times")   
main()