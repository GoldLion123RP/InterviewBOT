let currentTopic = '';
let questions = [];
let currentQuestionIndex = 0;
let selectedAnswer = null;
let score = 0;
let userAnswers = [];

const topicIcons = {
    'DSA': '🔢',
    'OOP': '🎯',
    'DBMS': '🗄️',
    'OS': '💻',
    'CN': '🌐',
    'AI': '🤖'
};

// Screen Navigation
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    document.getElementById(screenId).classList.add('active');
}

function showWelcome() {
    showScreen('welcomeScreen');
    resetQuiz();
}

function showTopicSelection() {
    loadTopics();
    showScreen('topicScreen');
}

function showConfig(topic) {
    currentTopic = topic;
    const topicNames = {
        'DSA': 'Data Structures & Algorithms',
        'OOP': 'Object-Oriented Programming',
        'DBMS': 'Database Management Systems',
        'OS': 'Operating Systems',
        'CN': 'Computer Networks',
        'AI': 'Artificial Intelligence',
        'ALL': 'All Topics (Mixed)'
    };
    document.getElementById('selectedTopicName').textContent = topicNames[topic];
    showScreen('configScreen');
}

// Load Topics
async function loadTopics() {
    try {
        const response = await fetch('/api/topics');
        const topics = await response.json();
        
        const topicGrid = document.getElementById('topicGrid');
        topicGrid.innerHTML = '';
        
        // Add individual topics
        for (const [code, name] of Object.entries(topics)) {
            const card = document.createElement('button');
            card.className = 'topic-card';
            card.onclick = () => showConfig(code);
            card.innerHTML = `
                <span class="topic-icon">${topicIcons[code]}</span>
                <div class="topic-code">${code}</div>
                <div class="topic-name">${name}</div>
            `;
            topicGrid.appendChild(card);
        }
        
        // Add "All Topics" option
        const allCard = document.createElement('button');
        allCard.className = 'topic-card';
        allCard.onclick = () => showConfig('ALL');
        allCard.style.gridColumn = 'span 2';
        allCard.innerHTML = `
            <span class="topic-icon">📚</span>
            <div class="topic-code">ALL TOPICS</div>
            <div class="topic-name">Mixed Questions</div>
        `;
        topicGrid.appendChild(allCard);
        
    } catch (error) {
        console.error('Error loading topics:', error);
    }
}

// Question Count Slider
document.addEventListener('DOMContentLoaded', () => {
    const slider = document.getElementById('numQuestions');
    const count = document.getElementById('questionCount');
    
    if (slider) {
        slider.addEventListener('input', (e) => {
            count.textContent = e.target.value;
        });
    }
});

// Start Quiz
async function startQuiz() {
    const numQuestions = parseInt(document.getElementById('numQuestions').value);
    
    try {
        const response = await fetch('/api/questions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                topic: currentTopic,
                num_questions: numQuestions
            })
        });
        
        questions = await response.json();
        currentQuestionIndex = 0;
        score = 0;
        userAnswers = [];
        
        showScreen('quizScreen');
        loadQuestion();
        
    } catch (error) {
        console.error('Error starting quiz:', error);
    }
}

// Load Question
function loadQuestion() {
    if (currentQuestionIndex >= questions.length) {
        showResults();
        return;
    }
    
    const question = questions[currentQuestionIndex];
    selectedAnswer = null;
    
    // Update progress
    document.getElementById('questionNumber').textContent = 
        `Question ${currentQuestionIndex + 1}/${questions.length}`;
    document.getElementById('currentTopic').textContent = question.topic;
    
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    document.getElementById('progressFill').style.width = progress + '%';
    
    // Update question
    document.getElementById('questionText').textContent = question.question;
    
    // Update options
    const optionsContainer = document.getElementById('optionsContainer');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, index) => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'option';
        optionDiv.onclick = () => selectOption(index);
        optionDiv.innerHTML = `
            <div class="option-letter">${String.fromCharCode(65 + index)}</div>
            <div class="option-text">${option}</div>
        `;
        optionsContainer.appendChild(optionDiv);
    });
    
    document.getElementById('submitBtn').disabled = true;
}

// Select Option
function selectOption(index) {
    selectedAnswer = index;
    
    document.querySelectorAll('.option').forEach((opt, i) => {
        opt.classList.toggle('selected', i === index);
    });
    
    document.getElementById('submitBtn').disabled = false;
}

// Submit Answer
function submitAnswer() {
    if (selectedAnswer === null) return;
    
    const question = questions[currentQuestionIndex];
    const isCorrect = selectedAnswer === question.answer;
    
    if (isCorrect) {
        score++;
    }
    
    userAnswers.push({
        question: question.question,
        userAnswer: selectedAnswer,
        correctAnswer: question.answer,
        isCorrect: isCorrect
    });
    
    // Show explanation
    showExplanation(isCorrect, question.explanation);
}

// Show Explanation
function showExplanation(isCorrect, explanation) {
    const resultIcon = document.getElementById('resultIcon');
    const resultText = document.getElementById('resultText');
    
    if (isCorrect) {
        resultIcon.textContent = '✅';
        resultText.textContent = 'Correct!';
        resultText.style.color = 'var(--success)';
    } else {
        resultIcon.textContent = '❌';
        resultText.textContent = 'Incorrect!';
        resultText.style.color = 'var(--danger)';
    }
    
    document.getElementById('explanationText').textContent = explanation;
    showScreen('explanationScreen');
}

// Next Question
function nextQuestion() {
    currentQuestionIndex++;
    showScreen('quizScreen');
    loadQuestion();
}

// Show Results
function showResults() {
    const total = questions.length;
    const correct = score;
    const wrong = total - correct;
    const percentage = (correct / total * 100).toFixed(1);
    
    document.getElementById('totalQuestions').textContent = total;
    document.getElementById('correctAnswers').textContent = correct;
    document.getElementById('wrongAnswers').textContent = wrong;
    document.getElementById('scorePercentage').textContent = percentage + '%';
    
    // Animate score circle
    const circumference = 2 * Math.PI * 90;
    const offset = circumference - (percentage / 100 * circumference);
    document.getElementById('scoreCircle').style.strokeDashoffset = offset;
    
    // Performance message
    const messageDiv = document.getElementById('performanceMessage');
    if (percentage >= 80) {
        messageDiv.textContent = '🌟 Excellent! You have strong knowledge!';
        messageDiv.style.background = 'rgba(16, 185, 129, 0.1)';
        messageDiv.style.color = 'var(--success)';
    } else if (percentage >= 60) {
        messageDiv.textContent = '👍 Good job! Keep practicing!';
        messageDiv.style.background = 'rgba(59, 130, 246, 0.1)';
        messageDiv.style.color = '#3b82f6';
    } else if (percentage >= 40) {
        messageDiv.textContent = '📖 Not bad! More study needed!';
        messageDiv.style.background = 'rgba(245, 158, 11, 0.1)';
        messageDiv.style.color = 'var(--warning)';
    } else {
        messageDiv.textContent = '💪 Keep learning! Practice makes perfect!';
        messageDiv.style.background = 'rgba(239, 68, 68, 0.1)';
        messageDiv.style.color = 'var(--danger)';
    }
    
    showScreen('resultsScreen');
}

// Reset Quiz
function resetQuiz() {
    currentTopic = '';
    questions = [];
    currentQuestionIndex = 0;
    selectedAnswer = null;
    score = 0;
    userAnswers = [];
    document.getElementById('numQuestions').value = 5;
    document.getElementById('questionCount').textContent = '5';
}