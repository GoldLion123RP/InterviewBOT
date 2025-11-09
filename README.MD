# 🎓 CSE Interview Chatbot

A modern, interactive web-based interview preparation platform for Computer Science and Engineering students. Test your knowledge across 6 core CSE subjects with MCQ-based questions, real-time timer, and instant feedback.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [API Endpoints](#-api-endpoints)
- [Question Format](#-question-format)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [FAQ](#-faq)

---

## ✨ Features

### 🎯 Core Features
- **6 Core CSE Topics**: DSA, OOP, DBMS, OS, Computer Networks, AI
- **30 Questions per Topic**: Total of 180+ carefully curated questions
- **MCQ Format**: Multiple choice questions with 4 options each
- **Flexible Quiz Configuration**: Choose 1-30 questions per session
- **Mixed Topic Mode**: Select "ALL" to get questions from all topics
- **Real-time Timer**: Track your time with live countdown
- **Instant Feedback**: Get explanations after each answer
- **Score Analysis**: Detailed performance metrics with percentage
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Beautiful UI**: Modern gradient design with smooth animations

### 🚀 Advanced Features
- Timer warning at 5 minutes
- Progress tracking with visual progress bar
- Performance categorization (Excellent/Good/Average/Needs Improvement)
- Animated score circle with percentage display
- Question-by-question navigation
- Topic-wise color coding
- Session-based quiz management

---

## 🛠️ Technologies Used

### Backend
- **Flask** (v2.0+) - Python web framework
- **Python 3.8+** - Programming language

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern features (Flexbox, Grid, Animations)
- **JavaScript (ES6)** - Interactive functionality
- **Google Fonts (Poppins)** - Typography

### Tools
- **VS Code** - Code editor
- **Git** - Version control

---

## 📁 Project Structure

```
interview-chatbot/
│
├── app.py                      # Flask backend server
├── questions.py                # Question database (180+ questions)
│
├── templates/
│   └── index.html             # Main HTML template
│
├── static/
│   ├── style.css              # CSS styling
│   └── script.js              # JavaScript logic
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── .gitignore                 # Git ignore file
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/cse-interview-chatbot.git
cd cse-interview-chatbot
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
Flask==2.3.0
Werkzeug==2.3.0
```

### Step 4: Verify Installation
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🚀 Usage

### Starting the Application

1. **Activate virtual environment** (if using one)
2. **Run the Flask app:**
   ```bash
   python app.py
   ```
3. **Open browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### Using the Chatbot

#### Step 1: Select Topic
- Choose from **6 core topics** or select **"ALL TOPICS"** for mixed questions
- Topics include:
  - 🔢 DSA (Data Structures & Algorithms)
  - 🎯 OOP (Object-Oriented Programming)
  - 🗄️ DBMS (Database Management Systems)
  - 💻 OS (Operating Systems)
  - 🌐 CN (Computer Networks)
  - 🤖 AI (Artificial Intelligence)

#### Step 2: Configure Quiz
- Use the **slider** to select number of questions (1-30)
- Click **"Start Quiz"**

#### Step 3: Answer Questions
- Read the question carefully
- Click on your answer choice (A/B/C/D)
- Click **"Submit Answer"**
- View explanation and click **"Next Question"**

#### Step 4: View Results
- See your **score percentage**
- Review **correct/wrong answers**
- Check **time taken**
- Get **performance feedback**

### Stopping the Server
Press `Ctrl + C` in the terminal where Flask is running

---

## ⚙️ Configuration

### Changing Number of Questions
Edit in `templates/index.html`:
```html
<input type="range" id="numQuestions" min="1" max="30" value="10">
```
- **min**: Minimum questions (default: 1)
- **max**: Maximum questions (default: 30)
- **value**: Default selection (default: 10)

### Adding New Topics

1. **Add questions** to `questions.py`:
```python
questions_db = {
    # ... existing topics ...
    "ML": [  # New topic
        {
            "question": "What is Machine Learning?",
            "options": ["...", "...", "...", "..."],
            "answer": 0,
            "explanation": "..."
        }
    ]
}
```

2. **Update API** in `app.py`:
```python
topics = {
    # ... existing topics ...
    "ML": "Machine Learning"
}
```

3. **Add icon** in `static/script.js`:
```javascript
const topicIcons = {
    // ... existing icons ...
    'ML': '🧠'
};
```

### Customizing Timer Warning
Edit in `static/script.js`:
```javascript
// Warning at 5 minutes (300 seconds)
if (totalSeconds === 300) {
    document.querySelector('.timer-container').classList.add('warning');
}
```

### Changing Color Scheme
Edit CSS variables in `static/style.css`:
```css
:root {
    --primary: #6366f1;      /* Main color */
    --secondary: #8b5cf6;    /* Secondary color */
    --success: #10b981;      /* Success color */
    --danger: #ef4444;       /* Error color */
}
```

---

## 🔌 API Endpoints

### 1. Home Page
```
GET /
```
**Description:** Serves the main HTML page

**Response:** HTML document

---

### 2. Get Topics
```
GET /api/topics
```

**Description:** Returns list of available topics

**Response:**
```json
{
  "DSA": "Data Structures & Algorithms",
  "OOP": "Object-Oriented Programming",
  "DBMS": "Database Management Systems",
  "OS": "Operating Systems",
  "CN": "Computer Networks",
  "AI": "Artificial Intelligence"
}
```

**Example:**
```javascript
fetch('/api/topics')
    .then(response => response.json())
    .then(data => console.log(data));
```

---

### 3. Get Questions
```
POST /api/questions
```

**Description:** Returns random questions based on topic and count

**Request Body:**
```json
{
  "topic": "DSA",
  "num_questions": 10
}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| topic | string | Yes | Topic code or "ALL" |
| num_questions | integer | No | Number of questions (default: 5) |

**Response:**
```json
[
  {
    "question": "What is the time complexity of binary search?",
    "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
    "answer": 1,
    "explanation": "Binary search divides the search space...",
    "topic": "DSA"
  }
]
```

**Example:**
```javascript
fetch('/api/questions', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        topic: 'DSA',
        num_questions: 10
    })
})
.then(response => response.json())
.then(questions => console.log(questions));
```

---

## 📝 Question Format

### Question Object Structure

```python
{
    "question": "Question text here?",           # String: The question
    "options": [                                 # List: 4 answer choices
        "Option A",
        "Option B", 
        "Option C",
        "Option D"
    ],
    "answer": 2,                                 # Integer: Index of correct answer (0-3)
    "explanation": "Detailed explanation..."     # String: Why the answer is correct
}
```

### Example Question

```python
{
    "question": "What is the time complexity of binary search?",
    "options": [
        "O(n)",           # Index 0
        "O(log n)",       # Index 1 - Correct answer
        "O(n^2)",         # Index 2
        "O(1)"            # Index 3
    ],
    "answer": 1,  # Points to "O(log n)"
    "explanation": "Binary search divides the search space in half each time, resulting in O(log n) complexity."
}
```

### Adding New Questions

Edit `questions.py`:

```python
questions_db = {
    "DSA": [
        # ... existing questions ...
        {
            "question": "Your new question?",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": 0,  # Index of correct answer
            "explanation": "Explanation of the correct answer."
        }
    ]
}
```

**Important Notes:**
- Answer index is **0-based** (0, 1, 2, or 3)
- All questions must have exactly **4 options**
- Explanation should be **clear and educational**

---

## 📸 Screenshots

### Welcome Screen
![Welcome Screen](https://via.placeholder.com/800x400?text=Welcome+Screen)

### Topic Selection
![Topic Selection](https://via.placeholder.com/800x400?text=Topic+Selection)

### Quiz Interface
![Quiz Screen](https://via.placeholder.com/800x400?text=Quiz+Interface)

### Results Dashboard
![Results Screen](https://via.placeholder.com/800x400?text=Results+Dashboard)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### How to Contribute

1. **Fork the repository**
   ```bash
   git fork https://github.com/yourusername/cse-interview-chatbot.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make your changes**
   - Add new questions
   - Fix bugs
   - Improve UI/UX
   - Add new features

4. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

6. **Open a Pull Request**

### Contribution Ideas

- 📝 Add more questions to existing topics
- 🎨 Improve UI/UX design
- 🌐 Add new topics (Machine Learning, Cloud Computing, etc.)
- 🔧 Add difficulty levels (Easy/Medium/Hard)
- 📊 Add detailed analytics and progress tracking
- 🏆 Add leaderboard functionality
- 💾 Add user authentication and save progress
- 📱 Improve mobile responsiveness
- 🌍 Add multi-language support
- ♿ Improve accessibility features

### Code Style Guidelines

- Use **meaningful variable names**
- Add **comments** for complex logic
- Follow **PEP 8** for Python code
- Use **ES6** features for JavaScript
- Maintain **consistent indentation**
- Write **clear commit messages**

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 CSE Interview Chatbot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📧 Contact

**Project Maintainer:** Your Name

- GitHub: [@GoldLion123RP](https://github.com/GoldLion123RP)
- Email: goldlion123.rp@gmail.com
- LinkedIn: [https://www.linkedin.com/in/rahul-pal-133a67153/](https://www.linkedin.com/in/rahul-pal-133a67153/)

**Project Link:** [TAP TO OPEN](https://interviewbot-rqwq.onrender.com)

---

## 🙏 Acknowledgments

- Flask documentation
- Google Fonts (Poppins)
- Icons from emoji
- Inspiration from various online quiz platforms
- All contributors who helped improve this project

---

## 📌 Roadmap

### Version 1.0 (Current) ✅
- [x] Basic quiz functionality
- [x] 6 core CSE topics
- [x] 30 questions per topic
- [x] Timer feature
- [x] Score tracking
- [x] Responsive design

### Version 2.0 (Planned) 🚧
- [ ] User authentication
- [ ] Save progress
- [ ] Question difficulty levels
- [ ] Detailed analytics
- [ ] Leaderboard
- [ ] Practice mode

### Version 3.0 (Future) 🔮
- [ ] AI-powered question recommendations
- [ ] Video explanations
- [ ] Community-contributed questions
- [ ] Mobile app (React Native)
- [ ] Multi-language support

---

## 🐛 Known Issues

1. Timer doesn't pause when navigating away from page
2. No question review feature after quiz completion
3. Mobile landscape mode needs improvement

**Report bugs:** [Issues Page](https://github.com/yourusername/cse-interview-chatbot/issues)

---

## ❓ FAQ

### Q: Can I use this for commercial purposes?
**A:** Yes, this project is licensed under MIT License.

### Q: How do I add more questions?
**A:** Edit the `questions.py` file and add questions following the format shown in the documentation.

### Q: Does this store my quiz results?
**A:** No, currently results are not stored. This is a planned feature for v2.0.

### Q: Can I run this on a different port?
**A:** Yes, modify `app.py`: `app.run(debug=True, port=8080)`

### Q: Is this suitable for interview preparation?
**A:** Yes! It covers fundamental concepts for CSE interviews and placements.

---

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐!

---

<div align="center">

**Made with ❤️ by Computer Science Students**

**Happy Learning! 🎓**

[⬆ Back to Top](#-cse-interview-chatbot)

</div>