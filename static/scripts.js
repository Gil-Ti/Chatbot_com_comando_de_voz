const voiceButton = document.getElementById("voice_button");
const userInput = document.getElementById("user_input");


if (window.SpeechRecognition || window.webkitSpeechRecognition) {
    let SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition = new SpeechRecognition();

    voiceButton.addEventListener("click", () => {
        recognition.start();
    });

    recognition.addEventListener("result", (event) => {
        let transcript = event.results[0][0].transcript;
        userInput.value = transcript;
        document.querySelector("form").submit();
    });
} else {
    voiceButton.remove();
    console.log("API de reconhecimento de fala não suportada pelo navegador.");
}
