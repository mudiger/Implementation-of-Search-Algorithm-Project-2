#DAA project
#Saarthak Mudigere Girish
#1002119262



''' 2. Project 2 (Search Algorithms)

    Implement and compare the following search algorithm:
        ● Linear search
        ● Binary search in sorted array.
        ● Binary search tree
        ● Red-Black Tree
'''


    
# Red Black Tree
# Define Node
class Node():
    def __init__(self,val):
        self.val = val                                   
        self.parent = None                               
        self.left = None                                 
        self.right = None                                
        self.color = 1                                   

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = Node (0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Insert New Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   

        y = None
        x = self.root                                    

        while x != self.NULL :                           
            y = x
            if node.val < x.val :
                x = x.left
            else :
                x = x.right

        node.parent = y                                  
        if y == None :                                   
            self.root = node
        elif node.val < y.val :                          
            y.left = node
        else :
            y.right = node

        if node.parent == None :                     
            node.color = 0
            return

        if node.parent.parent == None :                  
            return

        self.fixInsert ( node )                          



    # Code for left rotate
    def LR ( self , x ) :
        y = x.right                                  
        x.right = y.left                                
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                             
        if x.parent == None :                           
            self.root = y                              
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                      
        x.left = y.right                                
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                             
        if x.parent == None :                          
            self.root = y                               
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y


    # Fix Up Insertion
    def fixInsert(self, k):
        while k.parent.color == 1:                       
            if k.parent == k.parent.parent.right:        
                u = k.parent.parent.left                
                if u.color == 1:                          
                    u.color = 0                          
                    k.parent.color = 0
                    k.parent.parent.color = 1            
                    k = k.parent.parent                  
                else:
                    if k == k.parent.left:                
                        k = k.parent
                        self.RR(k)                        
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:                                       
                u = k.parent.parent.right                
                if u.color == 1:                          
                    u.color = 0                         
                    k.parent.color = 0
                    k.parent.parent.color = 1            
                    k = k.parent.parent                   
                else:
                    if k == k.parent.right:              
                        k = k.parent
                        self.LR(k)                       
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)             
            if k == self.root:                           
                break
        self.root.color = 0                              

    
    # Find a node with a given value in the tree
    def __searchValue(self, node, b, temp_arr):
        try:
            if b < node.val:
                if node.left is None:
                    return -1
                temp_arr.append(node.val)
                return self.__searchValue(node.left, b, temp_arr)
            elif b > node.val:
                if node.right is None:
                    return -1
                temp_arr.append(node.val)
                return self.__searchValue(node.right, b, temp_arr)
            else:
                temp_arr.append(node.val)
                return temp_arr
        except:
            return -1
    
    
    def searchValue(self, b, temp_arr):
        return self.__searchValue(self.root, b, temp_arr)
    
  


#Linear Search
def linear_search(user_input, search_element):
    for i in range(len(user_input)):
        if user_input[i] == search_element:
            return i
    return -1

#Bineary search
def binary_search(user_input, low, high, search_element):
    if high >= low:
        mid = (low + high) // 2
 
        if user_input[mid] == search_element:
            return mid
 
        elif user_input[mid] > search_element:
            return binary_search(user_input, low, mid-1,search_element)
 
        else:
            return binary_search(user_input, mid+1, high,search_element)
 
    return -1


#Binary search tree
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

# Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


# findval method to compare the value with nodes
    def findval(self, lkpval, temp_arr):
        if lkpval < self.data:
            if self.left is None:
                return -1
            temp_arr.append(self.data)
            return self.left.findval(lkpval, temp_arr)
        elif lkpval > self.data:
            if self.right is None:
               return -1
            temp_arr.append(self.data)
            return self.right.findval(lkpval, temp_arr)
        else:
            temp_arr.append(self.data)
            return temp_arr




#GUI
#import modules
from tkinter import *
import timeit
from numpy import random

# Convert str to int 
def string_to_int_1(input_string):
    string_list = input_string.split(",")
    if string_list[0] == 'random':
        return random.randint(1000, size=(int(string_list[1])))
    else:
        integer_list = []
        for string in string_list:
            integer_list.append(int(string))
        return integer_list

def string_to_int_3(input_string_2):
    string_list_2 = input_string_2.split("+")
    type_list = []
    for string_2 in string_list_2:
        type_list.append(string_2)
    return type_list

# Switch Case
def compute_search():
    arr = string_to_int_1(connection_user_input.get())
    print(arr)
    string_to_int_2 = int(connection_element_search.get())
    type = string_to_int_3(connection_algorithm.get())
    
    
    array_entry.delete(0, END)
    element_entry.delete(0, END)
    algorithm_entry.delete(0, END)

    
    for i in range(len(type)):
        if type[i] == 'ls':
            search_start_time_1 = timeit.timeit()
            output = linear_search(arr, string_to_int_2)
            search_end_time_1 = timeit.timeit()
            time_difference_1 = abs(search_end_time_1-search_start_time_1)
            if output!=-1:
                temp_output = f"Element found at index : {output}"
            else: 
                temp_output = "Element not found"
            print_result("Linear Search : ", time_difference_1, temp_output)
        
        if type[i] == 'bs':
            sorted_arr=[]
            for g in arr:
                sorted_arr.append(g)
            sorted_arr.sort()
            search_start_time_2 = timeit.timeit()
            output = binary_search(sorted_arr, 0, len(arr)-1, string_to_int_2)
            search_end_time_2 = timeit.timeit()
            time_difference_2 = abs(search_end_time_2-search_start_time_2)
            if output!=-1:
                temp_output = f"Element found at index : {output}"
            else: 
                temp_output = "Element not found"
            print_result("Binary Search : ", time_difference_2, temp_output)

        if type[i] == 'bst':
            root = Node(arr[0])
            for next_node in arr:
                root.insert(next_node)  
            
            search_start_time_3 = timeit.timeit()
            output = root.findval(string_to_int_2, [])
            search_end_time_3 = timeit.timeit()
            time_difference_3 = abs(search_end_time_3-search_start_time_3)
            if output!=-1:
                temp_output = f"Element found with path : {output}"
            else: 
                temp_output = "Element not found"
            print_result("Binary Search tree : ", time_difference_3, temp_output)
        
        if type[i] == 'rb':
            bst = RBTree()
            
            for next_node in arr:
                bst.insertNode(next_node)  
            
            search_start_time_4 = timeit.timeit()
            output = bst.searchValue(string_to_int_2, [])
            search_end_time_4 = timeit.timeit()
            time_difference_4 = abs(search_end_time_4-search_start_time_4)
            if output!=-1:
                temp_output = f"Element found with path : {output}"
            else: 
                temp_output = "Element not found"
            print_result("Red Black Tree : ", time_difference_4, temp_output)

 
# Designing Algorithm(Second) window
def print_result(algorithm_type, time_difference, temp_output):
    global secondary_screen
    secondary_screen = Toplevel(main_screen)
    secondary_screen.title("Result")
    secondary_screen.geometry("650x200")

    Label(secondary_screen, text=algorithm_type, font=("Arial", 25)).pack()
    Label(secondary_screen, text="").pack()
    
    Label(secondary_screen, text=temp_output).pack()
    Label(secondary_screen, text="").pack()

    Label(secondary_screen, text=(f"Time taken by search is = {time_difference} sec")).pack()
    Label(secondary_screen, text="").pack()

    Button(secondary_screen, text="OK", command=delete_user_not_found_screen).pack()
    

 
# Deleting popups 
def delete_user_not_found_screen():
    secondary_screen.destroy()
 

 
# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x350")
    main_screen.title("Search Algorithms")
    Label(main_screen, text="Please enter details below").pack()
    Label(main_screen, text="").pack()
 
    global connection_user_input
    global connection_element_search
    global connection_algorithm
 
    connection_user_input = StringVar()
    connection_element_search = StringVar()
    connection_algorithm = StringVar()
 
    global array_entry
    global element_entry
    global algorithm_entry
 
    Label(main_screen, text="Please enter your array : ").pack()
    array_entry = Entry(main_screen, textvariable=connection_user_input)
    array_entry.pack()
    Label(main_screen, text="").pack()

    Label(main_screen, text="Please enter the element to be searched : ").pack()
    element_entry = Entry(main_screen, textvariable=connection_element_search)
    element_entry.pack()
    Label(main_screen, text="").pack()

    Label(main_screen, text="Please enter the algorithm to be searched with: ").pack()
    algorithm_entry = Entry(main_screen, textvariable=connection_algorithm)
    algorithm_entry.pack()
    Label(main_screen, text="").pack()

    Button(main_screen, text="GO!", width=10, height=1, command = compute_search).pack()
 
    main_screen.mainloop()
 

# main function
def main():
    main_account_screen()
    


if __name__ == "__main__":
    main()