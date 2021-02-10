def unique_char(word):
    listword = []
    listword[:0] = word
    print(listword)
    for index in range(len(listword)):
        if listword.count(listword[index]) == 1:
            return index
        elif index == len(listword) - 1:
            return -1


word = "alphabet"
print(unique_char(word))
word = "barbados"
print(unique_char(word))