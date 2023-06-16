//Taking by DOM the name of the room to create the WebSocket
const roomName = JSON.parse(document.querySelector("#room_name").textContent)

//Defining the chat's WebSocket.
const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}`);

console.log(chatSocket);

//Logic to receive messages
chatSocket.addEventListener("message", event => {
    const data = JSON.parse(event.data);
    document.querySelector("#chat-box").value += `${data.message} \n`;
});

//Logic to close the connection
chatSocket.addEventListener("close", event => {
    console.error("The WebSocket socked unexpectedly");
});

const $chatInput = document.querySelector("#chat-message");
const $chatForm = document.querySelector("#chat-form");

$chatInput.focus();

//Logic to send a message when the $chatForm is submitted.
$chatForm.addEventListener("submit", event => {
    event.preventDefault();

    const message = $chatInput.value;
    chatSocket.send(JSON.stringify({
        "message": message
    }));

    $chatInput.value = "";
});

