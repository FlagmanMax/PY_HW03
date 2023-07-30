# Hw_02
# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
import operator

str_input = "This reference manual describes the Python programming language. It is not intended as a tutorial.\
While I am trying to be as precise as possible, I chose to use English rather than formal specifications for everything except syntax and lexical analysis. This should make the document more understandable to the average reader, but will leave room for ambiguities. Consequently, if you were coming from Mars and tried to re-implement Python from this document alone, you might have to guess things and in fact you would probably end up implementing quite a different language. On the other hand, if you are using Python and wonder what the precise rules about a particular area of the language are, you should definitely be able to find them here. If you would like to see a more formal definition of the language, maybe you could volunteer your time — or invent a cloning machine :-).\
It is dangerous to add too many implementation details to a language reference document — the implementation may change, and other implementations of the same language may work differently. On the other hand, CPython is the one Python implementation in widespread use (although alternate implementations continue to gain support), and its particular quirks are sometimes worth being mentioned, especially where the implementation imposes additional limitations. Therefore, you’ll find short “implementation notes” sprinkled throughout the text."
print(str_input)

str_input = str_input.strip(',.:-)')
word_array = str_input.split()
word_count = len(word_array)
print(f"Количество слов = {word_count}")

# Make dict
result = {}
for i in word_array:
    result[i.lower()] = result.setdefault(i.lower(), 0) + 1
# print(result)

# Sort it and print the first 10
sorted_tuples = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
print(*sorted_tuples[0:10:1], sep='\n')



