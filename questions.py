# questions.py - Question Database for Interview Chatbot

questions_db = {
    "DSA": [
        {
            "question": "What is the time complexity of binary search?",
            "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
            "answer": 1,
            "explanation": "Binary search divides the search space in half each time, resulting in O(log n) complexity."
        },
        {
            "question": "Which data structure uses LIFO (Last In First Out)?",
            "options": ["Queue", "Stack", "Tree", "Graph"],
            "answer": 1,
            "explanation": "Stack follows LIFO principle where the last element added is the first one removed."
        },
        {
            "question": "What is the worst-case time complexity of Quick Sort?",
            "options": ["O(n log n)", "O(n)", "O(n^2)", "O(log n)"],
            "answer": 2,
            "explanation": "Quick Sort has O(n^2) worst-case when pivot selection is poor, though average case is O(n log n)."
        },
        {
            "question": "Which traversal of binary tree uses a queue?",
            "options": ["Inorder", "Preorder", "Postorder", "Level order"],
            "answer": 3,
            "explanation": "Level order traversal (BFS) uses a queue data structure."
        },
        {
            "question": "What is the space complexity of merge sort?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "answer": 2,
            "explanation": "Merge sort requires O(n) additional space for temporary arrays during merging."
        },
        {
            "question": "Which sorting algorithm is most efficient for small datasets?",
            "options": ["Merge Sort", "Quick Sort", "Insertion Sort", "Heap Sort"],
            "answer": 2,
            "explanation": "Insertion Sort is efficient for small datasets due to low overhead."
        },
        {
            "question": "What is a hash collision?",
            "options": ["Two keys map to same index", "Hash function fails", "Memory overflow", "Duplicate keys"],
            "answer": 0,
            "explanation": "Hash collision occurs when two different keys hash to the same index."
        },
        {
            "question": "Which data structure is best for implementing LRU cache?",
            "options": ["Array", "LinkedList + HashMap", "Stack", "Tree"],
            "answer": 1,
            "explanation": "Combination of HashMap and Doubly LinkedList provides O(1) operations for LRU cache."
        },
        {
            "question": "What is the time complexity of insertion in a balanced BST?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
            "answer": 1,
            "explanation": "Balanced BST maintains height of log n, making insertion O(log n)."
        },
        {
            "question": "Which algorithm uses divide and conquer strategy?",
            "options": ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"],
            "answer": 2,
            "explanation": "Merge Sort divides array into halves recursively, following divide and conquer."
        },
        {
            "question": "What is the best case time complexity of bubble sort?",
            "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
            "answer": 0,
            "explanation": "Best case for bubble sort is O(n) when array is already sorted."
        },
        {
            "question": "Which data structure is used in BFS?",
            "options": ["Stack", "Queue", "Priority Queue", "Deque"],
            "answer": 1,
            "explanation": "BFS uses Queue to process nodes level by level."
        },
        {
            "question": "What is a circular queue?",
            "options": ["Queue with no end", "Queue where rear connects to front", "Infinite queue", "Double ended queue"],
            "answer": 1,
            "explanation": "Circular queue connects rear to front, efficiently using space."
        },
        {
            "question": "Which tree traversal visits root first?",
            "options": ["Inorder", "Preorder", "Postorder", "Level order"],
            "answer": 1,
            "explanation": "Preorder traversal visits root first, then left and right subtrees."
        },
        {
            "question": "What is the height of a complete binary tree with n nodes?",
            "options": ["log n", "n", "n log n", "n^2"],
            "answer": 0,
            "explanation": "Complete binary tree has height of log n where n is number of nodes."
        },
        {
            "question": "Which searching algorithm requires sorted data?",
            "options": ["Linear Search", "Binary Search", "Jump Search", "Interpolation Search"],
            "answer": 1,
            "explanation": "Binary Search requires data to be sorted to work correctly."
        },
        {
            "question": "What is the time complexity of accessing an element in an array?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "answer": 0,
            "explanation": "Arrays provide constant time O(1) access using index."
        },
        {
            "question": "Which is NOT a stable sorting algorithm?",
            "options": ["Merge Sort", "Bubble Sort", "Quick Sort", "Insertion Sort"],
            "answer": 2,
            "explanation": "Quick Sort is not stable as it may change relative order of equal elements."
        },
        {
            "question": "What is a deque?",
            "options": ["Single ended queue", "Double ended queue", "Priority queue", "Circular queue"],
            "answer": 1,
            "explanation": "Deque (Double Ended Queue) allows insertion and deletion from both ends."
        },
        {
            "question": "Which data structure uses both LIFO and FIFO?",
            "options": ["Stack", "Queue", "Deque", "Array"],
            "answer": 2,
            "explanation": "Deque can operate as both stack (LIFO) and queue (FIFO)."
        },
        {
            "question": "What is the space complexity of recursive fibonacci?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(2^n)"],
            "answer": 2,
            "explanation": "Recursive fibonacci has O(n) space complexity due to call stack."
        },
        {
            "question": "Which graph traversal uses stack?",
            "options": ["BFS", "DFS", "Dijkstra", "Prim's"],
            "answer": 1,
            "explanation": "DFS uses stack (or recursion which uses call stack) for traversal."
        },
        {
            "question": "What is a max heap?",
            "options": ["Parent smaller than children", "Parent larger than children", "All nodes equal", "Random order"],
            "answer": 1,
            "explanation": "Max heap has parent node value greater than or equal to its children."
        },
        {
            "question": "Which operation is NOT efficient in a linked list?",
            "options": ["Insertion at beginning", "Deletion at beginning", "Random access", "Sequential access"],
            "answer": 2,
            "explanation": "Linked lists don't support efficient random access, requiring O(n) traversal."
        },
        {
            "question": "What is the time complexity of heap sort?",
            "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
            "answer": 1,
            "explanation": "Heap sort has O(n log n) time complexity in all cases."
        },
        {
            "question": "Which data structure is used for Dijkstra's algorithm?",
            "options": ["Stack", "Queue", "Priority Queue", "Array"],
            "answer": 2,
            "explanation": "Dijkstra's algorithm uses Priority Queue to select minimum distance node."
        },
        {
            "question": "What is a trie?",
            "options": ["Binary tree", "Prefix tree", "Balanced tree", "Complete tree"],
            "answer": 1,
            "explanation": "Trie is a prefix tree used for efficient string storage and retrieval."
        },
        {
            "question": "Which has better worst case: Quick Sort or Merge Sort?",
            "options": ["Quick Sort", "Merge Sort", "Both same", "Depends on data"],
            "answer": 1,
            "explanation": "Merge Sort has O(n log n) worst case while Quick Sort has O(n^2)."
        },
        {
            "question": "What is dynamic programming?",
            "options": ["Random approach", "Greedy approach", "Optimization using subproblems", "Brute force"],
            "answer": 2,
            "explanation": "Dynamic programming solves problems by breaking into overlapping subproblems."
        },
        {
            "question": "Which is the best average case sorting algorithm?",
            "options": ["Bubble Sort", "Quick Sort", "Selection Sort", "Insertion Sort"],
            "answer": 1,
            "explanation": "Quick Sort has best average case performance of O(n log n) with low overhead."
        }
    ],
    "OOP": [
        {
            "question": "Which OOP principle allows a class to inherit properties from another class?",
            "options": ["Encapsulation", "Polymorphism", "Inheritance", "Abstraction"],
            "answer": 2,
            "explanation": "Inheritance allows a class to acquire properties and methods from another class."
        },
        {
            "question": "What is method overloading?",
            "options": ["Same method name, different parameters", "Same method name, same parameters", 
                       "Different method name, same parameters", "Runtime polymorphism"],
            "answer": 0,
            "explanation": "Method overloading is compile-time polymorphism with same name but different parameters."
        },
        {
            "question": "Which keyword is used to prevent method overriding in Java?",
            "options": ["static", "final", "abstract", "private"],
            "answer": 1,
            "explanation": "The 'final' keyword prevents a method from being overridden in subclasses."
        },
        {
            "question": "What is encapsulation?",
            "options": ["Hiding implementation details", "Creating multiple methods", 
                       "Inheriting properties", "Creating objects"],
            "answer": 0,
            "explanation": "Encapsulation is wrapping data and methods together and hiding internal details."
        },
        {
            "question": "Which type of polymorphism is method overriding?",
            "options": ["Compile-time", "Runtime", "Static", "Early binding"],
            "answer": 1,
            "explanation": "Method overriding is runtime polymorphism (dynamic binding)."
        },
        {
            "question": "What is an abstract class?",
            "options": ["Cannot be instantiated", "Has no methods", "Cannot have variables", "Must be final"],
            "answer": 0,
            "explanation": "Abstract class cannot be instantiated and may contain abstract methods."
        },
        {
            "question": "What is the diamond problem in OOP?",
            "options": ["Multiple inheritance ambiguity", "Memory leak", "Infinite loop", "Syntax error"],
            "answer": 0,
            "explanation": "Diamond problem occurs when a class inherits from two classes that have a common parent."
        },
        {
            "question": "What is a constructor?",
            "options": ["Destroys objects", "Initializes objects", "Copies objects", "Deletes objects"],
            "answer": 1,
            "explanation": "Constructor is a special method that initializes objects when created."
        },
        {
            "question": "Which access modifier is most restrictive?",
            "options": ["public", "protected", "private", "default"],
            "answer": 2,
            "explanation": "Private is most restrictive, accessible only within the same class."
        },
        {
            "question": "What is a destructor?",
            "options": ["Creates objects", "Cleans up resources", "Copies objects", "Inherits objects"],
            "answer": 1,
            "explanation": "Destructor cleans up resources when object is destroyed."
        },
        {
            "question": "What is interface in OOP?",
            "options": ["Concrete class", "Abstract contract", "Data type", "Variable"],
            "answer": 1,
            "explanation": "Interface is an abstract contract that defines methods without implementation."
        },
        {
            "question": "Can we overload constructor?",
            "options": ["Yes", "No", "Only in Java", "Only in C++"],
            "answer": 0,
            "explanation": "Constructors can be overloaded with different parameter lists."
        },
        {
            "question": "What is 'this' keyword?",
            "options": ["Refers to parent class", "Refers to current object", "Refers to child class", "Refers to interface"],
            "answer": 1,
            "explanation": "'this' keyword refers to the current instance of the class."
        },
        {
            "question": "What is multiple inheritance?",
            "options": ["One parent, multiple children", "Multiple parents, one child", "No inheritance", "Single inheritance"],
            "answer": 1,
            "explanation": "Multiple inheritance means a class inherits from multiple parent classes."
        },
        {
            "question": "What is method hiding?",
            "options": ["Private method", "Static method in subclass", "Protected method", "Abstract method"],
            "answer": 1,
            "explanation": "Method hiding occurs when subclass defines static method with same signature."
        },
        {
            "question": "What is composition?",
            "options": ["IS-A relationship", "HAS-A relationship", "No relationship", "Multiple relationship"],
            "answer": 1,
            "explanation": "Composition represents HAS-A relationship where object contains other objects."
        },
        {
            "question": "Can interface have variables?",
            "options": ["Yes, only constants", "Yes, any variables", "No variables allowed", "Only static"],
            "answer": 0,
            "explanation": "Interface can have variables but they are implicitly public, static, and final."
        },
        {
            "question": "What is aggregation?",
            "options": ["Strong relationship", "Weak HAS-A relationship", "IS-A relationship", "No relationship"],
            "answer": 1,
            "explanation": "Aggregation is weak HAS-A relationship where objects have independent lifecycle."
        },
        {
            "question": "What is virtual function?",
            "options": ["Static function", "Function that can be overridden", "Private function", "Final function"],
            "answer": 1,
            "explanation": "Virtual function can be overridden in derived classes for runtime polymorphism."
        },
        {
            "question": "What is super keyword?",
            "options": ["Refers to current object", "Refers to parent class", "Refers to child class", "Refers to interface"],
            "answer": 1,
            "explanation": "Super keyword refers to parent class members and constructor."
        },
        {
            "question": "Can abstract class have constructor?",
            "options": ["Yes", "No", "Only default", "Only parameterized"],
            "answer": 0,
            "explanation": "Abstract class can have constructor used by subclasses."
        },
        {
            "question": "What is static binding?",
            "options": ["Runtime binding", "Compile-time binding", "No binding", "Dynamic binding"],
            "answer": 1,
            "explanation": "Static binding resolves method calls at compile-time."
        },
        {
            "question": "What is dynamic binding?",
            "options": ["Compile-time binding", "Runtime binding", "No binding", "Static binding"],
            "answer": 1,
            "explanation": "Dynamic binding resolves method calls at runtime based on object type."
        },
        {
            "question": "Can we override static method?",
            "options": ["Yes", "No, only hide", "Yes, in Java", "Yes, in C++"],
            "answer": 1,
            "explanation": "Static methods cannot be overridden, only hidden in subclass."
        },
        {
            "question": "What is object cloning?",
            "options": ["Deleting object", "Creating copy of object", "Destroying object", "Comparing objects"],
            "answer": 1,
            "explanation": "Object cloning creates a copy of existing object."
        },
        {
            "question": "What is shallow copy?",
            "options": ["Copies references", "Deep copy of all members", "No copy", "Partial copy"],
            "answer": 0,
            "explanation": "Shallow copy copies object references, not the actual objects."
        },
        {
            "question": "What is deep copy?",
            "options": ["Copies references", "Copies all objects recursively", "No copy", "Surface copy"],
            "answer": 1,
            "explanation": "Deep copy creates copies of all referenced objects recursively."
        },
        {
            "question": "What is cohesion in OOP?",
            "options": ["Low relationship", "High relationship within class", "No relationship", "External relationship"],
            "answer": 1,
            "explanation": "Cohesion measures how closely related methods and data are within a class."
        },
        {
            "question": "What is coupling?",
            "options": ["Dependency between classes", "Independence", "Inheritance", "Polymorphism"],
            "answer": 0,
            "explanation": "Coupling measures degree of dependency between classes."
        },
        {
            "question": "What is friend function in C++?",
            "options": ["Member function", "Can access private members", "Static function", "Virtual function"],
            "answer": 1,
            "explanation": "Friend function can access private and protected members of a class."
        }
    ],
    "DBMS": [
        {
            "question": "Which normal form eliminates transitive dependency?",
            "options": ["1NF", "2NF", "3NF", "BCNF"],
            "answer": 2,
            "explanation": "Third Normal Form (3NF) removes transitive dependencies."
        },
        {
            "question": "What does ACID stand for in database transactions?",
            "options": ["Atomicity, Consistency, Isolation, Durability", 
                       "Accuracy, Consistency, Isolation, Dependency",
                       "Atomicity, Control, Isolation, Durability", 
                       "Accuracy, Control, Integration, Dependency"],
            "answer": 0,
            "explanation": "ACID properties ensure reliable database transactions: Atomicity, Consistency, Isolation, Durability."
        },
        {
            "question": "Which SQL command is used to remove a table?",
            "options": ["DELETE", "DROP", "REMOVE", "TRUNCATE"],
            "answer": 1,
            "explanation": "DROP command permanently removes a table and its structure from the database."
        },
        {
            "question": "What is a primary key?",
            "options": ["Can be NULL", "Uniquely identifies each record", 
                       "Can have duplicates", "Optional field"],
            "answer": 1,
            "explanation": "Primary key uniquely identifies each record and cannot be NULL or duplicate."
        },
        {
            "question": "Which join returns all records from both tables?",
            "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
            "answer": 3,
            "explanation": "FULL OUTER JOIN returns all records from both tables, matching where possible."
        },
        {
            "question": "What is denormalization?",
            "options": ["Adding redundancy for performance", "Removing data", "Creating tables", "Deleting records"],
            "answer": 0,
            "explanation": "Denormalization intentionally adds redundancy to improve query performance."
        },
        {
            "question": "What is a foreign key?",
            "options": ["Links two tables", "Primary identifier", "Unique constraint", "Index type"],
            "answer": 0,
            "explanation": "Foreign key creates a link between two tables by referencing primary key of another table."
        },
        {
            "question": "What is the purpose of indexing?",
            "options": ["Slow down queries", "Speed up data retrieval", "Delete data", "Update data"],
            "answer": 1,
            "explanation": "Indexing creates data structure to speed up data retrieval operations."
        },
        {
            "question": "What is a view in database?",
            "options": ["Physical table", "Virtual table", "Index", "Constraint"],
            "answer": 1,
            "explanation": "View is a virtual table based on result of SQL query."
        },
        {
            "question": "What is normalization?",
            "options": ["Adding redundancy", "Organizing data to reduce redundancy", "Deleting data", "Copying data"],
            "answer": 1,
            "explanation": "Normalization organizes data to minimize redundancy and dependency."
        },
        {
            "question": "Which is NOT an aggregate function?",
            "options": ["COUNT", "SUM", "AVG", "SELECT"],
            "answer": 3,
            "explanation": "SELECT is not an aggregate function; COUNT, SUM, AVG are aggregate functions."
        },
        {
            "question": "What is a trigger?",
            "options": ["Stored procedure", "Automatic action on event", "Index", "Constraint"],
            "answer": 1,
            "explanation": "Trigger is automatic action executed in response to certain events on table."
        },
        {
            "question": "What is TRUNCATE command?",
            "options": ["Deletes specific rows", "Removes all rows, keeps structure", "Drops table", "Updates data"],
            "answer": 1,
            "explanation": "TRUNCATE removes all rows from table but keeps the table structure."
        },
        {
            "question": "What is the difference between DELETE and TRUNCATE?",
            "options": ["No difference", "DELETE can use WHERE, TRUNCATE cannot", "Both same", "TRUNCATE slower"],
            "answer": 1,
            "explanation": "DELETE can remove specific rows using WHERE clause, TRUNCATE removes all rows."
        },
        {
            "question": "What is a stored procedure?",
            "options": ["View", "Precompiled SQL code", "Trigger", "Index"],
            "answer": 1,
            "explanation": "Stored procedure is precompiled collection of SQL statements stored in database."
        },
        {
            "question": "What is the purpose of GROUP BY?",
            "options": ["Sort data", "Group rows with same values", "Filter data", "Join tables"],
            "answer": 1,
            "explanation": "GROUP BY groups rows that have same values in specified columns."
        },
        {
            "question": "What is HAVING clause used for?",
            "options": ["Filter rows before grouping", "Filter groups after GROUP BY", "Join tables", "Sort data"],
            "answer": 1,
            "explanation": "HAVING filters groups after GROUP BY, unlike WHERE which filters before."
        },
        {
            "question": "What is a composite key?",
            "options": ["Single column key", "Multiple columns as key", "Foreign key", "Unique key"],
            "answer": 1,
            "explanation": "Composite key uses combination of two or more columns to uniquely identify row."
        },
        {
            "question": "What is UNION operator?",
            "options": ["Combines rows from queries", "Joins tables", "Filters data", "Sorts data"],
            "answer": 0,
            "explanation": "UNION combines result sets of two or more SELECT statements, removing duplicates."
        },
        {
            "question": "What is the difference between UNION and UNION ALL?",
            "options": ["No difference", "UNION removes duplicates, UNION ALL keeps them", "Both keep duplicates", "UNION faster"],
            "answer": 1,
            "explanation": "UNION removes duplicate rows, UNION ALL includes all rows including duplicates."
        },
        {
            "question": "What is referential integrity?",
            "options": ["Data accuracy", "Foreign key must match primary key", "Unique values", "No NULL values"],
            "answer": 1,
            "explanation": "Referential integrity ensures foreign key values match existing primary key values."
        },
        {
            "question": "What is a candidate key?",
            "options": ["Foreign key", "Potential primary key", "Composite key", "Unique key"],
            "answer": 1,
            "explanation": "Candidate key is minimal set of attributes that can uniquely identify tuple."
        },
        {
            "question": "What is super key?",
            "options": ["Primary key", "Set of attributes that uniquely identify tuple", "Foreign key", "Composite key"],
            "answer": 1,
            "explanation": "Super key is set of one or more attributes that uniquely identifies tuple."
        },
        {
            "question": "What is 1NF?",
            "options": ["No repeating groups", "No partial dependency", "No transitive dependency", "No multivalued dependency"],
            "answer": 0,
            "explanation": "First Normal Form requires atomic values and no repeating groups."
        },
        {
            "question": "What is 2NF?",
            "options": ["In 1NF and no repeating groups", "In 1NF and no partial dependency", "In 1NF and no transitive dependency", "No dependency"],
            "answer": 1,
            "explanation": "Second Normal Form is in 1NF and removes partial dependencies."
        },
        {
            "question": "What is BCNF?",
            "options": ["Same as 3NF", "Stricter version of 3NF", "Before 1NF", "After 4NF"],
            "answer": 1,
            "explanation": "BCNF (Boyce-Codd Normal Form) is stricter version of 3NF."
        },
        {
            "question": "What is isolation level?",
            "options": ["Security level", "Degree of transaction isolation", "Access level", "Performance level"],
            "answer": 1,
            "explanation": "Isolation level defines degree to which transactions are isolated from each other."
        },
        {
            "question": "What is deadlock in database?",
            "options": ["System crash", "Two transactions waiting for each other", "Lock timeout", "Database corruption"],
            "answer": 1,
            "explanation": "Deadlock occurs when two or more transactions wait indefinitely for each other."
        },
        {
            "question": "What is checkpoint in database?",
            "options": ["Backup point", "Point where changes are written to disk", "Restore point", "Transaction start"],
            "answer": 1,
            "explanation": "Checkpoint is point where database writes all changes from memory to disk."
        },
        {
            "question": "What is dirty read?",
            "options": ["Reading committed data", "Reading uncommitted data", "Reading old data", "Reading NULL data"],
            "answer": 1,
            "explanation": "Dirty read occurs when transaction reads uncommitted changes from another transaction."
        }
    ],
    "OS": [
        {
            "question": "Which scheduling algorithm can cause starvation?",
            "options": ["Round Robin", "FCFS", "Priority Scheduling", "SJF"],
            "answer": 2,
            "explanation": "Priority Scheduling can cause starvation where low-priority processes may never execute."
        },
        {
            "question": "What is a deadlock?",
            "options": ["Process waiting indefinitely", "CPU is idle", 
                       "Memory is full", "Disk failure"],
            "answer": 0,
            "explanation": "Deadlock is when processes wait indefinitely for resources held by each other."
        },
        {
            "question": "Which memory management technique divides process into fixed-size pages?",
            "options": ["Segmentation", "Paging", "Partitioning", "Swapping"],
            "answer": 1,
            "explanation": "Paging divides logical memory into fixed-size blocks called pages."
        },
        {
            "question": "What is thrashing?",
            "options": ["CPU running too fast", "Excessive page faults", 
                       "Disk corruption", "Network failure"],
            "answer": 1,
            "explanation": "Thrashing occurs when a system spends more time swapping pages than executing processes."
        },
        {
            "question": "Which algorithm is optimal for page replacement?",
            "options": ["FIFO", "LRU", "Optimal Page Replacement", "Random"],
            "answer": 2,
            "explanation": "Optimal Page Replacement (OPR) replaces the page that won't be used for longest time."
        },
        {
            "question": "What are the conditions for deadlock?",
            "options": ["Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait", 
                       "Only Mutual Exclusion", "Only Circular Wait", "None"],
            "answer": 0,
            "explanation": "All four conditions must hold simultaneously for deadlock to occur."
        },
        {
            "question": "What is a semaphore?",
            "options": ["Synchronization tool", "Memory allocation", "File system", "Network protocol"],
            "answer": 0,
            "explanation": "Semaphore is a synchronization tool used to control access to shared resources."
        },
        {
            "question": "What is the difference between process and thread?",
            "options": ["No difference", "Thread is lightweight process", "Process is lightweight", "Both same"],
            "answer": 1,
            "explanation": "Thread is lightweight process that shares memory space with other threads."
        },
        {
            "question": "What is context switching?",
            "options": ["Switching users", "Switching between processes", "Switching memory", "Switching files"],
            "answer": 1,
            "explanation": "Context switching is process of storing and restoring state of process or thread."
        },
        {
            "question": "What is virtual memory?",
            "options": ["Physical RAM", "Simulated memory using disk", "Cache memory", "ROM"],
            "answer": 1,
            "explanation": "Virtual memory uses disk space to simulate additional RAM."
        },
        {
            "question": "What is a critical section?",
            "options": ["Important code", "Code accessing shared resource", "Error code", "Startup code"],
            "answer": 1,
            "explanation": "Critical section is code segment that accesses shared resources."
        },
        {
            "question": "What is mutex?",
            "options": ["Multiple locks", "Mutual exclusion lock", "Memory unit", "Process state"],
            "answer": 1,
            "explanation": "Mutex is mutual exclusion lock ensuring only one thread accesses resource."
        },
        {
            "question": "What is the purpose of TLB?",
            "options": ["Store data", "Cache page table entries", "Store programs", "Network buffer"],
            "answer": 1,
            "explanation": "TLB (Translation Lookaside Buffer) caches page table entries for faster access."
        },
        {
            "question": "What is internal fragmentation?",
            "options": ["Wasted space within allocated block", "Wasted space between blocks", "No waste", "Disk fragmentation"],
            "answer": 0,
            "explanation": "Internal fragmentation is wasted space within allocated memory block."
        },
        {
            "question": "What is external fragmentation?",
            "options": ["Wasted space within block", "Wasted space between blocks", "No waste", "Cache fragmentation"],
            "answer": 1,
            "explanation": "External fragmentation is wasted free space scattered between allocated blocks."
        },
        {
            "question": "What is preemptive scheduling?",
            "options": ["Process runs till completion", "OS can interrupt running process", "No interruption", "Manual scheduling"],
            "answer": 1,
            "explanation": "Preemptive scheduling allows OS to interrupt and switch running process."
        },
        {
            "question": "What is non-preemptive scheduling?",
            "options": ["OS can interrupt", "Process runs till completion", "Random interruption", "Time-based"],
            "answer": 1,
            "explanation": "Non-preemptive scheduling runs process until completion or voluntary yield."
        },
        {
            "question": "What is a race condition?",
            "options": ["Fast execution", "Multiple processes accessing shared data", "CPU competition", "Memory race"],
            "answer": 1,
            "explanation": "Race condition occurs when multiple processes access shared data simultaneously."
        },
        {
            "question": "What is the purpose of page table?",
            "options": ["Store pages", "Map virtual to physical addresses", "Store data", "Cache memory"],
            "answer": 1,
            "explanation": "Page table maps virtual addresses to physical memory addresses."
        },
        {
            "question": "What is demand paging?",
            "options": ["Load all pages", "Load pages only when needed", "No paging", "Pre-load pages"],
            "answer": 1,
            "explanation": "Demand paging loads pages into memory only when they are needed."
        },
        {
            "question": "What is spooling?",
            "options": ["Direct I/O", "Simultaneous peripheral operations online", "Memory management", "Process scheduling"],
            "answer": 1,
            "explanation": "Spooling is simultaneous peripheral operations online, buffering I/O."
        },
        {
            "question": "What is the purpose of PCB?",
            "options": ["Physical memory", "Store process information", "Network protocol", "File system"],
            "answer": 1,
            "explanation": "PCB (Process Control Block) stores all information about a process."
        },
        {
            "question": "What is aging in OS?",
            "options": ["System slowdown", "Gradually increase priority", "Process termination", "Memory cleanup"],
            "answer": 1,
            "explanation": "Aging gradually increases priority of waiting processes to prevent starvation."
        },
        {
            "question": "What is the difference between logical and physical address?",
            "options": ["No difference", "Logical is virtual, physical is actual", "Both same", "Logical is faster"],
            "answer": 1,
            "explanation": "Logical address is generated by CPU, physical address is actual RAM location."
        },
        {
            "question": "What is a zombie process?",
            "options": ["Dead process", "Process completed but entry remains", "Sleeping process", "New process"],
            "answer": 1,
            "explanation": "Zombie process has completed execution but still has entry in process table."
        },
        {
            "question": "What is an orphan process?",
            "options": ["No parent", "Parent terminated before child", "Child terminated", "Idle process"],
            "answer": 1,
            "explanation": "Orphan process has parent process terminated before it."
        },
        {
            "question": "What is the role of dispatcher?",
            "options": ["Schedule processes", "Give CPU control to selected process", "Terminate process", "Create process"],
            "answer": 1,
            "explanation": "Dispatcher gives CPU control to process selected by scheduler."
        },
        {
            "question": "What is copy-on-write?",
            "options": ["Immediate copy", "Copy only when modified", "No copy", "Always copy"],
            "answer": 1,
            "explanation": "Copy-on-write delays copying until data is modified."
        },
        {
            "question": "What is belady's anomaly?",
            "options": ["More frames, fewer page faults", "More frames, more page faults", "No effect", "System crash"],
            "answer": 1,
            "explanation": "Belady's anomaly: increasing frames can increase page faults in FIFO."
        },
        {
            "question": "What is banker's algorithm used for?",
            "options": ["Scheduling", "Deadlock avoidance", "Memory allocation", "File management"],
            "answer": 1,
            "explanation": "Banker's algorithm is used for deadlock avoidance in resource allocation."
        }
    ],
    "CN": [
        {
            "question": "Which layer of OSI model handles routing?",
            "options": ["Data Link Layer", "Network Layer", "Transport Layer", "Session Layer"],
            "answer": 1,
            "explanation": "Network Layer (Layer 3) is responsible for routing and logical addressing."
        },
        {
            "question": "What is the size of an IPv4 address?",
            "options": ["16 bits", "32 bits", "64 bits", "128 bits"],
            "answer": 1,
            "explanation": "IPv4 addresses are 32 bits long, typically written as four octets."
        },
        {
            "question": "Which protocol is connection-oriented?",
            "options": ["UDP", "IP", "TCP", "ICMP"],
            "answer": 2,
            "explanation": "TCP (Transmission Control Protocol) is connection-oriented and ensures reliable delivery."
        },
        {
            "question": "What does DNS stand for?",
            "options": ["Domain Name System", "Direct Network Service", 
                       "Data Network System", "Domain Network Service"],
            "answer": 0,
            "explanation": "DNS (Domain Name System) translates domain names to IP addresses."
        },
        {
            "question": "Which device operates at the Data Link layer?",
            "options": ["Router", "Hub", "Switch", "Repeater"],
            "answer": 2,
            "explanation": "Switches operate at Data Link Layer (Layer 2) using MAC addresses."
        },
        {
            "question": "What is the maximum size of TCP segment?",
            "options": ["64 KB", "65,535 bytes", "1500 bytes", "No limit"],
            "answer": 1,
            "explanation": "Maximum TCP segment size is 65,535 bytes (limited by 16-bit length field)."
        },
        {
            "question": "Which protocol uses port 80?",
            "options": ["FTP", "SMTP", "HTTP", "SSH"],
            "answer": 2,
            "explanation": "HTTP (HyperText Transfer Protocol) uses port 80 by default."
        },
        {
            "question": "What is the size of IPv6 address?",
            "options": ["32 bits", "64 bits", "128 bits", "256 bits"],
            "answer": 2,
            "explanation": "IPv6 addresses are 128 bits long, written in hexadecimal."
        },
        {
            "question": "What is the purpose of ARP?",
            "options": ["IP to MAC mapping", "MAC to IP mapping", "DNS resolution", "Routing"],
            "answer": 0,
            "explanation": "ARP (Address Resolution Protocol) maps IP addresses to MAC addresses."
        },
        {
            "question": "Which layer is responsible for error detection?",
            "options": ["Physical", "Data Link", "Network", "Application"],
            "answer": 1,
            "explanation": "Data Link Layer detects and corrects errors in physical layer."
        },
        {
            "question": "What is the difference between TCP and UDP?",
            "options": ["No difference", "TCP reliable, UDP unreliable", "UDP reliable", "Both unreliable"],
            "answer": 1,
            "explanation": "TCP is reliable and connection-oriented, UDP is unreliable and connectionless."
        },
        {
            "question": "What is subnet mask?",
            "options": ["MAC address", "Network and host portion separator", "Gateway", "DNS server"],
            "answer": 1,
            "explanation": "Subnet mask separates network and host portions of IP address."
        },
        {
            "question": "What is the purpose of ICMP?",
            "options": ["File transfer", "Error reporting and diagnostics", "Email", "Web browsing"],
            "answer": 1,
            "explanation": "ICMP (Internet Control Message Protocol) reports errors and diagnostics."
        },
        {
            "question": "Which protocol is used for email sending?",
            "options": ["POP3", "IMAP", "SMTP", "HTTP"],
            "answer": 2,
            "explanation": "SMTP (Simple Mail Transfer Protocol) is used for sending emails."
        },
        {
            "question": "What is MAC address?",
            "options": ["Logical address", "Physical address", "IP address", "Port number"],
            "answer": 1,
            "explanation": "MAC (Media Access Control) address is unique physical address of network interface."
        },
        {
            "question": "What is the role of gateway?",
            "options": ["Connect same networks", "Connect different networks", "Filter packets", "Store data"],
            "answer": 1,
            "explanation": "Gateway connects different networks with different protocols."
        },
        {
            "question": "What is DHCP?",
            "options": ["Static IP assignment", "Dynamic IP assignment", "DNS service", "Routing protocol"],
            "answer": 1,
            "explanation": "DHCP (Dynamic Host Configuration Protocol) dynamically assigns IP addresses."
        },
        {
            "question": "What is the purpose of NAT?",
            "options": ["Translate private to public IP", "DNS resolution", "Routing", "Error checking"],
            "answer": 0,
            "explanation": "NAT (Network Address Translation) translates private to public IP addresses."
        },
        {
            "question": "Which layer handles data encryption?",
            "options": ["Physical", "Data Link", "Presentation", "Application"],
            "answer": 2,
            "explanation": "Presentation Layer (Layer 6) handles encryption and decryption."
        },
        {
            "question": "What is the maximum length of UTP cable?",
            "options": ["50 meters", "100 meters", "200 meters", "500 meters"],
            "answer": 1,
            "explanation": "Maximum recommended length for UTP (Unshielded Twisted Pair) is 100 meters."
        },
        {
            "question": "What is full form of FTP?",
            "options": ["Fast Transfer Protocol", "File Transfer Protocol", "Final Transport Protocol", "Fixed Transfer Protocol"],
            "answer": 1,
            "explanation": "FTP stands for File Transfer Protocol, used for file transfer."
        },
        {
            "question": "What is the difference between hub and switch?",
            "options": ["No difference", "Hub broadcasts, switch sends to specific port", "Switch broadcasts", "Both broadcast"],
            "answer": 1,
            "explanation": "Hub broadcasts to all ports, switch sends to specific destination port."
        },
        {
            "question": "What is TTL in IP packet?",
            "options": ["Transfer Time Limit", "Time To Live", "Total Transfer Length", "Type To Load"],
            "answer": 1,
            "explanation": "TTL (Time To Live) limits packet lifetime to prevent infinite loops."
        },
        {
            "question": "What is the purpose of firewall?",
            "options": ["Speed up network", "Filter and control network traffic", "Store data", "Assign IP"],
            "answer": 1,
            "explanation": "Firewall filters and controls incoming/outgoing network traffic based on rules."
        },
        {
            "question": "What is bandwidth?",
            "options": ["Cable width", "Data transfer capacity", "Signal strength", "Network size"],
            "answer": 1,
            "explanation": "Bandwidth is maximum data transfer rate of network or channel."
        },
        {
            "question": "What is latency?",
            "options": ["Bandwidth", "Delay in data transmission", "Error rate", "Packet size"],
            "answer": 1,
            "explanation": "Latency is time delay in transmitting data from source to destination."
        },
        {
            "question": "What is the purpose of SSL/TLS?",
            "options": ["Speed up connection", "Secure communication", "Compress data", "Route packets"],
            "answer": 1,
            "explanation": "SSL/TLS provides secure encrypted communication over network."
        },
        {
            "question": "What is VPN?",
            "options": ["Virtual Public Network", "Virtual Private Network", "Very Private Network", "Visual Private Network"],
            "answer": 1,
            "explanation": "VPN (Virtual Private Network) creates secure connection over public network."
        },
        {
            "question": "What is packet switching?",
            "options": ["Circuit based", "Data sent in packets", "Continuous connection", "Analog transmission"],
            "answer": 1,
            "explanation": "Packet switching breaks data into packets sent independently."
        },
        {
            "question": "What is the difference between LAN and WAN?",
            "options": ["No difference", "LAN is local, WAN is wide area", "WAN is faster", "LAN is wireless"],
            "answer": 1,
            "explanation": "LAN covers small area (local), WAN covers large geographical area."
        }
    ],
    "AI": [
        {
            "question": "Which search algorithm uses a heuristic function?",
            "options": ["BFS", "DFS", "A* Search", "Linear Search"],
            "answer": 2,
            "explanation": "A* Search uses a heuristic function to estimate the cost to reach the goal."
        },
        {
            "question": "What type of learning uses labeled data?",
            "options": ["Unsupervised Learning", "Supervised Learning", 
                       "Reinforcement Learning", "Random Learning"],
            "answer": 1,
            "explanation": "Supervised Learning uses labeled training data to learn patterns."
        },
        {
            "question": "Which is an example of unsupervised learning?",
            "options": ["Classification", "Regression", "Clustering", "Decision Trees"],
            "answer": 2,
            "explanation": "Clustering is unsupervised learning that groups similar data without labels."
        },
        {
            "question": "What is the Turing Test used for?",
            "options": ["Measuring computer speed", "Testing machine intelligence", 
                       "Network testing", "Database optimization"],
            "answer": 1,
            "explanation": "The Turing Test evaluates a machine's ability to exhibit intelligent behavior."
        },
        {
            "question": "Which activation function is commonly used in neural networks?",
            "options": ["Linear", "ReLU", "Constant", "None"],
            "answer": 1,
            "explanation": "ReLU (Rectified Linear Unit) is widely used due to its simplicity and effectiveness."
        },
        {
            "question": "What is overfitting in machine learning?",
            "options": ["Model performs well on training data but poorly on test data", 
                       "Model performs poorly on both", "Model is too simple", "Data is corrupted"],
            "answer": 0,
            "explanation": "Overfitting occurs when model learns training data too well, including noise."
        },
        {
            "question": "What is a neural network?",
            "options": ["Network of computers", "Computing system inspired by biological brain", 
                       "Internet protocol", "Database structure"],
            "answer": 1,
            "explanation": "Neural network is a computing system inspired by biological neural networks."
        },
        {
            "question": "What is backpropagation?",
            "options": ["Forward pass", "Algorithm to train neural networks", "Data preprocessing", "Activation function"],
            "answer": 1,
            "explanation": "Backpropagation is algorithm that trains neural networks by adjusting weights."
        },
        {
            "question": "What is gradient descent?",
            "options": ["Classification algorithm", "Optimization algorithm", "Clustering method", "Search algorithm"],
            "answer": 1,
            "explanation": "Gradient descent is optimization algorithm to minimize cost function."
        },
        {
            "question": "What is the difference between AI and ML?",
            "options": ["No difference", "AI is broader, ML is subset", "ML is broader", "Both same"],
            "answer": 1,
            "explanation": "AI is broader field, Machine Learning is a subset of AI."
        },
        {
            "question": "What is reinforcement learning?",
            "options": ["Supervised learning", "Learning through rewards and punishments", "Unsupervised learning", "Random learning"],
            "answer": 1,
            "explanation": "Reinforcement learning learns through interaction with environment using rewards."
        },
        {
            "question": "What is a decision tree?",
            "options": ["Neural network", "Tree-like model for decisions", "Clustering algorithm", "Linear model"],
            "answer": 1,
            "explanation": "Decision tree is tree-like model used for classification and regression."
        },
        {
            "question": "What is deep learning?",
            "options": ["Shallow networks", "Neural networks with many layers", "Simple ML", "Rule-based system"],
            "answer": 1,
            "explanation": "Deep learning uses neural networks with multiple hidden layers."
        },
        {
            "question": "What is cross-validation?",
            "options": ["Training method", "Model evaluation technique", "Feature selection", "Data collection"],
            "answer": 1,
            "explanation": "Cross-validation evaluates model performance by splitting data multiple ways."
        },
        {
            "question": "What is precision in ML?",
            "options": ["Total correct predictions", "True positives / (True positives + False positives)", "All predictions", "Random metric"],
            "answer": 1,
            "explanation": "Precision is ratio of true positives to all positive predictions."
        },
        {
            "question": "What is recall?",
            "options": ["Precision", "True positives / (True positives + False negatives)", "Accuracy", "F1 score"],
            "answer": 1,
            "explanation": "Recall is ratio of true positives to all actual positives."
        },
        {
            "question": "What is confusion matrix?",
            "options": ["Neural network", "Table showing prediction results", "Clustering method", "Optimization technique"],
            "answer": 1,
            "explanation": "Confusion matrix shows true vs predicted classifications."
        },
        {
            "question": "What is feature engineering?",
            "options": ["Model training", "Creating relevant features from raw data", "Testing", "Deployment"],
            "answer": 1,
            "explanation": "Feature engineering creates meaningful features from raw data."
        },
        {
            "question": "What is ensemble learning?",
            "options": ["Single model", "Combining multiple models", "Deep learning", "Clustering"],
            "answer": 1,
            "explanation": "Ensemble learning combines multiple models for better predictions."
        },
        {
            "question": "What is random forest?",
            "options": ["Single tree", "Ensemble of decision trees", "Neural network", "Clustering algorithm"],
            "answer": 1,
            "explanation": "Random forest is ensemble of decision trees."
        },
        {
            "question": "What is SVM?",
            "options": ["Support Vector Machine", "Simple Virtual Machine", "System Virtual Memory", "Scaled Vector Method"],
            "answer": 0,
            "explanation": "SVM (Support Vector Machine) is classification algorithm finding optimal hyperplane."
        },
        {
            "question": "What is K-means clustering?",
            "options": ["Supervised learning", "Partitioning data into K clusters", "Classification", "Regression"],
            "answer": 1,
            "explanation": "K-means partitions data into K clusters based on similarity."
        },
        {
            "question": "What is dimensionality reduction?",
            "options": ["Adding features", "Reducing number of features", "Data collection", "Model training"],
            "answer": 1,
            "explanation": "Dimensionality reduction reduces number of input features."
        },
        {
            "question": "What is PCA?",
            "options": ["Classification method", "Principal Component Analysis", "Clustering algorithm", "Activation function"],
            "answer": 1,
            "explanation": "PCA (Principal Component Analysis) reduces dimensions while preserving variance."
        },
        {
            "question": "What is the vanishing gradient problem?",
            "options": ["Gradient becomes too large", "Gradient becomes very small", "No gradient", "Random gradient"],
            "answer": 1,
            "explanation": "Vanishing gradient problem occurs when gradients become too small during backpropagation."
        },
        {
            "question": "What is transfer learning?",
            "options": ["Training from scratch", "Using pretrained model for new task", "Data transfer", "Model deployment"],
            "answer": 1,
            "explanation": "Transfer learning uses pretrained model as starting point for new task."
        },
        {
            "question": "What is batch normalization?",
            "options": ["Data preprocessing", "Normalizing inputs of each layer", "Activation function", "Loss function"],
            "answer": 1,
            "explanation": "Batch normalization normalizes inputs of each layer for faster training."
        },
        {
            "question": "What is dropout in neural networks?",
            "options": ["Adding neurons", "Randomly dropping neurons during training", "Removing layers", "Data augmentation"],
            "answer": 1,
            "explanation": "Dropout randomly drops neurons during training to prevent overfitting."
        },
        {
            "question": "What is CNN?",
            "options": ["Convolutional Neural Network", "Central Neural Network", "Complex Neural Network", "Circular Neural Network"],
            "answer": 0,
            "explanation": "CNN (Convolutional Neural Network) is primarily used for image processing."
        },
        {
            "question": "What is RNN?",
            "options": ["Random Neural Network", "Recurrent Neural Network", "Rapid Neural Network", "Real Neural Network"],
            "answer": 1,
            "explanation": "RNN (Recurrent Neural Network) is used for sequential data like text or time series."
        }
    ]
}