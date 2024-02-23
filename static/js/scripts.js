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

    const messageItem = document.createElement('div');
    messageItem.classList.add('card', 'sent');

    messageItem.innerHTML = `
        <div class="message-text">
            <div class="message-sender">
                <b>You</b>
            </div>
            <div class="message-content">
                ${message}
            </div>
        </div>`;
    messageList.appendChild(messageItem);
    messageInput.value = '';
})