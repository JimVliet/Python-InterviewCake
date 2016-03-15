import random
def in_place_list_shuffle(listToShuffle):
	listLength = len(listToShuffle)
	for index, element in enumerate(listToShuffle):
		randomNumb = random.randint(0, listLength-1)
		listToShuffle[index] = listToShuffle[randomNumb]
		listToShuffle[randomNumb] = element
	return listToShuffle