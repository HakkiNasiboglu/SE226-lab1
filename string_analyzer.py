from string_package import reverse_string,capitalize_words,remove_punctuation
from string_package import count_words,count_characters,average_word_length
s = input("Enter a sentence:")

reversed = reverse_string(s)
print(capitalize_words(reversed))
print(remove_punctuation(s))
print(count_words(s))
print(count_characters(s))
print(average_word_length(s))
