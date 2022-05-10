print("Este código resolve Equações de Segundo Grau.\n")

a = int(input("Insira o valor de a: ")) 
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: ")) 
            
if (a == 0):
        print("0 no valor de a é inválido para uma Equação de Segundo Grau")
else:
                
        delta = (b * b) - 4 * (a) * (c)
                
        print(delta)
                
        if(delta < 0):
            print("O Delta é Negativo, a equação não possui raízes reais")
        elif(delta == 0):
            raiz_de_delta = round(pow(delta, 0.5),3)
            x_positivo = -(b) +(raiz_de_delta) / (2 * a)
            print("O resultado é somente positovo devido ao deltar ser 0, o resultado é {:.4f}".format(x_positivo))
        else:
            raiz_de_delta = round(pow(delta, 0.5),3)
            print(raiz_de_delta)
            x_positivo = (-(b) +(raiz_de_delta)) /  (2 * a)
            x_negativo = (-(b) -(raiz_de_delta)) /  (2 * a)
            print("Os resultados são:", "Delta Negativo = {:.4f}".format(x_negativo), "Delta Positivo = {:.4f}".format(x_positivo), sep = "\n")             