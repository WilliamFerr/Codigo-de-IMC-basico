# Codigo-de-IMC-basico
#Um codigo funcional de calculo IMC para trabalhos de faculdade

altura = float(input('qual sua altura? (lembre-se de separar com .)'))
peso = float(input('qual seu peso? '))
imc = (peso / (altura * altura))

if imc <= 18.5:
    print("Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
elif imc < 25:
	print("Você está Saudável.\nParabéns!")
elif imc < 30:
	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
elif imc < 35:
	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
elif imc < 40:
	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
else:
    print('preencha as informações corretamente.')
