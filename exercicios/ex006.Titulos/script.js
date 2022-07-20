//Esse script cuida da section mudando a cor de branco para vermelho. 
h1 = window.document.querySelector('h1#h1')
h1.addEventListener('mouseenter',entrar)
h1.addEventListener('mouseout',sair)

function entrar(){
    h1.style.color = "red"
}

function sair(){
    h1.style.color = 'white'
}

//Esse script vai cuida do título da reportagem.
h2 = window.document.querySelector('h1#h2')
h2.addEventListener('mouseenter',entrar2)
h2.addEventListener('mouseout',sair2)

function entrar2(){
    h2.style.color = 'blue'
    
}

function sair2(){
    h2.style.color = '#6d6d6df0'
}
