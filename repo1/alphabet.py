#print alphabetin lowercase
letter = 0

for letter in range(ord('z'),ord('a'),-1):
    print("{}".format(chr(letter)),end='')
#chr(letter) :converts the integer letter to its corresponding Unicode character.

#"{}".format(chr(letter)) :formats the Unicode character as a string 
#and replaces the {} in the string with the formatted value.