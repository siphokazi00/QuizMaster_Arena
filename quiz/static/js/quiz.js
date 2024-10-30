/*document.addEventListener('DOMContentLoaded', () => {
	const questions = {{ questions|safe }};

	export function displayQuiz() {
		const quizContainer = document.getElementById("quiz-container");
		quizContainer.innerHTML = "";

		questions.forEach((question, index) => {
			const questionDiv = document.createElement("div");
			questionDiv.innerHTML = `
			<h3>${index + 1}. ${question.question.text}</h3>
			${question.answers.map((answer, i) => `
			<button onclick="checkAnswer(${i}, '${question.correctAnswer}')">${answer}</button>
			`).join("")}
			`;
			quizContainer.appendChild(questionDiv);
		});
	}*/

	export function checkAnswer(selectedAnswer, correctAnswer) {
		alert(selectedAnswer === correctAnswer ? "Correct!" : "Incorrect!");
	}

	displayQuiz();

	export function checkAnswer(button, selectedAnswer, correctAnswer) {
            // Disable all buttons for this question after answering
            const buttons = button.parentNode.querySelectorAll('.answer-button');
            buttons.forEach(btn => btn.disabled = true);

            // Mark the selected button as correct or incorrect
            if (selectedAnswer === correctAnswer) {
                button.classList.add('correct');
            } else {
                button.classList.add('incorrect');
            }
        }
