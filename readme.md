Descrição
Você foi chamado para desenvolver um sistema de gerenciamento de estoque para uma loja de eletrônicos. O estoque inicial de pendrives é de 100 unidades. Cada vez que um cliente faz uma compra, o sistema deve calcular o estoque restante e aplicar descontos progressivos, seguindo as seguintes regras:

Se o cliente comprar até 5 pendrives, não há desconto.
Se o cliente comprar de 6 a 10 pendrives, recebe um desconto de 5% no valor total da compra.
Se o cliente comprar mais de 10 pendrives, recebe um desconto de 10% no valor total da compra.
O sistema que você vai desenvolver deve checar se existe estoque suficiente para atender ao pedido do cliente. Se o estoque for insuficiente, a compra não pode ser concluída. Foi informado à você que cada pendrive custa 5 reais.



Formato de entrada

Um número inteiro que define a quantidade de pendrives que o cliente irá comprar.

Formato de saída

O valor total X da compra, com duas casas decimais de aproximação.

A quantidade Y de pendrives restantes após a compra.

Se o saldo for suficiente, sua saíra deverá ser (sem as aspas):

"Ainda existe estoque! O valor total eh de R$ X e sobraram Y pendrives no estoque".

Se o saldo for insuficiente, sua saída deverá ser (sem as aspas):

"Poxa, nao temos mais pendrives no estoque"
