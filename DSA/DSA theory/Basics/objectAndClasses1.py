'''## 1. Core Concepts & Definitions

* **Class:** A blueprint, template, or category definition used to create objects. It defines the structure (attributes) and behavior (methods) without holding specific instance data.
* **Object:** An actual instance created from a class that occupies memory and contains real values for the attributes defined by the class.
* **Instance Variables / Attributes:** Variables defined inside an object that store state or properties specific to that instance.
* **Methods:** Functions defined inside a class/object that dictate what actions or behavior the object can perform.
* **Constructor:** A specialized function run automatically upon object creation to initialize its instance variables.

---

## 2. Theoretical Example: Robot Representation

Imagine creating a platform with interactive robots (`Tom` and `Jerry`):

* **Tom:** Red color, weight $30\text{ lbs}$, method `introduceSelf()`.
* **Jerry:** Blue color, weight $40\text{ lbs}$, method `introduceSelf()`.

### The "Robot" Class Blueprint
Class: Robot
├── Attributes (Properties):
│   ├── name (String)
│   ├── color (String)
│   └── weight (Integer)
└── Methods (Behaviors):
└── introduceSelf() -> Prints: "My name is " + this.name


---

## 3. Implementation in Java

### Class Definition (With Constructor & Methods)
```java
public class Robot {
    // Attributes / Instance Variables
    String name;
    String color;
    int weight;

    // Custom Constructor
    Robot(String name, String color, int weight) {
        this.name = name;   // 'this' refers to the specific instance being created
        this.color = color;
        this.weight = weight;
    }

    // Method Definition
    void introduceSelf() {
        System.out.println("My name is " + this.name);
    }
}
Instantiating Objects and Calling Methods
Java
public class Main {
    public static void main(String[] args) {
        // Instantiate Object 1 using Constructor
        Robot r1 = new Robot("Tom", "red", 30);
        
        // Instantiate Object 2 using Constructor
        Robot r2 = new Robot("Jerry", "blue", 40);

        // Invoke Methods
        r1.introduceSelf(); // Output: My name is Tom
        r2.introduceSelf(); // Output: My name is Jerry
    }
}
4. Key Takeaways
this Keyword: Refers directly to the specific object instance executing the method or constructor call.

Default vs. Custom Constructors:

Languages provide a default zero-argument constructor automatically if no constructor is defined.

Defining a custom constructor overrides and disables the default constructor, forcing proper attribute initialization upon instantiation.

Relevance to Data Structures: Classes and objects form the fundamental building block for creating complex data structures like Linked Lists, Trees, and Graphs (via Node objects linked together).'''