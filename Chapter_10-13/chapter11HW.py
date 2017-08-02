







def sort_contacts(contacts):
    newList = []
    sorted_keys = list(contacts)                   #make a list of keys w/o values
    sorted_keys.sort()                             #sort the keys
    for sKey in sorted_keys:
        for cKey, cValue in contacts.items():
            if sKey == cKey:                       #if key matches with contact key, add key (converted to tuple
                newList.append((cKey,) + cValue)   #tuple() method doesnt work here, I get single characters
                                                   #tuple way: I can convert cValue to list, add cKey to list, then convert list to tuple.
    print(newList)


sort_contacts(({'Summitt, Pat': ('1-865-355-4320', 'pat@greatcoaches.com'), 'Rudolph, Wilma': ('1-410-5313-584', 'wilma@olympians.com')}))




''' # Tuple() conversion method
def sort_contacts(contacts):
    newList = []
    sorted_keys = list(contacts)
    sorted_keys.sort()   #i have my keys here
    for key in sorted_keys:
        for akey, value in contacts.items():
            if key == akey:
                temp = list(value)
                temp.insert(0, key)
                newList.append(tuple(temp))

    return newList

'''
