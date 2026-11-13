Here’s a Java → Python cheat sheet in Markdown format, focused for a Senior Java Developer transitioning to Python:

# Java → Python Cheat Sheet

## 1. Variables & Types
| Java                  | Python                           | Notes |
|-----------------------|---------------------------------|-------|
| `int x = 5;`          | `x = 5`                          | Dynamic typing |
| `double y = 3.14;`    | `y = 3.14`                       | Float type in Python |
| `boolean flag = true;`| `flag = True`                     | Capitalized True/False |
| `String s = "hi";`    | `s = "hi"`                        | Strings are objects |
| `final int z = 10;`   | `z = 10`                          | No constants by default |

---

## 2. Control Flow
### If-Else
```java
if (x > 0) {
    System.out.println("Positive");
} else {
    System.out.println("Non-positive");
}

if x > 0:
    print("Positive")
else:
    print("Non-positive")

Switch / Match
switch(day) {
    case 1: System.out.println("Mon"); break;
    case 2: System.out.println("Tue"); break;
}

match day:
    case 1: print("Mon")
    case 2: print("Tue")

Loops

For loop

for(int i=0; i<5; i++) { System.out.println(i); }

for i in range(5):
    print(i)


For-each loop

for(String s : list) { System.out.println(s); }

for s in lst:
    print(s)


While loop

while(x < 5) { x++; }

while x < 5:
    x += 1

3. Functions / Methods
int add(int a, int b) { return a+b; }

def add(a: int, b: int) -> int:
    return a + b


Default arguments:

def greet(name="Guest"):
    print(f"Hello {name}")

4. Classes & OOP
public class Person {
    private String name;
    public Person(String name) { this.name = name; }
    public String getName() { return name; }
}

class Person:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name


Inheritance

class Employee extends Person { }

class Employee(Person):
    pass


Interfaces / Abstract Classes

interface Vehicle { void drive(); }

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

5. Collections
Java	Python
ArrayList<String>	list
HashMap<String,Int>	dict
HashSet<Integer>	set
Arrays.asList()	list([...])

Iteration

for(String s : list) { ... }

for s in lst:
    ...


Map / Filter / Reduce

list.stream().filter(x -> x>0).map(x->x*2).collect(Collectors.toList());

list(filter(lambda x: x>0, map(lambda x: x*2, lst)))
# Or list comprehension
[x*2 for x in lst if x>0]

6. Exception Handling
try {
    int x = 5/0;
} catch(ArithmeticException e) {
    e.printStackTrace();
} finally {
    System.out.println("Done");
}

try:
    x = 5/0
except ZeroDivisionError as e:
    print(e)
finally:
    print("Done")

7. Imports & Packages
import java.util.List;

from typing import List


Python standard library is rich: os, sys, json, datetime, pathlib.

8. Misc Pythonic Tips

with open('file.txt') as f: → Auto-close file

enumerate(list) → Loop with index

zip(list1, list2) → Loop in parallel

*args, **kwargs → Variable arguments

List comprehensions > for-loops for simple transformations

9. Lambda & Functional Style
list.stream().map(x -> x*2).collect(Collectors.toList());

list(map(lambda x: x*2, lst))
# Or more Pythonic:
[x*2 for x in lst]

10. Running Code

Python files: python myfile.py

Interactive REPL: python or ipython

Virtual environments:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows