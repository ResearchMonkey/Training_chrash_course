import this


persons_name = "john candy"

print('Hello {}, would you like to learn some Python today?'.format(persons_name.title()))

name = 'ada lovelace'
case = 'Example of case'
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' '+last_name
print(name.title())
print(name.lower())
print(name.upper())
print(full_name.title())
print('Hello, '+full_name.title()+'!')

message = 'Hello, ' + full_name.title()+'!'
print(message)

print('Hello, '+full_name.title()+'\tI want to thank you')

print('Languages:\nPython\nC\nJava')
print('Languages:\n\tPython\n\tC\n\tJava')

favorite_language = 'Python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())

# how python handles Integers
print(2 + 3)
print(3-2)
print(2*3)
print(3/2)
print(3**2)
print(10**6)

# How python handles floats
print(2.1 + 3.2)
print(3.3-2.4)
print(2.5*3.6)
print(3.7/2.8)
print(3.9**2.10)
print(10.11**6.12)

age = 23
message = "Happy " + str(age) + 'rd Birthday!'
print(message)


quote = "I'll give you my gun when you pry it from my cold, dead hands"
speaker = 'Charlton Heston'

print(f'{speaker} once said "{quote}"'.format())

name_for_2_7 = "  jonny\n\tsilverhand  "
print(name_for_2_7)

print(name_for_2_7.lstrip())
print(name_for_2_7.rstrip())
print(name_for_2_7.strip().title())

# addition
print(5+3)
# subtraction
print(9-1)
# multiplication
print(2*4)
# division
print(16/2)

favorate_number = 7
print('My favorite number is {}!'.format(favorate_number))