const lista = [
    { produto: 'TV', preco: 2300 },
    { produto: 'Geladeira', preco: 2750 },
    { produto: 'Fogão', preco: 950 },
    { produto: 'Lava-louça', preco: 1800 },
    { produto: 'Lava-roupa', preco: 1790 },
    { produto: 'Microondas', preco: 560 }
]

const novaLista = lista.filter((item) => item.preco <= 1000) // retorna os items da lista que tem preço abaixo de 1000
console.log(novaLista)

const nomesLista = lista.map((item) => item.produto)  // retorna uma lista apenas com os nomes dos produtos
console.log(`Nomes dos produtos ${nomesLista}`)

const itemFind = lista.find((item) => item.produto ='TV') // procura um produto especifico
console.log(itemFind)

lista.forEach( item => console.log(item)) // loga cada item da array individualmente

const produtosCaros =  lista.some( item => item.preco > 2300 )  // verifica se a array possui ao menos um item com preço acima de 2300
const produtosBaratos =  lista.some( item => item.preco < 100 )  // verifica se a array possui ao menos um item com preço abaixo de 100
console.log(produtosCaros)
console.log(produtosBaratos)

console.log(lista.every( item => item.preco > 2000)) // testa se todos os preços são maiores do que 2000

const precoTotal = lista.reduce( (totalParcial, item) => totalParcial + item.preco, 0)
console.log(precoTotal) // 10150

numbers = [10, 55, 63, 74, 98, 47, 14, 27, 79, 64]
console.log(numbers.includes(74)) // true
console.log(numbers.includes(97)) // false
