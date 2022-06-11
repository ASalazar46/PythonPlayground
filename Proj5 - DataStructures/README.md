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

### Current Progress/Solution

List - A simple collection of data, and one of the built-in data structures in Python. It is a sequence data type, meaning items are stored in the order the user set them. Duplicate items are allowed in a list. Lists are mutable, meaning list contents can changed and modified in place after initial creation. Lists are similar to arrays in C, but has a few differences:

- Lists are not restricted to one data type; it can collect data of various types. Arrays are restricted to only one data type.
- Lists dynamically change in size. Arrays set their size upon creation, and it will not change afterwards.

Dictionary - A mapping of hashable objects to arbitrary objects, or key:value pairs. It is one of the built-in data structures in Python. Keys should be hashable, or immutable in nature, like strings. Keys can be numbers, much like indices in an array/list. Values can be any data type. Dictionaries are ordered, and cannot contain duplicate items.

Tuple - A collection of data, and one of the built-in data structures. Like lists, tuples are sequence data types. Tuples are immutable once created; values initialized cannot be changed unless you make a new tuple with different values. Tuples can contain any data type and can have duplicate value. However, to use tuples as keys in a dictionary, values in the tuple must be immutable.

Set - Sets are their own type of data structure, and a part of the built-in data structures. Sets have two variants: normal sets and frozen sets. Normal sets (referred to as just sets) are mutable, and frozen sets are immutable. Both set variants are unordered. Sets cannot have duplicate items. Only frozen sets are usable for dictionary keys.
