let botao = document.getElementById('botao-aba')
botao.addEventListener('click', aba)

//função para abrir a aba lateral
function aba(){
    let abaa = document.getElementById('aba_do_lado')
    // Verificar as dimensões reais com offsetWidth e offsetHeight
    let elementos = document.getElementById('elements')

    let trashboys_name_1 = document.getElementById('trashboys-h2')
    let pesquisa = document.getElementById('pesquisar')
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