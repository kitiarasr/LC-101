#$ python caesar.py
#Type a message:
#Hello, World!
#Rotate by:
#5
#Mjqqt, Btwqi!

message = input("Type a message:")
list_message = list(message)             #convert to list to work with easier, replace each letter then join
rotation = int(input("Rotate by:"))
tempVal = 0
for (index, val) in enumerate(list_message):
    val = ord(val)                       #convert to ascii decimal value

    if val < 122 and val > 97:    #if ascii is greater than z or Z, then modulo

        val = val + rotation
        val = val % 26
        if val > 97

    elif val > 65 and val < 90:   #if asci is less than a or A, then modulo different way
        val = val + rotation
        val = val % 26

    val = chr(val)                       #convert back to ascii
    list_message[index] = val
print("".join(list_message))

a = new object
