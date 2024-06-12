#teste

salario_minimo = float(input('digite o valor do seu salario: '))
desconto_INSS = 10
salario_liquido = salario_minimo - desconto_INSS

emregado = input('Voce e empregado?: ')

if emregado == 'sim' and salario_minimo >= 1000:
    print('o seu valor para emprestimo foi aprovado com base em',salario_minimo)
    if salario_minimo >= 1000:
        print('com o valor do desconto',desconto_INSS, 'seu salario ficou em', salario_liquido)
    else:
        print('seu valor para emprestimo nao foi aprovado por motivos de que seu salario e baixo')
else:
    print('nao aprovado')
    



    

    
