# Bases Numéricas

Um projeto de terminal em Python pra converter números entre bases diferentes (de base 2 até base 36) e fazer operações matemáticas direto em binário. Comecei isso pra treinar lógica e acabou virando um projetinho completo, com menu, modo de prática e até um tutorial explicando cada conta na mão.

## O que dá pra fazer

- **Converter qualquer número de uma base pra outra**, de base 2 até base 36 (sim, com letras de A a Z pras bases acima de 10).
- **Praticar conversões**, com números aleatórios pra você tentar resolver na mão antes de ver a resposta.
- **Fazer contas em binário** — soma, subtração, multiplicação e divisão — sem precisar converter nada, só digitando os números já em binário.
- **Ler o tutorial de cada método**, se você (como eu) sempre esquece como faz a divisão sucessiva ou a separação em grupos de 3/4 bits.

Tudo isso rodando num menu de terminal com tabelas usando a biblioteca [rich](https://github.com/Textualize/rich).

## Como rodar

```bash
python main.py
```

Ou clicando no executável em que está na pasta dist.

## Estrutura do projeto

```
.
├── main.py                  # ponto de entrada, só chama o menu principal
└── funcoes/
    ├── menus.py              # navegação entre os menus
    ├── conversor.py          # conversão universal entre bases + tutorial + modo prática
    └── operacoes_binarias.py # calculadora de operações em base 2 + tutorial + modo prática
```

A ideia foi separar cada responsabilidade num arquivo diferente em vez de jogar tudo num script só, deixando mais fácil de mexer e de entender o que cada parte faz.

## Detalhes técnicos

- O conversor universal funciona com **qualquer par de bases** entre 2 e 36 (não só as convencionais 2/8/10/16), fazendo a conversão em duas etapas por baixo dos panos: base de origem → base 10 → base de destino.
- Validação de erros feita com exceção própria (`NumeroInvalidoError`), então números com dígitos inválidos pra base escolhida são pegos antes de qualquer conta ser feita.

## Por que fiz isso

Eu queria treinar Python de um jeito que não fosse só exercício solto, mas completo, com validação de erro de verdade, menus, e alguma coisa que eu pudesse mostrar no portfólio. Decidi fazer com base numérica pois é um dos conteúdos que estou vendo atualmente na faculdade.