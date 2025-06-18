# 🃏 Duelo de Cartas - Jogo Simplificado

Este repositório contém uma versão **simplificada** do jogo "Armague", criada para ajudar estudantes iniciantes em programação a praticarem os conceitos de **entrada e saída de dados, funções, condicionais e lógica de decisão**.

---

## 🧠 Objetivo

Dois jogadores, **Pedro** e **Túlio**, vão duelar com **uma carta cada**. Cada carta possui:

- **Ataque** (número inteiro)
- **Vida** (número inteiro)

O objetivo do programa é determinar quem vence o duelo, seguindo as regras abaixo.

---

## ⚔️ Regras do Duelo

1. A carta com **menos vida** ataca primeiro.
2. Se ambas tiverem **a mesma vida**, **Pedro** ataca primeiro.
3. O ataque **diminui a vida do oponente** pelo valor do ataque.
4. Se o oponente **sobreviver (vida > 0)**, ele **revida** com um ataque.
5. Após no máximo dois ataques (um de cada), o duelo termina.

---

## 🏆 Como Determinar o Vencedor

- Se **um dos jogadores morrer (vida <= 0)** após os ataques, o outro vence.
- Se **ninguém morrer**, vence quem tiver **mais vida restante**.

---

## 📥 Entrada Esperada

O programa deve solicitar:

```
Ataque de Pedro: <valor>
Vida de Pedro: <valor>
Ataque de Túlio: <valor>
Vida de Túlio: <valor>
```

---

## 📤 Exemplo de Saída

```
Túlio venceu o duelo!
```

---

## 💡 Conceitos Trabalhados

- Funções
- Leitura de dados com `input()`
- Conversão de dados com `int()`
- Estruturas condicionais `if`, `else`
- Lógica de combate simples

---
