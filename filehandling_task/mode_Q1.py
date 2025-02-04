"""
Q1 What are the different modes used when opening a file in Python (e.g., r, w, a, etc.),
 and what do they mean?


1. 'r' (Read)
Opens the file for reading only.
The file must exist, otherwise a FileNotFoundError will be raised.
"""

with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)

"""
2. 'w' (Write)
Opens the file for writing only.
If the file already exists, it will overwrite the file. If the file doesn't exist, it will be created.

"""
with open('myfile.txt', 'w') as file:
    file.write("Hello, World!")


"""
3.'a' (Append)
Opens the file for appending.
If the file exists, the new content is added at the end of the file without overwriting the existing content. If the file doesn't exist, it will be created.

"""
with open('myfile.txt', 'a') as file:
    file.write("\nAppended text.")


"""
4. 'x' (Exclusive Creation)
Opens the file for writing, but only if the file does not already exist.
If the file exists, a FileExistsError will be raised.

"""
with open('example1.txt', 'x') as file:
    file.write("This will create the file if it doesn't exist.")


"""
5. 'b' (Binary Mode)
Specifies that the file should be opened in binary mode.
This is added to other modes like 'rb', 'wb', 'ab', etc., to handle binary files (like images, audio, etc.).
"""
with open('example_binary.jpg', 'rb') as file:
    content = file.read()
