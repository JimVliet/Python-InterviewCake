from DeleteNode import *
linkedListNew = linkedList([1,2,3,4])
nodeToDel = linkedListNew.findValue(3)

for item in linkedListNew.generateList():
	print(item.value)