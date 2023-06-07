# String manipulation. capitalize, lower, strip

names = []
surnames = []
name = input("Add a name\n").strip().capitalize()
names.append(name)
print()
surname = input("Add a surname\n").strip().capitalize()
surnames.append(surname)
fullName = (f"{name} {surname}")
fullNames = []
if fullName not in fullNames:
  fullNames.append(f"{name} {surname}")
else:
  print("ERROR: Duplicate name")
for i in range(0,len(fullNames)):
  print(f"{i+1}. {fullNames[i]}")