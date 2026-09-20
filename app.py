Tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento, comercial): ")
Consumo_mensal = float(input("Digite o consumo mensal de água em m³: "))
if Tipo_imovel == "comercial":
    print("consulte o plano corporativo.")
elif Tipo_imovel == "apartamento" and Consumo_mensal < 10:
    print("Consumo econômico – excelente controle de água!")
elif Tipo_imovel == "casa" or Tipo_imovel == "apartamento" and Consumo_mensal < 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")