def get_longer_word(word1: str, word2: str) -> str:
    i, j = len(word1), len(word2)
    if i < j:
        return word2
    elif i > j:
        return word1
    pass

    return word1



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
