# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
overall_result = []
for i in range(1, nr_letters+1):
  letter_string = letters[random.randint(0,25)]
#   print(letter_string)
  overall_result.append(letter_string)
for i in range(1, nr_symbols+1):
  symbol_string = symbols[random.randint(0,len(symbols)-1)]
#   print(symbol_string)
  overall_result.append(symbol_string)
for i in range(1, nr_numbers+1):
  number_string = numbers[random.randint(0,len(numbers)-1)]
#   print(number_string)
  overall_result.append(number_string)
# print(overall_result)
random.shuffle(overall_result)
#Using a join function below to convert the list into string and joining the strings for removing '' from the arrary.
result = ''.join(map(str, overall_result))
print(f"Here is your password: {result}")