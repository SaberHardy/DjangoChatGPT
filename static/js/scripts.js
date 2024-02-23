const messageList = document.querySelector('.message-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    console.log(message);
    if (message.length === 0) {
        return;
    }
})