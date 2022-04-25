name="Zartab"
print(name)
print(type(name))
print(dir(name))

# String is enclosed in "some string" | 'some string'

# Multi Line String

paragraph="""
India is my country
All Indians are my brothers and sisters
I love my country
"""

print(paragraph)

# String in Python are like arrays

word="Kitkat"
print(word)
print(word[1])

print("Word[1:3]",word[1:3])

print("word[-5]:",word[-5])

# print("word[8]:",word[8])
# IndexError: string index out of range

print("word[0:20]:",word[0:20])

# Start from 1 of zero based till the length
print("word[1:]",word[1:])

# Start from 0 of zero based and end at 5 of one based
print("word[:5]",word[:5])

# Clone
print("word[:]",word[:])

# Length

print("Length:",len(word))

# Trimming -- strip()
word_with_spaces="   Hello World   "
print(word_with_spaces)
print("Length before strip",len(word_with_spaces))
word_with_spaces=word_with_spaces.strip()
print(word_with_spaces)
print("Length after strip",len(word_with_spaces))

# Casings
company='jp morgan'
print("Company:",company)
company=company.upper()
print("Company:",company)

sentence='I AM HAPPY TO BE HERE'
print("Sen:",sentence)

sentence=sentence.lower()
print("Sen:",sentence)

sentence=sentence.capitalize()
print("Sen with Capitalize:",sentence)

sentence=sentence.title()
print("Sen with Title:",sentence)

# Replacement

language="Jxvx"
print(language)

language=language.replace("x","a")
print(language)

# Split

line="1,Tom,IT,Dev,30000"
line2="Hello how are you"
print("O:",line)
print("o2",line2)
data=line.split(",")
data2=line2.split(" ")
print(data2)
print(data)
print(type(data))

# Format Functions

line="My name is Zartab, I am {} years old"
age=31

fline=line.format(age)
print("O:",line)
print("F:",fline)

line="My name is {} , I am {} years old"
name="Micheal"
age=35

fline=line.format(name,age)
print("O:",line)
print("F:",fline)


# Numbered Formatting

line="Hey I am a {0}, I train my {1}, {0} traines a {1}"
fline=line.format("Trainer","Trainee")
print("O:",line)
print("F:",fline)

# Named Formatting

line="Hey I am a {trainer}, I train my {trainee}, {trainer} traines a {trainer}"
fline=line.format(trainer="Trainer",trainee="Trainee")
print("O:",line)
print("F:",fline)

# Count
name='Zartab'
a_count=name.count('a')
print("Count of a in",name,'is',a_count)

# Starts and Ends with

print("Starts with z",name.startswith("z"))
print("Starts with Z",name.startswith("Z"))
print("Starts with a",name.startswith("a"))
print("Starts with Zar",name.startswith("Zar"))
print("Ends with b",name.endswith("b"))
print("Ends with B",name.endswith("B"))
print("Ends with x",name.endswith("x"))
print("Ends with tab",name.endswith("tab"))

# Escape Characters
# \n -- new line
# \t -- tab
# \\ - Backslash
# \" - Double Quotes

text="This is a backslash \\"
print(text)
text="These are two  backslashes  \\\\"
print(text)
text="I work at \"JP Morgan\""
print(text)

line="Python does support object orientation"

line=line.lower()

object_in_line="object" in line
print("Is object in line",object_in_line)


