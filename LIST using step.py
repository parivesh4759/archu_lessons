phrase="Don't panic"
plist=list(phrase)
slice=plist[1:8:1]
print(slice)
slice.insert(5,slice.pop(6))
slice.remove("'")
slice.insert(2,slice.pop(3))
print(''.join(slice))
print(plist)


