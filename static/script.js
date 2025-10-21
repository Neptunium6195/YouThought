function scroll() {
    const chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
}
window.onload = scroll;
function showFollowUps() {
    const divFollowUps = document.getElementById('follow-ups');
    divFollowUps.style.display = 'flex';
}
function hideFollowUp() {
    const divFollowUps = document.getElementById('follow-ups');
    divFollowUps.style.display = 'none'; 
}
function sendFollowUp(type) {
    document.getElementById('followUp-input').value = type;
    document.querySelector('#followUp-form').submit();
    const btn = document.getElementById('regenerateButton');
    btn.style.display = 'flex';
    hideFollowUp();
    scroll();
    showFollowUps();
}
function regenerate() {
    const form = document.getElementById('regenerate-form');
    if (form) form.submit();
}