const apiUrl = 'http://localhost:8001';

function generateQuote(type) {
    fetch(`${apiUrl}/${type}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('quote-label').innerText = data.quote || "Ошибка получения цитаты.";
            playSound();
        })
        .catch(error => {
            console.error("Ошибка при получении цитаты:", error);
        });
}

function addWord(type) {
    const word = prompt(`Введите ${type}:`);
    if (word) {
        fetch(`${apiUrl}/add/${type}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ word: word })
        })
        .then(response => response.json())
        .then(data => {
            alert(`${type.charAt(0).toUpperCase() + type.slice(1)} '${word}' добавлено успешно!`);
        })
        .catch(error => {
            alert(`Ошибка при добавлении ${type}.`);
            console.error(error);
        });
    }
}

function playSound() {
    const audio = new Audio('/static/bezumno.mp3');
    audio.play();
}

function exitApp() {
    alert("Выход из приложения.");
}
