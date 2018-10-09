dict= {
"class" : "Astr 119",
"prof"  : "Brant",
"awesomeness" : 10
}
print(type(dict))

course = dict["class"]
print(course)

dict["awesomeness"] += 1

print(dict)

for x in dict.keys():
	print(x, dict[x])