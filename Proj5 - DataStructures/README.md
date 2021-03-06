# Title: Data Structures in Python

## Project Number: 5

## Team: Andrew Salazar

### Overview

A project containing a lot of things related to data structures within Python.

### Context

Data structures are objects specialized in efficient data storage and modification. Each data structure will serve different purposes, and knowing how they work will give insight on why they serve those purposes. In addition, efficient data structure implementation leads to optimized application performance. This project will document what I learn.

### Goals

- Experience more Python application building.
- Write more design documents.
- Learn about data structures.

### Achieved Milestones

- [6/5/2022] Project files created.
- [6/7/2022] Read through Python's documentation of lists.
- [6/11/2022] Read through Python's documentation of dictionaries, tuples, and sets.
- [6/14/2022] Read about Stacks from [here.](https://realpython.com/python-data-structures/)
- [6/15/2022] Read about Queues from [here.](https://realpython.com/python-data-structures/)
- [6/17/2022] Read about Linked Lists from [here.](https://realpython.com/linked-lists-python/)
- [6/20/2022] Read about Binary Trees from [here.](https://www.geeksforgeeks.org/python-data-structures/)
- [6/21/2022] Read about Binary Search Trees from [here](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/) and [here.](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)
- [7/8/2022] Read about Graphs from [here](https://www.tutorialspoint.com/python_data_structure/python_graphs.htm) and [here.](https://www.geeksforgeeks.org/python-data-structures/)

### Current Progress/Solution

List - A simple collection of data, and one of the built-in data structures in Python. It is a sequence data type, meaning items are stored in the order the user sets them. Duplicate items are allowed in a list. Lists are mutable, meaning list contents can be changed and modified in place after initial creation. Lists are similar to arrays in C, but has a few differences:

- Lists are not restricted to one data type; it can collect data of various types. Arrays are restricted to only one data type.
- Lists dynamically change in size. Arrays set their size upon creation, and it will not change afterwards.

Dictionary - A mapping of hashable objects to arbitrary objects, or key:value pairs. It is one of the built-in data structures in Python. Keys should be hashable, or immutable in nature, like strings. Keys can be numbers, much like indices in an array/list. Values can be any data type. Dictionaries are ordered, and cannot contain duplicate items.

Tuple - A collection of data, and one of the built-in data structures. Like lists, tuples are sequence data types. Tuples are immutable once created; values initialized cannot be changed unless you make a new tuple with different values. Tuples can contain any data type and can have duplicate values. However, to use tuples as keys in a dictionary, values in the tuple must be immutable.

Set - Sets are their own type of data structure, and a part of the built-in data structures. Sets have two variants: normal sets and frozen sets. Normal sets (referred to as just sets) are mutable, and frozen sets are immutable. Both set variants are unordered. Sets cannot have duplicate items. Only frozen sets are usable for dictionary keys.

Stack - A data structure organized in a way similar to any stack of objects. In programming, this is called Last-In, First-Out (LIFO) semantics, where you stack data on top of each other, and have access to only the data at the top of the stack. Python does not have an official implementation of a stack, but it can be implemented with a Python list or with the `deque` class from the `collections` module.

Queue - A data structure organized in a way similar to any line (or queue, depending on geographical location) of objects. In programming, this is called First-In, First-Out (FIFO) semantics, where data objects are put in a line, and the data that got in the line first are processed first. Python does not have an official implementation of a queue, but it can be implemented using lists (albeit, not very efficiently) or with the `deque` class from the `collections` module.

Linked List - A data structure that collects data like a list, but the data does not have to be contiguous in memory. Items in the linked list are connected with "pointers." There are no official pointers (C language style) in Python, so the best we can do is use reference variables (will call them pointers). A linked list starts with a head pointer that denotes the start of the list and points to the first node. Linked list nodes contain data and a pointer to point towards successive linked list items. There is no official implementation of linked lists in Python, but it can be user-defined.

Binary Tree - A user-defined data structure that represents a hierarchy of nodes. Each node holds data, a left child pointer, and a right child pointer. The top-most node is called the root, and is the starting place when traversing the binary tree. The bottom-most nodes (i.e: nodes with no children) are called leaves.

Binary Search Tree - A variant of the binary tree. In addition to having up to two children per node, there are three more definitions that make a binary tree a binary search tree:

- The left subtree of the root node contains data smaller than the root node's data.
- The right subtree of the root node contains data bigger than the root node's data.
- Both left and right subtrees are also BSTs.

For example: if I had a BST with a root of 100 and I wanted to insert 50 and 150 into the BST, then `BSTNode(50)` would be set as the root - `BSTNode(100)` - node's left subtree, and `BSTNode(150)` would be the root node's right subtree.

Graphs - A data structure containing a set of nodes and a set of links between different nodes. Nodes are also called vertices and links between nodes are also called edges or arcs. While Python does not have official support for a graph, it is easily implemented with existing Python data structures. One common way of representation is to track each node's adjacency to other nodes. Two nodes are adjacent when connected with an edge. Tracking node adjacency can be done with a 2D list or with a dictionary, but there are more ways to accomplish this task. Graphs can be directed, which means that edges are directed from one node to another, and not in the reverse direction. Graphs can be undirected, which means that edges are pointing in both directions between nodes. Edges may also have weight attached to them, which may represent different things based on the context of the graph.
