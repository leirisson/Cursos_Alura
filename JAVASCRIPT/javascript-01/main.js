function toca_pom(){
    document.querySelector('#som_tecla_pom').play();
}
const listaDeTeclas =  document.querySelectorAll('.tecla');
listaDeTeclas[0].onclick = toca_pom;