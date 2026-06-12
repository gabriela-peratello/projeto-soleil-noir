 const carousel = document.getElementById('carousel');

        function scrollLeftCards() {
            carousel.scrollBy({
                left: -300,
                behavior: 'smooth'
            });
        }
        function scrollRightCards() {
            carousel.scrollBy({
                left: 300,
                behavior: 'smooth'
            });
        }


document.querySelectorAll('.dropdown-item').forEach(opcao => {
    opcao.addEventListener('click', (evento) =>{

        const categoriaSelecionada = opcao.getAttribute('data-filtro')

        
    })
})

