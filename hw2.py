input_word = input("Write your word: ")
len_of_word = len(input_word)
index_for_print = len_of_word // 2
if len_of_word % 2 == 0:
    print(f"Result: {input_word[index_for_print-1]}{input_word[index_for_print]}")
else:
    print(f"Result: {input_word[index_for_print]}")