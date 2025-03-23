class Node:
    def __init__(self, value):
        self.value=value
        self.next=None




class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def print_linkedlist(self):
        current=self.head
        while current:
            print (current.value)
            current=current.next




    def add_first(self, value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def add_last(self, value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1




    def insert(self, index, value):
        if index==0:
            self.add_first(value)
            return
        if index>=self.length:
            self.add_last(value)
            return
    
        new_node=Node(value)
        current=self.head
        for i in range(index-1):
            current=current.next




        new_node.next=current.next
        current.next=new_node




        self.length+=1




    def remove_first(self):
        if (self.length>1):
            self.head=self.head,next
        if self.length==1:
            self.head=None
            self.tail=None
        if self.length!=0:
            self.length-=1




    def remove_last(self):
        if self.length>1:
            current=self.head
            for i in range(self.length-2):
                current=current.next
            self.tail=current
            self.tail.next=None
        if self.length==1:
            self.head=None
            self.tail=None
        if self.length!=0:
            self.length-=1




    def remove(self, index):
        if index==0:
            self.remove_first()
            return
        if index>=self.length:
            self.remove_last()
            return
    
        current=self.head
        for i in range(index-1):
            current=current.next
        current.next=current.next.next
        self.length-=1




  #удаление всех вхождений value
    def remove_value(self, value):
        if(self.head.value == value):
            self.remove_first()


        if(self.tail.value == value):
            self.remove_last()


        current = self.head
        while current and current.next:
            if(current.next.value == value):
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
  




  #удаление всех дубликатов и возврат ового
  #связаного списка
    def remove_dublicate(self):
        new_linked_list = LinkedList()
        copied = set()
        current = self.head


        while current:
            if(current.value in copied):
                current = current.next
            else:
                copied.add(current.value)
                new_linked_list.add_last(current.value)
                current = current.next
        new_linked_list.print_linkedlist()




  #итератор для циклического прохода
    def __iter__(self):
      return self




  #слияние отсортированных связаных списков
  #возврат нового списка
  #(нельзя использовать встроенную сотртировку)
    def merge(linked1, linked2):
        merged_list = LinkedList()
        current1 = linked1.head
        current2 = linked2.head

        while current1 and current2:
            if current1.value < current2.value:
               merged_list.add_last(current1.value)
               current1 = current1.next
            else:
               merged_list.add_last(current2.value)
               current2 = current2.next
        
        while current1:
            merged_list.add_last(current1.value)
            current1 = current1.next

        while current2:
            merged_list.add_last(current2.value)
            current2 = current2.next

        return merged_list
 
    @staticmethod
    def compression(linked_list):
        current = linked_list.head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
                linked_list.length -= 1
            else:
                current = current.next
        return linked_list
    




linked_list=LinkedList()
linked_list.add_first(5)
linked_list.add_first(4)
linked_list.add_first(8)
linked_list.add_last(10)
linked_list.insert(0, 99)
linked_list.insert(100, 99)
linked_list.insert(2, 99)
linked_list.remove_first()
linked_list.remove_first
linked_list.print_linkedlist()


