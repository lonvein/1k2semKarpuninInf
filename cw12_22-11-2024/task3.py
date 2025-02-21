'''
Есть односвязный список, в нем есть функции добавить элемент в произвольное место, 
удалить элемент по значению, распечатать список (для проверки правильности добавления и удаления), 
значения элементов списка ai целые числа, где i – итый элемент текущего списка. Для текущего 
состояния списка вычислить последовательность элементов ai – an, где n – последний элемент 
односвязного списка.
'''

class Node: 
    def __init__(self, data): 
        self.item = data 
        self.nref = None
#{'item': data, nref: None, pref: None}


class SingleLinkedList: 
    def __init__(self): 
        self.start_node = None

    def insert_in_emptylist(self, data): 
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
        else: 
            print("list is not empty")
            
    def insert_at_start(self, data): 
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
            print("node inserted") 
            return 
        new_node = Node(data) 
        new_node.nref = self.start_node 
        self.start_node = new_node
        
    def insert_at_end(self, data): 
        if self.start_node is None: 
            new_node = Node(data) 
            self.start_node = new_node 
            return
        n = self.start_node 
        while n.nref is not None: 
            n = n.nref 
        new_node = Node(data) 
        n.nref = new_node 
            
    def insert_after_item(self, x, data): 
        if self.start_node is None: 
            print("List is empty") 
            return 
        else: 
            n = self.start_node 
            while n is not None: 
                if n.item == x: 
                    break 
                n = n.nref 
            if n is None: 
                print("item not in the list") 
            else: 
                new_node = Node(data) 
                new_node.nref = n.nref 
                n.nref = new_node
    
    def insert_with_index(self, index, data):
        if self.start_node is None: 
            print("List is empty") 
            return 
        else: 
            n = self.start_node 
            for i in range(index - 1):
                n = n.nref
                if n is None: 
                    print("item not in the list")
                    return
            new_node = Node(data) 
            new_node.nref = n.nref
            n.nref = new_node
            
    def insert_before_item(self, x, data): 
        if self.start_node is None: 
            print("List is empty") 
            return 
        elif self.start_node is not None and self.start_node.item == x:
            new_node = Node(data) 
            new_node.nref = self.start_node 
            self.start_node = new_node
        else: 
            n = self.start_node 
            while n is not None: 
                if n.nref.item == x: 
                    break 
                n = n.nref 
            if n is None: 
                print("item not in the list") 
            else: 
                new_node = Node(data) 
                new_node.nref = n.nref
                n.nref = new_node
                
    def traverse_list(self): 
        if self.start_node is None: 
            print("List has no element") 
            return 
        else: 
            n = self.start_node 
            while n is not None: 
                print(n.item , " ") 
                n = n.nref
                
    def traverse_list_with_start(self, num): 
        if self.start_node is None: 
            print("List has no element") 
            return 
        else: 
            # счет элементов идет с 0, вывод идет с i по конечный элемент оба включительно
            n = self.start_node
            for i in range(num):
                n = n.nref
            while n is not None: 
                print(n.item , " ") 
                n = n.nref
                
    def delete_at_start(self): 
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        if self.start_node.nref is None: 
            self.start_node = None 
            return 
        self.start_node = self.start_node.nref 
        
    def delete_at_end(self): 
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        if self.start_node.nref is None: 
            self.start_node = None 
            return 
        n = self.start_node 
        while n.nref.nref is not None: 
            n = n.nref 
        n.nref = None
        
    def delete_element_by_value(self, x): 
        #check empty list
        if self.start_node is None: 
            print("The list has no element to delete") 
            return 
        #check if list is a single element
        if self.start_node.nref is None: 
            if self.start_node.item == x: 
                self.start_node = None 
            else: 
                print("Item not found")
                return 
        # list has > 1 element, and desirable elem is the first in the list
        # folllowing the delete_at_start() method
        if self.start_node.item == x: 
            self.start_node = self.start_node.nref 
            return 
        # list is nonsingle-element and desirable elem is not the first
        n = self.start_node 
        
        while n.nref.nref is not None: 
            if n.nref.item == x: 
                break 
            n = n.nref 
        if n.nref.nref is not None: 
            n.nref = n.nref.nref
        else: 
            if n.nref.item == x: 
                n.nref = None 
            else: 
                print("Element not found")
    def find(self, x):
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                print('true')
                return
            n = n.nref
        if n.item == x:
            print('true')
            return
        print('false')
        return
        
        
a = SingleLinkedList()
a.start_node = Node(1)
a.start_node.nref = Node(2)
a.start_node.nref.nref = Node(3)
a.start_node.nref.nref.nref = Node(4)

a.insert_at_start(5)
a.insert_after_item(1, 11)
a.insert_before_item(1, 111)
a.insert_before_item(5, 555)
a.delete_at_end()
a.delete_at_start()
a.delete_element_by_value(11)
a.insert_with_index(3, 12)
a.traverse_list()
print()
a.traverse_list_with_start(1)
