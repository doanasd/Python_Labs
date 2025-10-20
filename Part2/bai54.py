def format_word_list(words):
    if not words:
        return ""
    if len(words) == 1:
        return words[0]

    formatted_string = ", ".join(words[:-1])
    formatted_string += " and " + words[-1]
    return formatted_string

words = []
print("Nhập các từ, nhập dòng trống để kết thúc:")
while True:
    word = input()
    if not word:
        break
    words.append(word)

print("Kết quả:", format_word_list(words))
