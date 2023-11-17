let login_header = document.getElementById('login_header'); //login do header
login_header.addEventListener('mouseenter', passar_mouse_login_header);
login_header.addEventListener('mouseout', sair_mouse_login_header);

function passar_mouse_login_header() {
    login_header.style.color = '#cbcdd4';
}

function sair_mouse_login_header() {
    login_header.style.color = 'white';
}

let signin_header = document.getElementById('signin-header'); //sign-in do header
signin_header.addEventListener('mouseenter', passar_mouse_signin_header);
signin_header.addEventListener('mouseout', sair_mouse_signin_header);

function passar_mouse_signin_header() {
    signin_header.style.color = '#cbcdd4';
}

function sair_mouse_signin_header() {
    signin_header.style.color = 'white';
}

let botao_login = document.getElementById('botao-login'); //botão de login na aba de login
botao_login.addEventListener('mouseenter', passar_mouse);
botao_login.addEventListener('mouseout', sair_mouse);

function passar_mouse() {
    botao_login.style.backgroundColor = '#262e45';
}

function sair_mouse() {
    botao_login.style.backgroundColor = '#2f3853';
}
