# Solution (No Peeking!)

![](https://www.youtube.com/watch?v=Co-jqvo0cDI)

<details> <summary> 👀 Answer </summary>

```python
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
```

</details>