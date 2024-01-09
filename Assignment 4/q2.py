"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""


class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # Start writing your code.
        if self.head==None:
            self.tail=Node(data,None)
            self.head=self.tail
        else:
            self.tail.pointer=Node(data,None)
            self.tail=self.tail.pointer
        self.size+=1
        # End writing your code.

# class ListQueue:
#     def __init__(self):
#         self.size=0
#         self.head=None
#         self.tail=None
#     def __len__(self):
#         return self.size
#     def is_empty(self):
#         return self.size==0
#     def enqueue(self,e):
#         new=Node(e)
#         self.tail.pointer=new
#         self.tail=self.tail.pointer
#         self.size+=1
#     def dequeue(self):
#         if self.is_empty():
#             print('The Queue is empty.')
#             return 
#         a=self.head.element
#         self.head=self.head.pointer
#         self.size-=1
#         return a

# def printList(node):
#     while node!=None:
#         print(node.element,end=' ')
#         node=node.pointer

def getTail(node):
    if node==None:
        print('The List is empty.')
    else:
        while node.pointer!=None:
            node=node.pointer
        return node #退出来的是最下面那个了

def quick_sort(node):
    # Start writing your code.
    # print('Called                  Called')
    if node == None:
        # print()
        return None
    elif node.pointer == None:
        return node
    else:
        # count=count_node(node)
        p=node.pointer
        # print(p.element,p.pointer.element)
        node.pointer=None
        # print(p.element,p.pointer.element)
        smallnode=None
        smallhead=None
        bignode=None
        bighead=None
            # print(type(p))
        while p!=None:
            if node.element > p.element:  #小的
                # printList(p)
                # print(' ')
                # print(p.element,p.pointer)
                if smallnode==None:
                    smallnode=Node(p.element,None)
                    smallhead=smallnode  #存下小list的头
                    smallnode.pointer=None
                    # print(smallhead.element)
                elif smallnode!=None:
                    smallnode.pointer=Node(p.element,None)
                    smallnode=smallnode.pointer
                    smallnode.pointer=None
                p=p.pointer
            elif node.element <= p.element: #大的
                if bignode==None:
                    bignode=Node(p.element,None)
                    bighead=bignode  #存下大list的头
                    bignode.pointer=None
                elif bignode!=None:
                    bignode.pointer=Node(p.element,None)
                    bignode=bignode.pointer
                    bignode.pointer=None
                p=p.pointer
        try:
            theVeryFirst=quick_sort(smallhead)
            getTail(theVeryFirst).pointer=node
            node.pointer=quick_sort(bighead)
        except:
            theVeryFirst=node
            node.pointer=quick_sort(bighead)


        return theVeryFirst
    # End writing your code.


# We will utilize the code similar to the following to check your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,5]  # An example.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    print('The number of nodes in test_list is:')
    p = quick_sort(first_node)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)