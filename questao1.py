populacao_campina=400*1000

def calculo_vacina(vacinados):
    return (vacinados*1000)/populacao_campina
    
porcentagemVacinados= calculo_vacina(float(input(" numero de vacinados")))
print("porcentagemVacinados de vacinados", porcentagemVacinados, "%")
