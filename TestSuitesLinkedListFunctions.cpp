// TestSuitesLinkedListFunctions.cpp

#include"LinkedListFunctions.h"
#include<cassert>
#include<array>
#include<ctime>

using namespace std;

void linkedListExample1(){
	linkedList* exampleLinkedList;
	linkedList* bufferForDeletedNode;
	linkedList* traverseList;
	array<unsigned int, 10> positiveIntegerArray;
	int k;
	for(k = 0; k < 5; k++){
		positiveIntegerArray[k] = 5-k;
	}
	addNodeLinkedList(exampleLinkedList, 1);
	addNodeLinkedList(exampleLinkedList, 2);
	addNodeLinkedList(exampleLinkedList, 3);
	addNodeLinkedList(exampleLinkedList, 4);
	addNodeLinkedList(exampleLinkedList, 5);
	traverseList = exampleLinkedList;
	assert(traverseList->dataNumber == positiveIntegerArray[4]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[3]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[2]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[1]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[0]);
	traverseList = traverseList->nextNode;
	assert(&traverseList == nullptr);
	bufferForDeletedNode = deleteLinkedList(exampleLinkedList, 4);
	traverseList = exampleLinkedList;
	assert(traverseList->dataNumber == positiveIntegerArray[4]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[2]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[1]);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == positiveIntegerArray[0]);
	traverseList = traverseList->nextNode;
	assert(&traverseList == nullptr);
}

void linkedListExample2(){
	linkedList* listHeader;
	linkedList* bufferForDeletedNode;
	linkedList* traverseList;
	addNodeLinkedList(listHeader, 12);
	addNodeLinkedList(listHeader, 25);
	addNodeLinkedList(listHeader, 45);
	addNodeLinkedList(listHeader, 70);
	addNodeLinkedList(listHeader, 75);
	addNodeLinkedList(listHeader, 85);
	addNodeLinkedList(listHeader, 100);
	addNodeLinkedList(listHeader, 120);
	traverseList = listHeader;
	assert(traverseList->dataNumber == 120);
	assert(traverseList->index == 1);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 100);
	assert(traverseList->index == 2);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 85);
	assert(traverseList->index == 3);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 75);
	assert(traverseList->index == 4);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 70);
	assert(traverseList->index == 5);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 45);
	assert(traverseList->index == 6);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 25);
	assert(traverseList->index == 7);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 12);
	assert(traverseList->index == 8);
	bufferForDeletedNode = deleteLinkedList(traverseList, 3);
	assert(bufferForDeletedNode->dataNumber == 85);
	bufferForDeletedNode = deleteLinkedList(traverseList, 5);
	assert(bufferForDeletedNode->dataNumber == 45);
	assert(traverseList->dataNumber == 120);
	assert(traverseList->index == 1);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 100);
	assert(traverseList->index == 2);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 75);
	assert(traverseList->index == 3);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 70);
	assert(traverseList->index == 4);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 25);
	assert(traverseList->index == 5);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 12);
	assert(traverseList->index == 6);
	traverseList = traverseList->nextNode;
	assert(&traverseList == nullptr);
}

void linkedListExample3(){
	linkedList* exampleLinkedList;
	linkedList* firstHeader;
	linkedList* secondHeader;
	linkedList* secondLastHeader;
	linkedList* lastHeader;
	addNodeLinkedList(exampleLinkedList, 85);
	addNodeLinkedList(exampleLinkedList, 80);
	addNodeLinkedList(exampleLinkedList, 35);
	addNodeLinkedList(exampleLinkedList, 140);
	addNodeLinkedList(exampleLinkedList, 120);
	addNodeLinkedList(exampleLinkedList, 100);
	addNodeLinkedList(exampleLinkedList, 75);
	addNodeLinkedList(exampleLinkedList, 70);
	addNodeLinkedList(exampleLinkedList, 45);
	addNodeLinkedList(exampleLinkedList, 25);
	addNodeLinkedList(exampleLinkedList, 12);
	firstHeader = exampleLinkedList;
	secondHeader = exampleLinkedList->nextNode;
	secondLastHeader = exampleLinkedList;
	lastHeader = exampleLinkedList;
	while(&(lastHeader->nextNode) != nullptr){
		secondLastHeader = lastHeader;
		lastHeader = lastHeader->nextNode;
	}
	assert(firstHeader->dataNumber == 12);
	assert(secondHeader->dataNumber == 25);
	assert(secondLastHeader->dataNumber == 80);
	assert(lastHeader->dataNumber == 85);
}

void linkedListExample4(){
	linkedList* exampleLinkedList;
	linkedList* traverseList;
	
	addNodeLinkedList(exampleLinkedList, 85);
	addNodeLinkedList(exampleLinkedList, 80);
	addNodeLinkedList(exampleLinkedList, 35);
	addNodeLinkedList(exampleLinkedList, 140);
	addNodeLinkedList(exampleLinkedList, 120);
	addNodeLinkedList(exampleLinkedList, 100);
	addNodeLinkedList(exampleLinkedList, 75);
	addNodeLinkedList(exampleLinkedList, 70);
	addNodeLinkedList(exampleLinkedList, 45);
	addNodeLinkedList(exampleLinkedList, 25);
	addNodeLinkedList(exampleLinkedList, 12);
	
	traverseList = exampleLinkedList;
	assert(traverseList->dataNumber == 12);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 25);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 45);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 70);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 75);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 100);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 120);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 140);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 35);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 80);
	traverseList = traverseList->nextNode;
	assert(traverseList->dataNumber == 85);
	traverseList = traverseList->nextNode;
	assert(&traverseList == nullptr);

	// reverseLinkedList(exampleLinkedList);
}

int main(){
	linkedListExample1();
	linkedListExample2();
	linkedListExample3();
	linkedListExample4();
	return 0;
}