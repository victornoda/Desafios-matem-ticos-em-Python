#Desafio

O rodízio de veículos de Bravoos é uma restrição à circulação de veículos na cidade.
Com o propósito de melhorar as condições ambientais reduzindo a carga de poluentes na atmosfera,
incluindo na região de Westeros, se consolidou como um instrumento para reduzir congestionamentos
nas principais vias da cidade, nos horários de maior movimento. Nas ruas delimitadoras não é permitido
o tráfego de cavalos e carruagens que estejam dentro da restrição. Há uma escala que determina em quais
dias da semana quais veículos não podem circular. Essa escala é regida pelo último dígito da placa do
animal, sendo:

Segunda-feira, digito final da placa 1 e 2
Terça-feira, digito final da placa 3 e 4
Quarta-feira, digito final da placa 5 e 6
Quinta-feira, digito final da placa 7 e 8
Sexta-feira, digito final da placa 9 e 0
Os motoristas que são flagrados violando a restrição de circulação são autuados com multa de 4 galinhas e condenados a passar 1 semana na Muralha.

Entrada
A primeira linha de entrada representa a quantidade de testes N (0 <= N < 1000) que deverão ser considerados.
As demais entradas são cadeia de caracteres com tamanho máximo S (1 <= S <= 100) que representam cada placa que
deverá ser analisada, de tal forma que, cada placa fique em uma única linha de entrada. O formato esperado para
uma placa veicular válida em Bravoos é "AAA-9999", tal que A é um caracter válido em [A-Z], e 9 um dígito numérico
válido em [0-9].

Saída
O conjunto de valores válidos como saída são: SEGUNDA, TERCA, QUARTA, QUINTA e SEXTA, de acordo com a tabela de
restrições predefinida, e FALHA caso a placa não apresente o padrão definido.

        
        
        
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
