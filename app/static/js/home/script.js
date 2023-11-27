let botao = document.getElementById('botao-aba')
botao.addEventListener('click', aba)

//variável menu
let img_menu = document.getElementById('menu-img')
img_menu.addEventListener('mouseenter', mouseEntrarMenu)
img_menu.addEventListener('mouseout', mouseSairMenu)

//variável sino
let img_sino = document.getElementById('sino-img')
img_sino.addEventListener('mouseenter', mouseEntrarSino)
img_sino.addEventListener('mouseout', mouseSairSino)

//variável perfil
let img_perfil = document.getElementById('foto-perfil-img')
img_perfil.addEventListener('mouseenter', mouseEntrarPerfil)
img_perfil.addEventListener('mouseout', mouseSairPerfil)

//variável musicas 1
let img_wallpaper_music = document.querySelectorAll('.msc-1')
img_wallpaper_music.forEach(function(img) {
    img.querySelectorAll("*").forEach(function(child) {
      child.addEventListener('mouseenter', mouseEntrarMusic)
      child.addEventListener('mouseout', mouseSairMusic)
    })
  })

//variável musicas 2
let img_wallpaper_music2 = document.querySelectorAll('.msc-2')
img_wallpaper_music2.forEach(function(img) {
    img.querySelectorAll("*").forEach(function(child) {
      child.addEventListener('mouseenter', mouseEntrarMusic2)
      child.addEventListener('mouseout', mouseSairMusic2)
    })
  })

//função menu
function mouseEntrarMenu(){
    img_menu.style.boxShadow = '1px 1px 20px rgb(126, 126, 126)';
    img_menu.style.backgroundColor = 'rgb(50, 50, 50)'
    img_menu.style.borderRadius = '50%'
}
function mouseSairMenu(){
    img_menu.style.boxShadow = 'none';
    img_menu.style.backgroundColor = ''
    img_menu.style.borderRadius = '0%'
}

//função sino
function mouseEntrarSino(){
    img_sino.style.boxShadow = '1px 1px 20px rgb(126, 126, 126)';
    img_sino.style.backgroundColor = 'rgb(60, 60, 60)'
    img_sino.style.borderRadius = '50%'
}
function mouseSairSino(){
    img_sino.style.boxShadow = 'none';
    img_sino.style.backgroundColor = ''
    img_sino.style.borderRadius = '0%'
}

//função perfil
function mouseEntrarPerfil(){
    img_perfil.style.boxShadow = '1px 1px 20px rgb(126, 126, 126)';
    img_perfil.style.backgroundColor = 'rgb(50, 50, 50)'
    img_perfil.style.borderRadius = '50%'
}
function mouseSairPerfil(){
    img_perfil.style.boxShadow = 'none';
    img_perfil.style.backgroundColor = ''
}

//variável musica 1
function mouseEntrarMusic(){
    this.style.boxShadow = '1px 1px 20px rgb(126, 126, 126)';
    this.style.backgroundColor = 'rgb(87, 87, 87)'
    this.style.borderRadius = '5px'
}

function mouseSairMusic(){
    this.style.boxShadow = 'none';
    this.style.backgroundColor = ''
    this.style.borderRadius = '5px'
}

//variável musica 2
function mouseEntrarMusic2(){
    this.style.boxShadow = '1px 1px 20px rgb(126, 126, 126)';
    this.style.backgroundColor = 'rgb(87, 87, 87)'
    this.style.borderRadius = '5px'
}

function mouseSairMusic2(){
    this.style.boxShadow = 'none';
    this.style.backgroundColor = ''
    this.style.borderRadius = '5px'
}


//função para abrir a aba lateral
function aba(){
    let abaa = document.getElementById('aba_do_lado')
    // Verificar as dimensões reais com offsetWidth e offsetHeight
    let elementos = document.getElementById('elements')

    let trashboys_name_1 = document.getElementById('trashboys-h2')
    let pesquisa = document.getElementById('pesquisar')

    //variável home
    let home_page = document.getElementById('botao-home')
    let home1 = document.getElementById('home')

    //variável follow
    let following_botao = document.getElementById('botao-following')
    let following1 = document.getElementById('following')

    let menuu = document.getElementById('menu')
    let lista_reprod = document.getElementById('playlist')
    let rec = document.getElementById('recentes')

    if(abaa.offsetWidth == 0 || abaa.offsetHeight == 0){
        abaa.style.width = '400px'
        abaa.style.height = '800px'
        /*
        botao.innerHTML = 'fechar'
        */
        pesquisa.style.width = '195px'
        pesquisa.style.height = '35px'
        menuu.style.width = '240px'
        menuu.style.height = '80px'
        lista_reprod.style.width = '240px'
        lista_reprod.style.height = '250px'
        rec.style.width = '240px'
        rec.style.height = '250px'
        trashboys_name_1.innerHTML = 'Trashboys'
        abaa.style.overflowY = 'scroll'
        elementos.style.height = '850px'
        elementos.style.width = '292px'

        //função aba
        let principal = document.getElementById('pag-principal')

        abaa.addEventListener('wheel', function(e){
            e.preventDefault();
            e.stopPropagation();
            abaa.scrollTop += e.deltaY;
        })

        principal.addEventListener('wheel', function(e) {
            e.preventDefault();
            e.stopPropagation();
            principal.scrollTop += e.deltaY;
        })

        //chamar função home
        home_page.addEventListener('mouseenter', mouseEntrarHome)
        home_page.addEventListener('mouseout', mouseSairHome)

        //chamar função following
        following_botao.addEventListener('mouseenter', mouseEntrarFollow)
        following_botao.addEventListener('mouseout', mouseSairFollow)

        //função home
        function mouseEntrarHome(){
            home1.style.backgroundColor = 'rgb(87, 87, 87)'
        }
        function mouseSairHome(){
            home1.style.backgroundColor = '#373737'
        }

        //função follow
        function mouseEntrarFollow(){
            following1.style.backgroundColor = 'rgb(87, 87, 87)'
        }
        function mouseSairFollow(){
            following1.style.backgroundColor = '#373737'
        }

    } else{
        abaa.style.width = '0px'
        abaa.style.height = '0%'
        /*
        botao.innerHTML = 'abrir'
        */
        pesquisa.style.width = '0px'
        pesquisa.style.height = '0px'
        menuu.style.width = '0px'
        menuu.style.height = '0px'
        lista_reprod.style.width = '0px'
        lista_reprod.style.height = '0px'
        rec.style.width = '0px'
        rec.style.height = '0px'
        trashboys_name_1.innerHTML = ''
        elementos.style.height = '0px'
        elementos.style.width = '0px'
    }
}