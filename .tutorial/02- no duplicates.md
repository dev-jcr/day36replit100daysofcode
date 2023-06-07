# No Duplicates

This is a simple program that creates a list with a simple subroutine. In the `while True` loop, the user is adding something to the list. (This is nowhere near as complicated as what you have done).

👉 What happens when you `run` this code and add 'phone' and 'Phone' to your list? Does it create duplicates?
```python
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ")
  if addItem not in myList:
    myList.append(addItem) 
  printList()
```
👉 Here is an easier way to ensure you do not have duplicates. Use these various string manipulations in your loop:



```python
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").capitalize().strip()
  if addItem not in myList:
    myList.append(addItem)
  printList()
```

*Note: Whatever you do after the `.` will happen to the string. If you use `.lower`, then the string will print in lower case.*

