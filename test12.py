ch = input("Enter any character : ")
line_length = int(input("Ënter the lenght of the line : "))
space_length = (line_length - len(ch)) * len(ch)

print(ch*line_length)
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch," "*space_length,ch,sep="")
print(ch*line_length)

"""
() --->2 characters * 20 = 40 characters

print() function is having two variables
end  ---->  by default end is having a NEW LINE character
sep  ---->  by default sep is having white space character
"""
