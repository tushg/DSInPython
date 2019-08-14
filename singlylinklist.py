#This class represents Node class
class node:

    def __init__(self, data):
        self.data = data
        self.next = None

# This class represents Linkedlist class
# It has append / push / display functionality
class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Create a new node
        new_node = node(data)

        # If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # Change the next of last node
        last.next = new_node

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node;

    def length(self):
        total=0
        cur = self.head
        while cur.next != None:
            total += 1
        return total

    # Utility function to print the linked LinkedList
    def printList(self):
        elems = []
        temp = self.head
        while (temp):
            elems.append(temp.data)
            temp = temp.next
        print(elems)


# Linked List demo
#Append Node at the end
my_list = linkedlist()
my_list.printList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print('Append node at the end of the list')
my_list.printList()

print('--------------------------------')

my_list1 = linkedlist()
my_list.push(12)
my_list.push(6)
my_list.push(11)
my_list.push(2)
print('Push the node in the list')
my_list.printList()




