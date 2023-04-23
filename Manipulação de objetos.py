'''
#Como manipular objetos em python 
#Como criar e modificar arquivos

# 'r'  - usado somente para ler algo
# 'w'  - usado somente para escever algo
# 'r+' - usado para ler e escrever algo 
# 'a'  - usado para acrecentar algo

'''

valores_celulares = [1100, 200, 900, 4000, 960]

#with open('valores_celulares.txt','w') as arquivo:
    #for valor in valores_celulares:
    #arquivo.write(str(valor) + '\n')

#with open('valores_celulares.txt','a') as arquivo:
    #for valor in valores_celulares:
    #arquivo.write(str(valor) + '\n')      

#with open('valores_celulares.txt','r') as arquivo:
    #for valor in arquivo:
        #print(valor)                  

with open('valores_celulares.txt','r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('100000000')                        