salario = float(input("qual seu salario"))

if salario <= 2000.00:
  print("vc esta isento")
elif salario >= 2000.01 and salario <= 3000.00:
  print("seu desconto sera de 8%")
  desconto = salario * 0.08
  print("seu desconto será de: ", desconto)
  print("seu salario liquido será de: ", salario - desconto)
elif salario >= 3000.01 and salario <= 4500.00:
  print("seu desconto será de 18%")
  desconto = salario * 0.18
  print("seu desconto será de: ", desconto)
  print("seu salario liquido será de: ", salario - desconto)
elif salario >= 4500.00:
  print("seu desconto será de 28%")
  desconto = salario * 0.28
  print("seu desconto será de: ", desconto)
  print("seu salario liquido será de: ", salario - desconto)