# This is a course of which objective is to cover some challenges involving double linked lists in python
# From how to create them till how to solve nice tricky challenges with them

# 1. Creation of double linked list.
# Def: Double linked list (DLS) is a dynamic allocated structure that involves storage of data as specific memory addresses
# and a linkage between them. Therefor DLSs allow for connections with both previous node(data) and the next one.
# Create such a structure: make use of classes or functions or whatever you fancy
# classes implementation:
# - a dls has to have nodes
class Node:
    def __init__(self , value):
        self . value  = value   # assigning a value to the node
        self . next = None      # this is a pointer to the next node
        self . prev = None      # pointer to previous node
class DLS:
    def __init__(self):
        self . head = None # the head of the list is firstly none. Head is like a list tag
        self . tail = None # store the address of the last node appended so we have both limits of the lists
    def appending(self , value): # this is a local function of class DLS that will append values in the list, firstly the list is empty
        newNode = Node( value )
        # newNode called is address , newNode . value is value at newNode's address
        if self . head is None:   # or if not self . head: # no node in the list yet
            self . head = newNode
            return
        # now last node created is the self . head
        lastNode = self . head
        # iteration till we find the last node if head is no longer the last node , so more than 1 element in list
        while lastNode . next:   # is not None  , None being the ending tag of the list
            lastNode = lastNode . next #iterate
        # we are at the last node ---> linking
        lastNode . next = newNode
        newNode . prev = lastNode   # bidirectional linkage
        self . tail = newNode
    def displayNext(self):
        # the idea is to start on the head and to go next next next as long as we can and the current element is not None
        el = self . head
        while el:
            print( el . value , end="->" )
            el = el . next
        print( None )
    def displayPrev(self):
        # the idea is to start on the tail and to go prev prev prev as long as we can and the current element is not None
        el = self . tail
        while el:
            print( el . value , end="->" )
            el = el . prev
        print( None )

# create the object of DLS
dls = DLS()
# append some values in the list
dls . appending( 1 )
dls . appending( 2 )
dls . appending( "Echo" )
dls . appending( 3 )
dls . appending( "Zulu" )
dls . appending( 4 )
# display the list as next and prev
dls . displayNext()
dls . displayPrev()


# List rotation. Rotate with respect to next and prev a given nr of times. A list is given and an integer
def RotateNext( localDLS , nRot ):
    while nRot > 0:
        # last becomes first
        localDLS . tail . next = localDLS . head
        localDLS . head . prev  = localDLS . tail
        localDLS . head = localDLS . tail
        localDLS . tail = localDLS . tail . prev
        localDLS . tail . next = None
        localDLS . head . prev = None
        nRot -= 1
    localDLS . displayNext()
    localDLS . displayPrev()

#RotateNext( dls , 2 )

def RotatePrev( localDLS , nRot ):
    while nRot > 0:
        # first becomes last
        localDLS . head . prev = localDLS . tail
        localDLS . tail . next = localDLS . head
        localDLS . tail = localDLS . head
        localDLS . head = localDLS . head . next
        localDLS . tail . next = None
        localDLS . head . prev = None
        nRot -= 1
    localDLS . displayNext()
    localDLS . displayPrev()

#RotatePrev( dls , 3 )


# 3. Detect the center of a double linked list and if the dls has even or odd  nr of nodes
thirdList = DLS()
thirdList . appending( "Physics" )
thirdList . appending( "Maths" )
thirdList . appending( "Chemistry" )
thirdList . appending( "Biology" )
thirdList . appending( "Computer Science" )
thirdList . appending( "Applied Engineering" )
def DetectCenter_And_Oddity( localDLS ):
    localDLS . displayNext()
    nextIt = localDLS . head
    prevIt = localDLS . tail
    while True:
        #print( "checking" , nextIt . value , prevIt . value )
        if prevIt . prev == nextIt and nextIt . next == prevIt:
            return f"Even nr of nodes , middle: {nextIt.value} , {prevIt.value}"
        elif prevIt == nextIt or prevIt.next == nextIt:
            return f"Odd nr of nodes , middle: {prevIt.value}"
        else:
            pass
        prevIt = prevIt . prev
        nextIt = nextIt . next

print( DetectCenter_And_Oddity( thirdList ) )


# 4. Write a function that checks if the double linked list is a palidrome. Reads same with next display as with prev display
palindromelist = DLS()
for letter in 'lupul':
    palindromelist . appending( letter )
palindromelist . displayNext()
def DLS_Palindrom_Checker( localDLS ):
    rightP = localDLS . tail
    leftP = localDLS . head
    while True:
        if rightP . value != leftP . value:
            return "Not a palindrome"
        if rightP . prev == leftP and leftP . next == rightP:
            break
        if rightP == leftP:
            break
        rightP = rightP . prev
        leftP = leftP . next
    return "palindrome"

print( DLS_Palindrom_Checker( palindromelist ) )

# 5. Sorting a double linked list: ascending and descending
def Sorting_DLS_Ascending( dls ):
    i = dls.head
    while i is not None:
        j = i.next
        while j is not None:
            if j.value < i.value:
                i.value, j.value = j.value, i.value
            j = j.next
        i = i . next

    dls . displayNext()

dls = DLS()
dls . appending( 2 )
dls . appending( 1 )
dls . appending( 3 )
dls . appending( 0 )
dls . appending( 7 )
dls . appending( 6 )
dls . appending( 5 )
Sorting_DLS_Ascending( dls )