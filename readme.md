# 🌼 Ekul em Busca da Flor

Ekul é um pequeno e corajoso cachorro em uma missão muito importante: encontrar uma flor especial em um campo florido. Mas, como todo cãozinho, ele também é um pouco preguiçoso... só sai de casa se estiver bem disposto!

Este projeto simula as condições necessárias para Ekul sair em busca da flor e determina se ele tem ou não chance de encontrá-la, com base em variáveis como estação do ano, clima, horário e tempo de sono.

## 🐾 Regras da Aventura

- A **disposição** de Ekul depende do seu tempo de sono:
  \[
  \text{DISPOSIÇÃO} = \frac{2 \times \text{TEMPO DE SONO (horas)}}{1}
  \]
  Ele só sai de casa se a disposição for **maior ou igual a 70**.

- Se Ekul sair de casa, a **chance de encontrar a flor** é calculada por:
  \[
  \text{CHANCE} = \text{VALOR DA ESTAÇÃO} + (\text{HORÁRIO (h)} \mod \text{CLIMA}) \times \text{TEMPO DE SONO}
  \]

  Onde:
  - **Clima**: `E` = 7 (Ensolarado), `C` = 5 (Chuvoso), `N` = 3 (Nublado)

- A flor só nasce se:
  \[
  \text{CHANCE} \geq \text{VALOR DA ESTAÇÃO} \times 3
  \]

- Caso a chance de encontrar ultrapasse 100%, ela é arredondada para **100%**.

## 📥 Formato de Entrada

- Linha 1: Dois inteiros → `horario_em_minutos` `horas_de_sono`
- Linha 2: Dois caracteres → `estacao` (`I`, `V`, `P`, `O`) e `clima` (`E`, `C`, `N`)
- Linha 3: Quatro inteiros → valores das estações: Inverno, Verão, Primavera, Outono

## 📤 Formato de Saída

Uma linha com a chance de encontrar a flor (em porcentagem), seguida por:

- `"Ekul nao acordou disposto hoje :("`
- `"Ekul possui chances de encontrar a flor :)"`
- `"Ekul nao possui chances de encontrar a flor :("`

## 💡 Exemplos

### Entrada
