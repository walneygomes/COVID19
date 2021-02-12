taxa_maxima=100

def calculo_taxa(valor_x, contaminado_y ):
     valor= (valor_x*taxa_maxima)/contaminado_y
     return valor
    

def calculo_perce(valor_x, valor_y):
    return (valor_x*valor_y)/taxa_maxima


contaminado= int(input("digite o numero contaminado"))

txObitos=calculo_taxa(int(input("digite o numero de obitos")), contaminado) 
 
txRecuperados= calculo_taxa(int(input("digite o numero de obitos")), contaminado)
 
print(" Taxa de Mortalidade " , txObitos, "%")
print(" Taxa de Recuperados ", txRecuperados, "%")
print(" Casos ativo ", int(contaminado-calculo_perce(contaminado, txObitos)- calculo_perce(contaminado,txRecuperados)))



