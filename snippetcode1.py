"""LIST"""
#assigning elements in a list
lst=[1,2,3,4,5]

# adding an element in the end of the list
lst.append(6)

#adding strings to the list
lst.extend('s')

#inserting elements at a particular index
# syntax: list.insert(index,value)
lst.insert(3,9)

print(lst)


"""TUPLE"""
#accessing elements from a tuple
tuple=(1,2,"wren",[6,4],3,5)

#to access elements which lie btw 2 indices
print(tuple[:2])

#to access an element from one index
print(tuple[2])

#to know the length of the tuple
print(len(tuple))

#to access a single element from a tuple inside a tuple
print(tuple[2][2])

#negative indexing
print(tuple[-4:-2])


"""DICTIONARY"""
#to delete elemets from the dictionary
dictionary={1:"harry",2:"hermoine",3:"ron",4:"draco",5:"medusa"}

#delete element at index 3
print(dictionary.pop(3))

#pops a random item
print(dictionary.popitem())

#clears the dictionary
print(dictionary.clear())

print(dictionary)






