def remove_fourth_character(word: str) -> str:
    new_word = word[:3]
    second_part = word[4:]
    
    new_message = new_word + second_part

    return new_message


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
