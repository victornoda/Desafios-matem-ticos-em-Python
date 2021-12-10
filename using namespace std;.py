N = int(input())

for i in range(0, N):
     placa = str(input())
     contador = len(placa)
     if contador != 8:
         print('FALHA')
     else:
         if not(placa[:3].isalpha() and placa[3] == '-' and placa[4:8].isnumeric()):
             print('FALHA')
         else:
           if str(placa.isupper()) == 'False':
             print('FALHA')
           else:
             indicador = int(placa[7])
             if indicador==1 or indicador==2:
                 print('SEGUNDA')
             elif indicador==3 or indicador==4:
                 print('TERCA')
             elif indicador==5 or indicador==6:
                 print('QUARTA')
             elif indicador==7 or indicador==8:
                 print('QUINTA')
             elif indicador==9 or indicador==0:
                 print('SEXTA')
