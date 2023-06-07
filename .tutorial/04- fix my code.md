# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip = "pasta": 
  print("Get out the pasta maker.")
elif whatToEatlower() == "TACOS":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")
```

<details> <summary> 👀 Answer </summary>

- Make sure you include `.` and `()` in your string manipulations.
- Strip the spaces first.
- The string manipulation needs to match the string. Ex: `.lower` = lowercase string
- Are your logical operators correct for the `if` statement?

```python
whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip().lower() == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.strip().lower() == "tacos":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")
  ```
</details>
  