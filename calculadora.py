Nome = input("Como posso te chamar? ")
print("Olá", Nome, "! Vamos supor que você esteja vendendo doces e precisa juntar 300 reais. Aqui, vou te ajudar a saber quantos itens terá que vender para atingir esta marca")

Brigadeiro = float(input("Digite o valor do brigadeiro "))

if Brigadeiro <= 3:
  print("Este brigadeiro é muito barato. Por favor, aumente o preço")
else:
  print() 
Brownie = float(input("Digite o valor do brownie  "))

if Brownie <= 5:
  print("Este brownie é muito barato. Por favor, aumente o preço")
else:
  print()
Cocada = float(input("Digite o valor da Cocada "))

if Cocada <= 4:
  print("Muito barato. Aumente o valor")
else:
  print()
Rapadura = float(input("Digite o valor da Rapadura "))

if Rapadura <= 6:
  print("Muito barato. Aumente o valor")
else:
  print()


print("Quantos produtos eu preciso vender para atingir R$100 reais de cada item? ")

print("Para juntar R$100 em Brigadeiro, você precisa vender", int (100 / Brigadeiro), "unidades")

print("Para juntar R$100 em Brownie, você precisa vender", int (100 / Brownie), "unidades")

print("Para juntar R$100 em Cocada, você precisa vender", int (100 / Cocada), "unidades")

print("Para juntar R$100 em Rapadura, você precisa vender", int (100 / Rapadura), "unidades")
