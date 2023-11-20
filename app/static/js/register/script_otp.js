let botao_login = document.getElementById('botao-verificar'); //botão de login na aba de login
botao_login.addEventListener('mouseenter', passar_mouse);
botao_login.addEventListener('mouseout', sair_mouse);

function passar_mouse() {
    botao_login.style.backgroundColor = '#262e45';
    botao_login.style.boxShadow = '1px 1px 20px rgb(126, 126, 126)';
}

function sair_mouse() {
    botao_login.style.backgroundColor = '#2f3853';
    botao_login.style.boxShadow = 'none';
}