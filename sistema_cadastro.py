# -*- coding: utf-8 -*-
"""
Sistema de Cadastro

@author: Ramon Moratori
"""

#Sistema de Cadastro Usando Listas

#Lista com todos os cadastrados
listageral = []

# ID (0), Nome (1), Idade (2), Genero (3), Email (4)
cadastro = []

while(1):
    
    #Ver O Banco de Dados Ou Cadastrar?
    menu = input('Digite "1" para ver o banco de dados, "2" para cadastrar e "3" para editar um cadastro e "4" para sair: ')
    
    if menu == '1': 
        #Printa o banco de dados 
        print ('Banco de Dados:')
        print (' ')
        
        for n in range(0, len(listageral)):
            #Faz um loop exibindo cada elemento da lista
            print ('Pessoa', n + 1, ': ', listageral[n])
        
    
    elif menu == '2':
        #Inicia o cadastro
        nome = input('Digite seu Nome: ')
        idade = input('Digite sua Idade: ')
        genero = input('Digite seu genero (M ou F): ')
        email = input('Digite seu email: ')
        
        ID = len(listageral) + 1
        #Coloca os dados dentro da lista 'Cadastro'
        cadastro = [ID, nome, idade, genero, email]

        #Coloca o cadastro na lista geral
        listageral.append(cadastro)
        
    elif menu == '3':
        #Edita algum elemento da lista geral
        editar = int(input('Digite a ID da pessoa a ser editada: '))
        
        print('Vamos refazer o cadastro: ')
        
        nome = input('Digite seu Nome: ')
        idade = input('Digite sua Idade: ')
        genero = input('Digite seu genero (M ou F): ')
        email = input('Digite seu email: ')
        
        ID = editar
        #Coloca os dados dentro da lista 'Cadastro'
        cadastro = [ID, nome, idade, genero, email]
        
        #Edita as informacoes na lista geral (editar menos 1 pois na hora do cadastro, o len soma 1)
        listageral[editar - 1] = cadastro

        
    elif menu == '4':
        #Fecha o programa
        break
        
    else:
        #Nao faz nada e consequentemente, reinicia o programa
        print ('Opcao Invalida, Tente Novamente.')    

