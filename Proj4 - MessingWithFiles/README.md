# Messing With Files

## Project Number: 4

## Team: Andrew Salazar

### Overview

Just a project where I learn about how to read and write to files.

### Context

Input can come from three places: expressions (e.g: `y = x + 1`), interactions (e.g: `input()` and command line arguments), and files. I have already seen and worked with the first two methods of inputs, but now I want to learn more about file input and output.

### Goals

- Experience more Python application building.
- Write more design documents.

### Achieved Milestones

- [6/3/2022] "Project" started

### Current Progress/Solution

The only goal of this "project" is to learn about file input and output. Anything I learn about such will be documented below.

- Open files with `fileObj = open(<filename>, <mode>, <encoding>)`
  - Set `mode` as these values to:
    - 'r' = read-only
    - 'w' = write-only
    - 'a' = append
- Close files with `fileObj.close()`
  - Always make sure to close the file when you're done with it
  - Using a `with` statement guarantees that the file closes, regardless of the result
- Read file contents ...
  - ... with `fileObj.read([size])`. Reads `size` chars from the file. If `size` is not specified or negative, then read the entire file.
  - ... line by line with a `for` loop
  
  ```python
  for line in fileObj:
      print(line, end='')
  ```

  - ... line by line in a list with `fileObj.readlines()` or `list(fileObj)`
- Write contents to file with `fileObj.write(str)`. `str` is a string.
- Writing contents to the file set in append-mode will append the content to the end of the file, instead of truncating the existing content.
- Attempting to write to a file opened in a non-write mode gives an error.
- Attempting to read a file opened in a non-read mode gives an error.
- A file object has a position in the file. Use `fileObj.tell()` to get its current location, and `fileObj.seek(<offset>, <whence>)` to set its location. `Offset` is the amount to move from `whence`, which is a reference point relative to the file. I.e: start at the position specified by `whence` and move `offset` amount from there. 
