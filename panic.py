phrase="Don't panic"

rlist= ["D","'","i","c"]


def remove_char(phrase, remove_list):
    plist = list(phrase)
    for element in remove_list:
        plist.remove(element)
    newphrase = ''.join(plist)
    return newphrase


output =list(remove_char(phrase, rlist))
output.pop()
output.insert(3,output.pop())
output.insert(2,output.pop(4))
coolphrase = ''.join(output)

print(coolphrase)

