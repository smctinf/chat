//Haverá o código do index.html da aplicação chat
const $inputNameRoom = document.querySelector("#room-name-input");
const $roomForm = document.querySelector("#room-form");

$inputNameRoom.focus();

$roomForm.addEventListener("submit", event => {
    event.preventDefault();
    let roomName = $inputNameRoom.value;
    window.location.pathname = `/chat/${roomName}/`;
});