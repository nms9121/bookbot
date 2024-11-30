def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    # print(file_contents)
    words = file_contents.split()
    # print(len(words))

    char_dict = {}
    for w in words:
        for c in w:
            c = c.lower()
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
    # print(char_dict)
    # return char_dict

    init_str = f"--- Begin report of {path_to_file} ---"
    ovrview_str = f"{len(words)} words found in the document"
    print(init_str)
    print(ovrview_str)
    print("\n")

    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

    for c in sorted_dict:
        if c.isalpha():
            print(f"The '{c}' character was found {char_dict[c]} times")
    print("--- End report ---")

main()