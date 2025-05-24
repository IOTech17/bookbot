def count_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def character_count(text):
    character_count ={}
    characters = text.lower()
    for character in characters:
        if character not in character_count:
           character_count[character] = 0
        character_count[character] += 1
    return character_count

def sort_on(dict):
    return dict["num"]

def beautify_report(character_count_result):
    dict_list = []
    for character in character_count_result:
        if character.isalpha():
           count = character_count_result[character]
           dict_list.append({"char": character, "num": count})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list