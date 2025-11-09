from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

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
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/topics', methods=['GET'])
def get_topics():
    topics = {
        "DSA": "Data Structures & Algorithms",
        "OOP": "Object-Oriented Programming",
        "DBMS": "Database Management Systems",
        "OS": "Operating Systems",
        "CN": "Computer Networks",
        "AI": "Artificial Intelligence"
    }
    return jsonify(topics)

@app.route('/api/questions', methods=['POST'])
def get_questions():
    data = request.json
    topic = data.get('topic')
    num_questions = data.get('num_questions', 5)
    
    if topic == 'ALL':
        all_questions = []
        for t, questions in questions_db.items():
            for q in questions:
                q_copy = q.copy()
                q_copy['topic'] = t
                all_questions.append(q_copy)
        random.shuffle(all_questions)
        selected = all_questions[:num_questions]
    else:
        questions = questions_db.get(topic, [])
        selected = random.sample(questions, min(num_questions, len(questions)))
        for q in selected:
            q['topic'] = topic
    
    return jsonify(selected)

if __name__ == '__main__':
    app.run(debug=True)