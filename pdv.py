compras = [];

#prints inicias
print("======== Sistema de Caixa ========");
print("Digite 0 para encerrar o programa e ver resumo. \n");

while True:
    #entrada de valor da compra
    valor = float(input("Digite o valor da compra: R$"));

    #validação do valor digitado
    if valor == 0:
        break;
    
    if valor < 0:
        print("Valor inválido. Digite um valor positivo (maior que 0).");
        continue;

    #quantidade de produtos
    quantidade_produtos = int(input("Digite a quantidade de produtos: "));
    if quantidade_produtos <= 0:
        print("Quantidade inválida. Digite uma quantidade positiva (maior que 0).");
        quantidade_produtos = int(input("Digite a quantidade de produtos: "))

    #entrada da idade e validação
    idade = int(input("Digite a idade do cliente: "));
    if idade < 0:
        print("Idade inválida. Digite uma idade positiva (maior que 0).");
        idade = int(input("Digite a idade do cliente: "))

    #desconto baseado na idade
    valor_parcial = valor;
    if idade >= 65:
        valor_parcial *= 0.8;

    #desconto baseado no valor da compra
    valor_final = valor_parcial;
    if valor_parcial > 100:
        valor_final *= 0.9;

    if quantidade_produtos > 3:
        valor_final *= 0.95;

    print(f"\n== Valor da compra: R${valor_final:.2f} ==\n");

    desconto = valor - valor_final;

    #adiciona a compra na lista
    compras.append([valor, desconto, valor_final]);

#Resumo Final
print("\n======== Resumo das Compras ========");

quantidade_compras = len(compras);

if quantidade_compras > 0:       
    #Criando variáveis para armazenar os totais
    total_bruto = 0
    total_desconto = 0 
    total_final = 0

    for compra in compras:
        total_bruto += compra[0];
        total_desconto += compra[1];
        total_final += compra[2];
    
    print(f"Quantidade de compras: {quantidade_compras}");
    print(f"Total bruto: R${total_bruto:.2f}");
    print(f"Total de descontos: R${total_desconto:.2f}");
    print(f"Total final: R${total_final:.2f}");
else:
    print("Nenhuma compra registrada.");
