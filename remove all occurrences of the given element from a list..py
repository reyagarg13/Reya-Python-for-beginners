mylist = eval(input("Enter all the elements in the list:"))
r_item = int(input("Enter the re-occurring element to be removed:"))

print("Original List:" , mylist)

for item in mylist:
	if(item == r_item):
		mylist.remove(r_item)

print("New List:" , mylist)
