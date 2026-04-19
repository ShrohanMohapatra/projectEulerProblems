// LinkedListFunctions.h

#include<cassert>

using namespace std;

struct linkedList{
	unsigned int dataNumber;
	unsigned int index;
	linkedList* nextNode;
};

void createFreshLinkedList(linkedList* inputHeader, unsigned int x){
	inputHeader->dataNumber = x;
	inputHeader->index = 1;
	inputHeader->nextNode = nullptr;
}

void addNodeLinkedList(linkedList* inputHeader, unsigned int x){
	linkedList* freshNode;
	freshNode->dataNumber = x;
	freshNode->index = inputHeader->index + 1;
	freshNode->nextNode = inputHeader;
	inputHeader = freshNode;
}

linkedList* deleteLinkedList(linkedList* inputHeader, unsigned int indexPtr){
	assert(1 < indexPtr && indexPtr <= inputHeader->index);
	linkedList* deletedNode;
	linkedList* prevNode = inputHeader;
	linkedList* traverseNode = inputHeader;
	unsigned int maxIndex = inputHeader->index;
	unsigned int scanningIndexPtr = maxIndex;
	while(scanningIndexPtr >= indexPtr){
		prevNode = traverseNode;
		traverseNode = traverseNode->nextNode;
		scanningIndexPtr = scanningIndexPtr - 1;
	}
	prevNode->nextNode = traverseNode->nextNode;
	traverseNode->nextNode = nullptr;
	deletedNode = traverseNode;
	return deletedNode;
}

void reverseLinkedList(linkedList* inputHeader){
	linkedList* firstBufferHeader;
	linkedList* secondBufferHeader;
	unsigned int lastEndCounter = inputHeader->index;
	while(lastEndCounter >= 0){
		firstBufferHeader = deleteLinkedList(inputHeader, lastEndCounter);
		addNodeLinkedList(secondBufferHeader, firstBufferHeader->dataNumber);
		lastEndCounter = lastEndCounter - 1;
	}
	inputHeader = secondBufferHeader;
	secondBufferHeader = nullptr;
}
