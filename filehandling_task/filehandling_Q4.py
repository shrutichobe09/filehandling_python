"""
What happens if you try to read from a file that does not exist? 
How can you prevent the program from crashing?
"""
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")

