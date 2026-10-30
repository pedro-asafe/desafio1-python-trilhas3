# 🛒 Sistema de Caixa (PDV) - Descontos em Cascata

## 📌 O que o código faz
Este projeto é um sistema simples de Ponto de Venda (PDV) desenvolvido em Python. Ele tem como objetivo registrar compras consecutivas, aplicar regras de desconto automáticas baseadas na idade do cliente, no valor da compra e na quantidade de itens comprados, e, ao final da execução, gerar um resumo financeiro completo detalhando o total bruto, os descontos concedidos e o valor líquido arrecadado.

## ⚙️ Como funciona (Lógica do Sistema)
1. O código inicia um loop de atendimento e recebe o valor da compra, validando se é um número positivo (ou `0` para encerrar o caixa).
2. Recebe e valida a quantidade de produtos e a idade do cliente.
3. **Desconto por idade:** Verifica se a idade é maior ou igual a 65 anos para aplicar **20%** de desconto.
4. **Desconto por valor:** Verifica se o valor parcial (já com o desconto de idade) passa de R$ 100,00 para aplicar mais **10%** de desconto.
5. **Desconto por quantidade:** Verifica se a quantidade de produtos é maior que 3 para aplicar **5%** de desconto extra.
6. Guarda os dados dessa compra (valor original, desconto total e valor final) em uma lista.
7. Ao digitar `0` no valor, o programa encerra o loop, soma tudo o que foi guardado na lista e exibe um resumo financeiro da sessão.

## 🚀 Como rodar o projeto

**Pré-requisitos:** Ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.

1. Clone este repositório ou baixe o arquivo `pdv.py`.
2. Abra o terminal na pasta onde o arquivo está salvo.
3. Execute o comando abaixo:

```bash
python pdv.py
```
## 📊 Tabela de Casos de Teste (Exemplos)
![Tabela de casos de testes](https://drive.google.com/file/d/1SpO7nI7Z8y-msWl2wW7gIJe0Z5QlCf2n/view?usp=drive_link)
