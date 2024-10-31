console.log("quiz.js loaded");

// Initialize variables
let timeLeft = 10;
let countdown;
let score = 0; // Score counter
const totalQuestions = 5; // Set the total number of questions in the quiz
let questionNumber = 1; // Track current question number

const timerDisplay = document.getElementById("time-left");
const timeoutMessage = document.getElementById("timeout-message");
const answerButtons = document.querySelectorAll(".answer-button");

// Start the timer when the page loads
window.onload = function () {
    startTimer();
};

// Timer countdown function
function startTimer() {
    clearInterval(countdown); // Clear any previous timer
    timeLeft = 10; // Reset time for each question
    timerDisplay.textContent = timeLeft;

    countdown = setInterval(() => {
        timeLeft -= 1;
        timerDisplay.textContent = timeLeft;

        // If time runs out
        if (timeLeft <= 0) {
            clearInterval(countdown);
            endQuestion(); // Handle timeout
        }
    }, 1000);
}

// Function to end the question if time runs out
function endQuestion() {
    timeoutMessage.style.display = "block"; // Show "Time's up!" message
    disableAnswers();
    setTimeout(nextQuestion, 2000); // Move to the next question after 2 seconds
}

// Handle answer selection
function selectAnswer(button, correctAnswer) {
    clearInterval(countdown); // Stop the timer once an answer is selected

    // Show feedback for the selected answer
    if (button.innerText === correctAnswer) {
        button.classList.add("correct");
        score += 1; // Increase score if the answer is correct
    } else {
        button.classList.add("incorrect");
        // Highlight the correct answer
        answerButtons.forEach(btn => {
            if (btn.innerText === correctAnswer) {
                btn.classList.add("correct");
            }
        });
    }

    disableAnswers(); // Disable all answer buttons after selection
    setTimeout(nextQuestion, 2000); // Wait 2 seconds before loading the next question
}

// Disable all answer buttons
function disableAnswers() {
    answerButtons.forEach(button => {
        button.disabled = true;
    });
}

// Load the next question or show final score
function nextQuestion() {
    timeoutMessage.style.display = "none"; // Hide "Time's up!" message
    answerButtons.forEach(button => {
        button.classList.remove("correct", "incorrect"); // Reset button colors
        button.disabled = false; // Re-enable buttons
    });

    questionNumber += 1; // Move to the next question

    if (questionNumber > totalQuestions) {
        // End of quiz, show final score
        showFinalScore();
    } else {
        // Placeholder to actually load the next question
        // This can be replaced with an actual API call or backend logic to fetch the next question
        window.location.reload(); // Temporary reload to simulate question change
    }
}

// Show the final score to the user
function showFinalScore() {
    document.body.innerHTML = `<div class="score-container">
        <h2>Quiz Completed!</h2>
        <p>Your Score: ${score} out of ${totalQuestions}</p>
        <button onclick="restartQuiz()" class="btn">Play Again</button>
    </div>`;
}

// Function to restart the quiz
function restartQuiz() {
    score = 0; // Reset score
    questionNumber = 1; // Reset question number
    window.location.reload(); // Reload the page to start from the beginning
}
