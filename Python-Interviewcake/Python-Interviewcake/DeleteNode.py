class linkedList:
	def __init__(self, arrayToConvert):
		self.head = None
		arrLen = len(arrayToConvert)

		if arrLen == 0:
			return

		self.head = linkedListNode(arrayToConvert[0])
		currentItem = self.head
		for index in range(1, arrLen):
			currentItem.next = linkedListNode(arrayToConvert[index])
			currentItem = currentItem.next

	def generateList(self):
		if self.head is None:
			return
		current = self.head
		while current is not None:
			yield current
			current = current.next

	def findValue(self, valueToFind):
		for item in self.generateList():
			if item.value == valueToFind:
				return item
		return None
	def delNode(self, nodeToDel):
		if nodeToDel.next is None:

		nodeToDel.value = 

class linkedListNode:
	def __init__(self, value):
		self.value = value
		self.next = None
