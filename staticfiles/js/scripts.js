let sessionId = null;
let currentQuestionId = null;

// Start Quiz: Fetch session ID
document.getElementById("startQuiz").addEventListener("click", function () {
    fetch("/quiz/start/")
        .then(response => response.json())
        .then(data => {
            sessionId = data.session_id;
            document.getElementById("sessionInfo").innerText = `Session ID: ${sessionId}`;
            fetchQuestion();
        })
        .catch(error => {
            console.error("Error starting quiz:", error);
            alert("Failed to start the quiz. Please try again.");
        });
});

// Fetch a random question
function fetchQuestion() {
    fetch(`/quiz/question/${sessionId}/`)
        .then(response => response.json())
        .then(data => {
            if (!data.question) {
                fetchSummary(); // No questions left, show the summary
                return;
            }
            displayQuestion(data);
            currentQuestionId = data.id;
        })
        .catch(error => {
            console.error("Error fetching question:", error);
            alert("Error fetching question. Please try again.");
        });
}

// Display the question and options
function displayQuestion(data) {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = `
        <p><strong>${data.question}</strong></p>
        ${Object.keys(data.options).map(key => `
            <div class="option">
                <input type="radio" name="option" value="${key}" id="option-${key}">
                <label for="option-${key}">${key}: ${data.options[key]}</label>
            </div>
        `).join('')}
        <button id="submitAnswer">Submit Answer</button>
    `;

    document.getElementById("submitAnswer").addEventListener("click", submitAnswer);
}

// Submit selected answer
function submitAnswer() {
    const selectedOption = document.querySelector("input[name='option']:checked");
    if (!selectedOption) {
        alert("Please select an option!");
        return;
    }

    fetch(`/quiz/answer/${sessionId}/${currentQuestionId}/?option=${selectedOption.value}`)
        .then(() => fetchQuestion()) // Fetch the next question
        .catch(error => {
            console.error("Error submitting answer:", error);
            alert("Error submitting answer. Please try again.");
        });
}

// Fetch and display quiz summary
function fetchSummary() {
    fetch(`/quiz/summary/${sessionId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("quiz-container").innerHTML = `
                <h2>Quiz Summary</h2>
                <p>Total Questions: ${data.total}</p>
                <p>Correct Answers: ${data.correct}</p>
                <p>Incorrect Answers: ${data.incorrect}</p>
                <button onclick="window.location.reload()">Start New Quiz</button>
            `;
        })
        .catch(error => {
            console.error("Error fetching summary:", error);
            alert("Error fetching quiz summary.");
        });
}
