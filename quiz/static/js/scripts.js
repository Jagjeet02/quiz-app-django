let sessionId = null;
let currentQuestionId = null;

// Start Quiz
document.getElementById("startQuiz").addEventListener("click", function () {
    fetch("/quiz/start/")
        .then(response => response.json())
        .then(data => {
            sessionId = data.session_id;
            document.getElementById("sessionInfo").innerText = `Session ID: ${sessionId}`;
            fetchQuestion();
        })
        .catch(error => alert("Failed to start the quiz. Please try again."));
});

// Fetch Question
function fetchQuestion() {
    fetch(`/quiz/question/${sessionId}/`)
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                fetchSummary();
                return;
            }
            displayQuestion(data);
            currentQuestionId = data.id;
        })
        .catch(error => alert("Error fetching question."));
}

// Display Question
function displayQuestion(data) {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = `
        <p><strong>${data.question}</strong></p>
        ${Object.entries(data.options).map(([key, value]) => `
            <div>
                <input type="radio" name="option" value="${key}" id="option-${key}">
                <label for="option-${key}">${key}: ${value}</label>
            </div>
        `).join('')}
        <button id="submitAnswer">Submit Answer</button>
    `;

    document.getElementById("submitAnswer").addEventListener("click", submitAnswer);
}

// Submit Answer
function submitAnswer() {
    const selectedOption = document.querySelector("input[name='option']:checked");
    if (!selectedOption) {
        alert("Please select an option!");
        return;
    }
    fetch(`/quiz/answer/${sessionId}/${currentQuestionId}/?option=${selectedOption.value}`)
        .then(() => fetchQuestion())
        .catch(error => alert("Error submitting answer."));
}

// Fetch Summary
function fetchSummary() {
    fetch(`/quiz/summary/${sessionId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("quiz-container").innerHTML = `
                <h3>Quiz Summary</h3>
                <p>Total Questions: ${data.total}</p>
                <p>Correct Answers: ${data.correct}</p>
                <p>Incorrect Answers: ${data.incorrect}</p>
            `;
        })
        .catch(error => alert("Error fetching quiz summary."));
}
