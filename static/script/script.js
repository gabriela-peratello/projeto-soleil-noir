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

        const cards = document.querySelectorAll('.card-produtos')


        cards.forEach(card => {

            const categoriaCard = card.getAttribute('data-categoria')


            if (categoriaSelecionada === 'todos' || categoriaCard == categoriaSelecionada){
                card.style.display = 'block'
            } else{
                card.style.display = 'none'
            }
        })


        
    })
})

const botaoAbrir = document.getElementById('btnCarrinho')
const botaoFechar = document.getElementById('btnFechar')
const carrinho = document.getElementById('janelaCarrinho')


botaoAbrir.addEventListener('click', () =>{
    carrinho.classList.add('aberto')
}
)


botaoFechar.addEventListener('click', () =>{
    carrinho.classList.remove('aberto')
})

