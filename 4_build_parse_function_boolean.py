'''
Created on Aug 10, 2018

@author: Brad Bosak

This function was modified to handle boolean statements.

Note, I was unable to use the import function to import the Stack and
binary tree classes, so I just pasted them into my program with the appropriate
credit due to those authors
'''

import operator

class Stack:
    # Bradley N. Miller, David L. Ranum
    # Introduction to Data Structures and Algorithms in Python
    # Copyright 2005
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
class BinaryTree:
    # Bradley N. Miller, David L. Ranum
    # Introduction to Data Structures and Algorithms in Python
    # Copyright 2005
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.
    """    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self,):
        return self.key

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)


    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def printexp(self):
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printexp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printexp()
            print(')', end=' ')

    def postordereval(self):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        res1 = None
        res2 = None
        if self.leftChild:
            res1 = self.leftChild.postordereval()  #// \label{peleft}
        if self.rightChild:
            res2 = self.rightChild.postordereval() #// \label{peright}
        if res1 and res2:
            return opers[self.key](res1,res2) #// \label{peeval}
        else:
            return self.key

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    if tree.leftChild:
        print('(', end=' ')
        printexp(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.rightChild:
        printexp(tree.getRightChild())
        print(')', end=' ') 

def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())  #// \label{peleft}
        res2 = postordereval(tree.getRightChild()) #// \label{peright}
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2) #// \label{peeval}
        else:
            return tree.getRootVal()

def height(tree):
    if tree == None:
        return -1
    else:
        return 1 + max(height(tree.leftChild),height(tree.rightChild))

def buildParseTree(fpexp):
    fplist = fpexp.split()           #splits new list to create list of characters
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['==', '!=', '>', '<', '<=', '>=', ')']: #boolean operators and right paren
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['==', '!=', '>', '<', '<=', '>=']:          #boolean operators
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'!=':operator.is_not, '==':operator.is_, '>':operator.gt,  #new batch of operators
             '<':operator.lt, '<=':operator.le, '>=':operator.ge}       #to accommodate for booleans

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
def main():                                     #main function to demonstrate boolean expression evaluations
    pt = buildParseTree("( 6 >= 6 )")
    print("Posting the order of the first parse tree as a demonstration:")
    pt.postorder()  #show the order of the first parse tree as an example
    pt1 = buildParseTree("( 45 < 93 )")  #a variety of boolean statements to build and evaluate
    pt2 = buildParseTree("( 85 > 99 )")
    pt3 = buildParseTree("( 55 == 55 )")
    pt4 = buildParseTree("( 6 != 6 )")
    pt5 = buildParseTree("( 4567 <= 357567 )")
    print("Evaluate 6 >= 6: ",evaluate(pt))
    print("Evaluate 45 < 93: ",evaluate(pt1))
    print("Evaluate 85 > 99: ",evaluate(pt2))
    print("Evaluate 55 == 55: ",evaluate(pt3))
    print("Evaluate 6 != 6: ",evaluate(pt4))
    print("Evaluate 4567 <= 357567: ",evaluate(pt5))
    
main()