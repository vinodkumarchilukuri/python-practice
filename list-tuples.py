#list is mutable which can be changes eg: a= ["",""]
#tuple is immutable which cannot be changed eg: a=("","")

#list example
users = ["abc","def","ghi","xyz"]
users.append("jqk")  #to add new value
print(users)
users.remove("xyz")  #to remove new value
print(users)
print(users[1])  #to print particular element

#tuple example
users = ("abc","xyz")
print(users)


#output
# ['abc', 'def', 'ghi', 'xyz', 'jqk']
# ['abc', 'def', 'ghi', 'jqk']
# def
# ('abc', 'xyz')
