'''## 1. Interaction Between Multiple Objects

Objects can be designed to interact with other objects, pass each other as parameters, or contain references to other objects.

* **Passing Objects to Methods:** An object can accept another object as an argument within its method to perform actions between them.
* **Storing Objects as Attributes:** A class can contain instance variables that hold references to other custom objects (e.g., a `Person` object owning a `Robot` object).

---

## 2. Theoretical Example: Robot Ownership & Relationships

Expanding on the `Robot` class from Lecture 3, consider introducing a `Person` class that can own or interact with `Robot` objects:

* **Person Class:** Attributes `name`, `personality`, and `isSitting`.
* **Robot Object Owned by Person:** A `Person` instance holds a reference to a `Robot` object inside its attribute `robotOwned`.

Class: Person
├── Attributes:
│   ├── name (String)
│   ├── personality (String)
│   ├── isSitting (Boolean)
│   └── robotOwned (Robot object reference)
└── Methods:
├── sitDown()
└── standUp()


---

## 3. Implementation in Java

### Defining Interacting Classes
```java
// Person class interacting with the Robot class
public class Person {
    String name;
    String personality;
    boolean isSitting;
    Robot robotOwned; // Reference to another object

    // Constructor
    Person(String name, String personality, boolean isSitting) {
        this.name = name;
        this.personality = personality;
        this.isSitting = isSitting;
    }

    void sitDown() {
        this.isSitting = true;
    }

    void standUp() {
        this.isSitting = false;
    }
}
Linking Objects Together in Code
Java
public class Main {
    public static void main(String[] args) {
        // Instantiate Robot objects
        Robot r1 = new Robot("Tom", "red", 30);
        Robot r2 = new Robot("Jerry", "blue", 40);

        // Instantiate Person object
        Person p1 = new Person("Alice", "aggressive", false);
        Person p2 = new Person("Bob", "talkative", true);

        // Assign Robot ownership
        p1.robotOwned = r2; // Alice owns Jerry
        p2.robotOwned = r1; // Bob owns Tom

        // Invoke method on owned object through Person instance
        p1.robotOwned.introduceSelf(); // Output: My name is Jerry
    }
}
4. Key Takeaways
Object References: Object variables do not store the physical object directly; they store a pointer/reference to the object's location in memory.

Object Composition: Combining objects within objects allows you to build complex data structures (like nodes pointing to other nodes in Linked Lists or Trees).

Pointers to null: If an object attribute (like robotOwned) is not assigned, accessing methods on it will trigger a NullPointerException.'''