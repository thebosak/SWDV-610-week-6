'''
Created on Aug 9, 2018

@author: Brad Bosak

This python file is for both question 1 and 2.  I put them in the same program to
generate the random list once so both the first binary heap tree and second one are both
using the same list.

I have named the functions "question1" and "question2" to correspond to the
assignment questions.

Note, I was unable to use the import function to import the BinHeap class, so I pasted it
into my program with the appropriate credit due to those authors.

'''

import random

class BinHeap:
    # Bradley N. Miller, David L. Ranum
    # Introduction to Data Structures and Algorithms in Python
    # Copyright 2005
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    
    def showHeapList(self):
        return self.heapList

def generateRandomList():            #new function to generate a random list of integers
    randomlist = []
    for i in range(0,8):             #list has 8 integers in it
        randomlist.append(random.randint(0,10))    #list can be from 0 to 9
    return randomlist

def question1():
    list = generateRandomList()
    print("method1 list is ",list)
    bigOleHeap = BinHeap()
    for element in list:
        bigOleHeap.insert(element)   #using the insert method, insert each element, one at a time
    print("The Heap Tree for method one is ", bigOleHeap.showHeapList(), "\n")
    return list

def question2(list):
    print("method2 list is also",list)
    bigOleHeap = BinHeap()
    bigOleHeap.buildHeap(list)       #using the buildHeap method, create the binary heap tree with the list all at once
    print("The Heap Tree for method two is ", bigOleHeap.showHeapList())
    
question2(question1())               #calling this function in this way will use the
                                     #same random list for both question 1 and question 2