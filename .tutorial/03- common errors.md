# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Order matters

👉 What happens if you enter a space before ' phone' when you `run` this code? It duplicates!

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

<details> <summary> 👀 Answer </summary>

  - The functions manipulating the strings are applied in the order we add them. In this code, the first character is capitalized and then the spaces are stripped. We need to switch the order in which these functions are added.
    
```python
while True:
  addItem = input("Item > ").strip().capitalize()
  if addItem not in myList:
    myList.append(addItem)
  printList()
```


</details>