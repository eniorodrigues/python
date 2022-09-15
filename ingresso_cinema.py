from ast import Break
from pickle import TRUE
from unicodedata import numeric

def noturno(hora, minuto):
    if(hora < 24 and minuto < 61):
        if(hora < 18):
            return False 
        elif(hora == 18 and minuto <= 30):
            return False  
        elif(hora >= 18 or minuto > 30):
            return True 
        elif(hora >= 18 and hora <=24 and minuto <=60):
            return True  
        else:
            Break
            return "ERRO HORARIO"
    else:
        Break
        return "ERRO HORA MINUTO"

def dinheiro(tipo_dinheiro):
    if(tipo_dinheiro.upper() == "D"):
        return True 
    elif(tipo_dinheiro.upper() == "C"):
        return False
    else:
        return "ERRO dinheiro"

def estudante(tipo):
    if(tipo.upper() == "S"):
        return True 
    elif(tipo.upper() == "N"):
        return False
    else:
        return "ERRO TIPO estudante"

valores_noturnos = {
    "1": 30,
    "2": 20,
    "3": 20,
    "4": 30,
    "5": 30,
    "6": 40,
    "7": 40
}

valores_vespertinos ={
    "1": 30,
    "2": 15,
    "3": 15,
    "4": 15,
    "5": 20,
    "6": 20,
    "7": 30
}

def valor_inteira(noturno, dia):
    if(noturno):
        dia = str(dia)
        return float(valores_noturnos[dia])
    else:
        dia = str(dia)
        return float(valores_vespertinos[dia])

valor_inteira(True, 2)

def valor_reduzido(noturno, dia):
    if(noturno == True):
        dia = int(dia)
        if(dia > 1 and dia < 6):
            dia = str(dia)
            return valores_noturnos[dia] * 0.5
        elif(dia == 1 or dia == 6):
            dia = str(dia)
            return valores_noturnos[dia] * 0.7
        elif(dia == 7):
            dia = str(dia)
            return valores_noturnos[dia] * 0.8
        else:
            return "Erro valor_reduzido noturno"
    elif(noturno == False):
        dia = int(dia)
        if(dia > 1 and dia < 7):
            dia = str(dia)
            return valores_vespertinos[dia] * 0.5
        elif(dia == 1):
            dia = str(dia)
            return valores_vespertinos[dia] * 0.7
        elif(dia == 7):
            dia = str(dia)
            return valores_vespertinos[dia] * 0.8
        else:
            return "Erro valor_reduzido vespertinos"
    else:
        return "Erro valor_reduzido"

def valor_meia_inteira(tipo_estudante, noturno, dia):
    if(tipo_estudante.upper() == "S"):
        if(noturno == True):
            return valores_noturnos[dia] / 2
        elif(noturno == False):
            return valores_vespertinos[dia] / 2
        else:
            return "Erro valor_meia_inteira tipo estudante S" 
    elif(tipo_estudante.upper() == "N"):
        return valor_inteira(noturno,dia)
    else:
         return "Erro valor_meia_inteira tipo estudante N"
         
print(" Qual Dia da semana da sessão? ")
print(" Domingo - Digite: 1 ")
print(" Segunda-feira - Digite: 2 ")
print(" Terça-feira  - Digite: 3 ")
print(" Quarta-feira - Digite: 4 ")
print(" Quinta-feira - Digite: 5 ")
print(" Sexta-feira - Digite: 6 ")
print(" Sábado - Digite: 7 ")
dia = input()
dia = str(dia)
print(" <Hora do horário da sessão> ")
hora = input()
hora = int(hora)
print(" <Minuto do horário da sessão> ")
minuto = input()
minuto = int(minuto)
print(" < Estudante: Sim / Não > S / N ")
tipo_estudante = input()
print(" < Método de pagamento: Dinheiro / Cartão > D / C ")
tipo_dinheiro = input()

if(tipo_estudante.upper() == "S"):
    print(valor_meia_inteira(tipo_estudante,noturno(hora, minuto), dia))
elif(tipo_dinheiro.upper() == "C"):
    print(valor_reduzido(noturno(hora,minuto),dia))
else:
    print(valor_inteira(noturno(hora, minuto), dia))
        

# def valor_ingresso(dia, dinheiro, noturno , estudante):
#     if(dia==1 and noturno==False and dinheiro==False and estudante==False):
#         return  float(valores_vespertinos["1"]) * 0.7
#     elif(dia==1 and noturno==False and dinheiro==False and estudante==True):
#         return  float(valores_vespertinos["1"])/2
#     elif(dia==1 and noturno==False and dinheiro==True and estudante==True):
#         return  float(valores_vespertinos["1"])/2
#     elif(dia==1 and noturno==False and dinheiro==True and estudante==False):
#         return float(valores_vespertinos["1"])
#     elif(dia==1 and noturno==True and dinheiro==False and estudante==False):
#         return valores_noturnos["1"] * 0.7
#     elif(dia==1 and noturno==True and dinheiro==True and estudante==False):
#         return valores_noturnos["1"] 
#     elif(dia==1 and noturno==True and dinheiro==True and estudante==True):
#         return float(valores_noturnos["1"])/2
#     elif(dia==1 and noturno==True and dinheiro==False and estudante==True):
#         return float(valores_noturnos["1"])/2
#     else:
#         return "ERRO VALOR INGRESS"
