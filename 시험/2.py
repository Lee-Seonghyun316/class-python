text = input()
list_text = list(text)
print(list_text)

inverse = []
for i in range(len(list_text)):
    inverse.append(list_text[len(list_text)-1-i])
print(inverse)

text = "".join(inverse)
print(text)
