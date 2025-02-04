"""
6 Describe how you would handle reading and writing CSV, JSON, or XML files using Python.

1. Handling CSV Files
CSV files are a common format for tabular data. 
Python's built-in csv module provides an easy way to read from and write to CSV files.
"""
#read a csv file 
import csv
with open('data.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of values


#writting with csv
import csv
data = [['Name', 'Age', 'City'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles']]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Writes multiple rows at once



"""
2. Handling JSON Files
JSON is widely used for data interchange, and Python's json module makes it easy to read and write JSON data.
"""
#1 Reading a JSON file:
import json
with open('my_json.json', 'r') as file:
    data = json.load(file)  # Parses the JSON data into a Python object (dict or list)
    print(data)


# 2 Writing to a JSON file:
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('my_json.json', 'w') as file:
    json.dump(data, file, indent=4)  # Writes the Python 


"""
3. Handling XML Files
XML is a markup language used for data exchange, 
and Python's xml.etree.ElementTree module provides methods to read and write XML dat
"""
#writing xml file 
import xml.etree.ElementTree as ET

root = ET.Element('data')  # Create the root element
person = ET.SubElement(root, 'person')  # Add a sub-element under the root
person.set('name', 'shruti')
person.set('age', '30')

tree = ET.ElementTree(root)

with open('output.xml', 'wb') as file:
    tree.write(file)  # Writes the XML structure to the file


#read the xml file 
import xml.etree.ElementTree as ET

tree = ET.parse('output.xml')
root = tree.getroot()  # Root of the XML structure

# Iterate over elements
for child in root:
    print(child.tag, child.attrib)  # Prints element tags and attributes



"""
Key Considerations:
1. CSV: It's best suited for tabular data, where each line represents a row and columns are separated by commas.
 Use csv for simple data exchange.

2. JSON: It's flexible and supports complex nested structures. 
It's commonly used for APIs, web services, and configuration files.
 json is great for working with objects (dicts) or arrays (lists).

3 XML: It's more verbose and is used for structured data representation in markup format. 
Use xml.etree.ElementTree or other libraries like lxml for more advanced XML processing.


Summary:
CSV: csv.reader() for reading, csv.writer() for writing.
JSON: json.load() for reading, json.dump() for writing.
XML: xml.etree.ElementTree for parsing and writing XML data.


"""