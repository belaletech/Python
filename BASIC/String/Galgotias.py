text="Galgotias E Cell lunch Pad feb Event Galgotias univerity"
# Upper() functon to convert String to upper case
print("Converted String into uppercase=",text.upper())

#lower() function to convert String to lower case
print("Converted String into Lowercase=",text.lower())

#converts the first character to uppercase and rest to lower case
print("Converted String into Title=",text.title())

#original string never change
print(text)


# Converts the first character to the string a capital(uppercase) letter
print("Convert String into capital(uppercase) letter",text.capitalize())

# Casefold=implements caseless string matching
print("Case Fold=",text.casefold())

# Center=pad the String with the specified character.
print("Center String function=",text.center(25,'#')) 

#count() Resturn the number of occurence of a substring in the string.
print("Number of String in Statement= ",text.count("Galgotias"))