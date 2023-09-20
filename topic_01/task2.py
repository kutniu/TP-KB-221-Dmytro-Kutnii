#Додавання рядків:

text1 = "hi "
text2 = "man"
result = text1 + text2
print(result)

#Розділення рядка на слова:
text = "this is my example"
words = text.split()
print(words)

#Заміна тексту
text = "replace something"
new_text = text.replace("something", "text")
print(new_text)

#Перетворення на великі літери
text = "big letters"
uppercase_text = text.upper()
print(uppercase_text)

#Перетворення на маленькі літери:
text = "SMALL LETTERS"
lowercase_text = text.lower()
print(lowercase_text)

#Перевірка, чи починається рядок з певного слова:
text = "My name is"
starts_with_word = text.startswith("My")
print(starts_with_word)

#Перевірка, чи закінчується рядок певним словом:
text = "My name is"
ends_with_word = text.endswith("is")
print(ends_with_word)

#Пошук підрядка у тексті:
text = "Цей текст містить слово"
substring = "слово"
found = substring in text
print(found)

#Визначення довжини рядка:
text = "Ця стрічка має довжину"
length = len(text)
print(length)

#Вилучення пробілів з початку і кінця рядка:
text = "   With spases   "
trimmed_text = text.strip()
print(trimmed_text)

#Повторення рядка:
text = "Repeat. "
repeated_text = text * 3
print(repeated_text)

#Форматування рядка:
name = "Dmytro"
age = 58
formatted_text = f"My name is {name}. Im {age} years old."
print(formatted_text)

#Видалення символу з рядка:
text = "Delete 'this' symbol"
removed_char_text = text.replace("'", "")
print(removed_char_text)

#Перетворення числа в рядок:
number = 42
text = str(number)
print(text)

#Визначення позиції підрядка у тексті:
text = "This word is"
substring = "word"
position = text.find(substring)
print(position)

#Перетворення рядка у список символів:
text = "String"
char_list = list(text)
print(char_list)

#Переведення першої літери у велику:
text = "big the firdt letter"
capitalized_text = text.capitalize()
print(capitalized_text)

#Розділення рядка на підрядки за роздільником:
text = "dhidjkfsjgo, jiegiuer"
substrings = text.split(",")
print(substrings)

#Перевірка, чи складається рядок лише з букв:
text = "kfdsfshfdjsmn"
is_alpha = text.isalpha()
print(is_alpha)

#Перевірка, чи складається рядок лише з цифр:
text = "874554679845"
is_digit = text.isdigit()
print(is_digit)

#Перевірка, чи складається рядок лише з пробілів:
text = "        "
is_whitespace = text.isspace()
print(is_whitespace)

#Перевірка, чи починається рядок цифрою:
text = "42  jhfhesk fj fkhefs ius"
starts_with_digit = text[0].isdigit()
print(starts_with_digit)

#Визначення кількості входжень підрядка в рядок:
text = "my fjiuewfjdksg enfisheig ehsgsip my klefj my"
substring = "my"
count = text.count(substring)
print(count)

#Визначення, чи є рядок числом з плаваючою точкою:
text = "3.14"
is_float = text.replace(".", "", 1).isdigit()
print(is_float)