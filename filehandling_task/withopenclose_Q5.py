"""
Q 5) What is the difference between using open() and close() explicitly versus using a
 context manager (with statement) to handle file operations?

1. Automatic resource management: The with statement creates a context 
where the file is automatically opened and closed. When the block of code 
inside the with statement is finished (whether normally or due to an exception), 
the file is automatically closed.

2 .Error handling: Even if an error occurs during the file operations, Python will 
ensure that the file is properly closed when the block exits. This prevents resource 
leaks and ensures file integrity.

3 Cleaner and safer: The context manager guarantees that resources like files are managed correctly 
and automatically, making it the preferred approach for file handling.
"""
with open('pythonnotes.txt', 'r') as file:
    content = file.read()
    print(content)
