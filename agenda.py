contato1_nome = contato1_sobrenome = contato1_telefone = contato1_celular = contato1_email = contato1_mes = contato1_dia = contato1_ano = ""
contato2_nome = contato2_sobrenome = contato2_telefone = contato2_celular = contato2_email = contato2_mes = contato2_dia = contato2_ano = ""
contato3_nome = contato3_sobrenome = contato3_telefone = contato3_celular = contato3_email = contato3_mes = contato3_dia = contato3_ano = ""
contato4_nome = contato4_sobrenome = contato4_telefone = contato4_celular = contato4_email = contato4_mes = contato4_dia = contato4_ano = ""
contato5_nome = contato5_sobrenome = contato5_telefone = contato5_celular = contato5_email = contato5_mes = contato5_dia = contato5_ano = ""
 
total_contatos = 0
 
while True:
    print("--- Menu Principal da Agenda ---")
    print("1- Inserir Contato")
    print("2- Listar Contatos")
    print("3- Buscar Contato")
    print("4- Atualizar Contato")
    print("5- Remover Contato")
    print("6- Sair")
 
    opcao = input("Digite o número da opção desejada: ")
 
    if opcao == '1':
        if total_contatos == 5:
            print("ERRO: Não existe mais espaço na agenda.")
        else:
            print("--- Inserindo Novo Contato ---")
            
            novo_nome = input("Nome (obrigatório, até 20 letras): ")
            while not (0 < len(novo_nome) <= 20 and novo_nome.replace(" ", "").isalpha()):
                print("-> o valor não atende a especificação do campo.")
                novo_nome = input("Nome (obrigatório, até 20 letras): ")
            
            novo_sobrenome = input("Sobrenome (obrigatório, até 20 letras): ")
            while not (0 < len(novo_sobrenome) <= 20 and novo_sobrenome.replace(" ", "").isalpha()):
                print("-> o valor não atende a especificação do campo.")
                novo_sobrenome = input("Sobrenome (obrigatório, até 20 letras): ")
            
            novo_telefone = input("Telefone (opcional, até 15 números): ")
            while not ((novo_telefone == "" or novo_telefone.isdigit()) and len(novo_telefone) <= 15):
                print("-> o valor não atende a especificação do campo.")
                novo_telefone = input("Telefone (opcional, até 15 números): ")
            
            novo_celular = input("Celular (obrigatório, até 15 números): ")
            while not (novo_celular.isdigit() and 0 < len(novo_celular) <= 15):
                print("-> o valor não atende a especificação do campo.")
                novo_celular = input("Celular (obrigatório, até 15 números): ")
            
            novo_email = input("Email (obrigatório, formato palavra@palavra.palavra): ")
            while not ('@' in novo_email and '.' in novo_email and novo_email.count('@') == 1 and 
                      novo_email.find('@') > 0 and novo_email.rfind('.') > novo_email.find('@') + 1 and 
                      len(novo_email) - 1 > novo_email.rfind('.')):
                print("-> o valor não atende a especificação do campo.")
                novo_email = input("Email (obrigatório, formato palavra@palavra.palavra): ")
            
            novo_mes = input("Mês de Aniversário (obrigatório, 2 dígitos, 01-12): ")
            while not (len(novo_mes) == 2 and novo_mes.isdigit() and 1 <= int(novo_mes) <= 12):
                print("-> o valor não atende a especificação do campo.")
                novo_mes = input("Mês de Aniversário (obrigatório, 2 dígitos, 01-12): ")
            
            novo_dia = input("Dia de Aniversário (obrigatório, 2 dígitos, 01-31): ")
            while not (len(novo_dia) == 2 and novo_dia.isdigit() and 1 <= int(novo_dia) <= 31):
                print("-> o valor não atende a especificação do campo.")
                novo_dia = input("Dia de Aniversário (obrigatório, 2 dígitos, 01-31): ")
            
            novo_ano = input("Ano de Aniversário (obrigatório, 4 dígitos, 1900-2025): ")
            while not (len(novo_ano) == 4 and novo_ano.isdigit() and 1900 <= int(novo_ano) <= 2025):
                print("-> o valor não atende a especificação do campo.")
                novo_ano = input("Ano de Aniversário (obrigatório, 4 dígitos, 1900-2025): ")
            
            total_contatos = total_contatos + 1
            
            if total_contatos == 1:
                contato1_nome, contato1_sobrenome, contato1_telefone, contato1_celular, contato1_email, contato1_mes, contato1_dia, contato1_ano = (
                    novo_nome, novo_sobrenome, novo_telefone, novo_celular, novo_email, novo_mes, novo_dia, novo_ano
                )
            elif total_contatos == 2:
                contato2_nome, contato2_sobrenome, contato2_telefone, contato2_celular, contato2_email, contato2_mes, contato2_dia, contato2_ano = (
                    novo_nome, novo_sobrenome, novo_telefone, novo_celular, novo_email, novo_mes, novo_dia, novo_ano
                )
            elif total_contatos == 3:
                contato3_nome, contato3_sobrenome, contato3_telefone, contato3_celular, contato3_email, contato3_mes, contato3_dia, contato3_ano = (
                    novo_nome, novo_sobrenome, novo_telefone, novo_celular, novo_email, novo_mes, novo_dia, novo_ano
                )
            elif total_contatos == 4:
                contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano = (
                    novo_nome, novo_sobrenome, novo_telefone, novo_celular, novo_email, novo_mes, novo_dia, novo_ano
                )
            elif total_contatos == 5:
                contato5_nome, contato5_sobrenome, contato5_telefone, contato5_celular, contato5_email, contato5_mes, contato5_dia, contato5_ano = (
                    novo_nome, novo_sobrenome, novo_telefone, novo_celular, novo_email, novo_mes, novo_dia, novo_ano
                )
            
            print("SUCESSO: O contato " + novo_nome + " " + novo_sobrenome + " foi inserido com sucesso.")
 
    elif opcao == '2':
        print("--- Lista de Contatos Cadastrados ---")
        if total_contatos == 0:
            print("A agenda está vazia.")
        else:
            if total_contatos >= 1:
                print("1 - " + contato1_nome + " " + contato1_sobrenome)
            if total_contatos >= 2:
                print("2 - " + contato2_nome + " " + contato2_sobrenome)
            if total_contatos >= 3:
                print("3 - " + contato3_nome + " " + contato3_sobrenome)
            if total_contatos >= 4:
                print("4 - " + contato4_nome + " " + contato4_sobrenome)
            if total_contatos == 5:
                print("5 - " + contato5_nome + " " + contato5_sobrenome)
 
    elif opcao == '3':
        print("--- Buscar Contato ---")
        if total_contatos == 0:
            print("A agenda está vazia. Impossível buscar.")
        else:
            busca_nome = input("Digite o nome do contato a ser buscado: ")
            busca_sobrenome = input("Digite o sobrenome do contato a ser buscado: ")
            encontrado = False
            
            if total_contatos >= 1 and contato1_nome.lower() == busca_nome.lower() and contato1_sobrenome.lower() == busca_sobrenome.lower():
                print("--- Dados do Contato Encontrado ---")
                print("1- " + contato1_nome + " " + contato1_sobrenome)
                print("2- " + (contato1_telefone if contato1_telefone else 'Não informado'))
                print("3- " + contato1_celular)
                print("4- " + contato1_email)
                print("5- " + contato1_dia + "/" + contato1_mes + "/" + contato1_ano)
                encontrado = True
            
            if not encontrado and total_contatos >= 2 and contato2_nome.lower() == busca_nome.lower() and contato2_sobrenome.lower() == busca_sobrenome.lower():
                print("--- Dados do Contato Encontrado ---")
                print("1- " + contato2_nome + " " + contato2_sobrenome)
                print("2- " + (contato2_telefone if contato2_telefone else 'Não informado'))
                print("3- " + contato2_celular)
                print("4- " + contato2_email)
                print("5- " + contato2_dia + "/" + contato2_mes + "/" + contato2_ano)
                encontrado = True
            
            if not encontrado and total_contatos >= 3 and contato3_nome.lower() == busca_nome.lower() and contato3_sobrenome.lower() == busca_sobrenome.lower():
                print("--- Dados do Contato Encontrado ---")
                print("1- " + contato3_nome + " " + contato3_sobrenome)
                print("2- " + (contato3_telefone if contato3_telefone else 'Não informado'))
                print("3- " + contato3_celular)
                print("4- " + contato3_email)
                print("5- " + contato3_dia + "/" + contato3_mes + "/" + contato3_ano)
                encontrado = True
            
            if not encontrado and total_contatos >= 4 and contato4_nome.lower() == busca_nome.lower() and contato4_sobrenome.lower() == busca_sobrenome.lower():
                print("--- Dados do Contato Encontrado ---")
                print("1- " + contato4_nome + " " + contato4_sobrenome)
                print("2- " + (contato4_telefone if contato4_telefone else 'Não informado'))
                print("3- " + contato4_celular)
                print("4- " + contato4_email)
                print("5- " + contato4_dia + "/" + contato4_mes + "/" + contato4_ano)
                encontrado = True
            
            if not encontrado and total_contatos == 5 and contato5_nome.lower() == busca_nome.lower() and contato5_sobrenome.lower() == busca_sobrenome.lower():
                print("--- Dados do Contato Encontrado ---")
                print("1- " + contato5_nome + " " + contato5_sobrenome)
                print("2- " + (contato5_telefone if contato5_telefone else 'Não informado'))
                print("3- " + contato5_celular)
                print("4- " + contato5_email)
                print("5- " + contato5_dia + "/" + contato5_mes + "/" + contato5_ano)
                encontrado = True
            
            if not encontrado:
                print("ERRO: Contato não encontrado.")
 
    elif opcao == '4':
        print("--- Atualizar Contato ---")
        if total_contatos == 0:
            print("A agenda está vazia. Impossível atualizar.")
        else:
            busca_nome = input("Digite o nome do contato a ser atualizado: ")
            busca_sobrenome = input("Digite o sobrenome do contato a ser atualizado: ")
            encontrado = False
            contato_aux = 0
            
            if total_contatos >= 1 and contato1_nome.lower() == busca_nome.lower() and contato1_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_aux = 1
            elif total_contatos >= 2 and contato2_nome.lower() == busca_nome.lower() and contato2_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_aux = 2
            elif total_contatos >= 3 and contato3_nome.lower() == busca_nome.lower() and contato3_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_aux = 3
            elif total_contatos >= 4 and contato4_nome.lower() == busca_nome.lower() and contato4_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_aux = 4
            elif total_contatos == 5 and contato5_nome.lower() == busca_nome.lower() and contato5_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_aux = 5
            
            if not encontrado:
                print("ERRO: Contato não encontrado.")
            else:
                while True:
                    print("Qual campo deseja modificar?")
                    print("1- Nome\n2- Sobrenome\n3- Telefone\n4- Celular\n5- Email\n6- Mês de Aniversário\n7- Dia de Aniversário\n8- Ano de Aniversário\n9- Voltar para o menu principal")
                    campo_modificar = input("Escolha uma opção: ")
                    
                    novo_valor = ""
                    if campo_modificar in '12345678':
                        novo_valor = input("Digite o novo valor: ")
                    
                    if campo_modificar == '1':
                        while not (0 < len(novo_valor) <= 20 and novo_valor.replace(" ", "").isalpha()):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Nome: ")
                        if contato_aux == 1: contato1_nome = novo_valor
                        elif contato_aux == 2: contato2_nome = novo_valor
                        elif contato_aux == 3: contato3_nome = novo_valor
                        elif contato_aux == 4: contato4_nome = novo_valor
                        elif contato_aux == 5: contato5_nome = novo_valor
                    
                    elif campo_modificar == '2':
                        while not (0 < len(novo_valor) <= 20 and novo_valor.replace(" ", "").isalpha()):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Sobrenome: ")
                        if contato_aux == 1: contato1_sobrenome = novo_valor
                        elif contato_aux == 2: contato2_sobrenome = novo_valor
                        elif contato_aux == 3: contato3_sobrenome = novo_valor
                        elif contato_aux == 4: contato4_sobrenome = novo_valor
                        elif contato_aux == 5: contato5_sobrenome = novo_valor
                    
                    elif campo_modificar == '3':
                        while not ((novo_valor == "" or novo_valor.isdigit()) and len(novo_valor) <= 15):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Telefone: ")
                        if contato_aux == 1: contato1_telefone = novo_valor
                        elif contato_aux == 2: contato2_telefone = novo_valor
                        elif contato_aux == 3: contato3_telefone = novo_valor
                        elif contato_aux == 4: contato4_telefone = novo_valor
                        elif contato_aux == 5: contato5_telefone = novo_valor
                    
                    elif campo_modificar == '4':
                        while not (novo_valor.isdigit() and 0 < len(novo_valor) <= 15):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Celular: ")
                        if contato_aux == 1: contato1_celular = novo_valor
                        elif contato_aux == 2: contato2_celular = novo_valor
                        elif contato_aux == 3: contato3_celular = novo_valor
                        elif contato_aux == 4: contato4_celular = novo_valor
                        elif contato_aux == 5: contato5_celular = novo_valor
                    
                    elif campo_modificar == '5':
                        while not ('@' in novo_valor and '.' in novo_valor and novo_valor.count('@') == 1 and 
                                  novo_valor.find('@') > 0 and novo_valor.rfind('.') > novo_valor.find('@') + 1 and 
                                  len(novo_valor) - 1 > novo_valor.rfind('.')):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Email: ")
                        if contato_aux == 1: contato1_email = novo_valor
                        elif contato_aux == 2: contato2_email = novo_valor
                        elif contato_aux == 3: contato3_email = novo_valor
                        elif contato_aux == 4: contato4_email = novo_valor
                        elif contato_aux == 5: contato5_email = novo_valor
                    
                    elif campo_modificar == '6':
                        while not (len(novo_valor) == 2 and novo_valor.isdigit() and 1 <= int(novo_valor) <= 12):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Mês de Aniversário: ")
                        if contato_aux == 1: contato1_mes = novo_valor
                        elif contato_aux == 2: contato2_mes = novo_valor
                        elif contato_aux == 3: contato3_mes = novo_valor
                        elif contato_aux == 4: contato4_mes = novo_valor
                        elif contato_aux == 5: contato5_mes = novo_valor
                    
                    elif campo_modificar == '7':
                        while not (len(novo_valor) == 2 and novo_valor.isdigit() and 1 <= int(novo_valor) <= 31):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Dia de Aniversário: ")
                        if contato_aux == 1: contato1_dia = novo_valor
                        elif contato_aux == 2: contato2_dia = novo_valor
                        elif contato_aux == 3: contato3_dia = novo_valor
                        elif contato_aux == 4: contato4_dia = novo_valor
                        elif contato_aux == 5: contato5_dia = novo_valor
                    
                    elif campo_modificar == '8':
                        while not (len(novo_valor) == 4 and novo_valor.isdigit() and 1900 <= int(novo_valor) <= 2025):
                            print("-> o valor não atende a especificação do campo.")
                            novo_valor = input("Digite o novo Ano de Aniversário: ")
                        if contato_aux == 1: contato1_ano = novo_valor
                        elif contato_aux == 2: contato2_ano = novo_valor
                        elif contato_aux == 3: contato3_ano = novo_valor
                        elif contato_aux == 4: contato4_ano = novo_valor
                        elif contato_aux == 5: contato5_ano = novo_valor
                    
                    elif campo_modificar == '9':
                        break
                    
                    else:
                        print("ERRO: Campo inválido. Escolha novamente.")
                        continue
                    
                    print("SUCESSO: Campo atualizado com sucesso.")
                    break
 
    elif opcao == '5':
        print("--- Remover Contato ---")
        if total_contatos == 0:
            print("A agenda está vazia. Impossível remover.")
        else:
            busca_nome = input("Digite o nome do contato a ser removido: ")
            busca_sobrenome = input("Digite o sobrenome do contato a ser removido: ")
            encontrado = False
            contato_id = 0
            
            if total_contatos >= 1 and contato1_nome.lower() == busca_nome.lower() and contato1_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_id = 1
            elif total_contatos >= 2 and contato2_nome.lower() == busca_nome.lower() and contato2_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_id = 2
            elif total_contatos >= 3 and contato3_nome.lower() == busca_nome.lower() and contato3_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_id = 3
            elif total_contatos >= 4 and contato4_nome.lower() == busca_nome.lower() and contato4_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_id = 4
            elif total_contatos == 5 and contato5_nome.lower() == busca_nome.lower() and contato5_sobrenome.lower() == busca_sobrenome.lower():
                encontrado = True
                contato_id = 5
            
            if not encontrado:
                print("ERRO: Contato não encontrado.")
            else:
                if contato_id == 1:
                    nome_removido = contato1_nome + " " + contato1_sobrenome
                    contato1_nome, contato1_sobrenome, contato1_telefone, contato1_celular, contato1_email, contato1_mes, contato1_dia, contato1_ano = (
                        contato2_nome, contato2_sobrenome, contato2_telefone, contato2_celular, contato2_email, contato2_mes, contato2_dia, contato2_ano
                    )
                    contato2_nome, contato2_sobrenome, contato2_telefone, contato2_celular, contato2_email, contato2_mes, contato2_dia, contato2_ano = (
                        contato3_nome, contato3_sobrenome, contato3_telefone, contato3_celular, contato3_email, contato3_mes, contato3_dia, contato3_ano
                    )
                    contato3_nome, contato3_sobrenome, contato3_telefone, contato3_celular, contato3_email, contato3_mes, contato3_dia, contato3_ano = (
                        contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano
                    )
                    contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano = (
                        contato5_nome, contato5_sobrenome, contato5_telefone, contato5_celular, contato5_email, contato5_mes, contato5_dia, contato5_ano
                    )
                    contato5_nome = contato5_sobrenome = contato5_telefone = contato5_celular = contato5_email = contato5_mes = contato5_dia = contato5_ano = ""
                
                elif contato_id == 2:
                    nome_removido = contato2_nome + " " + contato2_sobrenome
                    contato2_nome, contato2_sobrenome, contato2_telefone, contato2_celular, contato2_email, contato2_mes, contato2_dia, contato2_ano = (
                        contato3_nome, contato3_sobrenome, contato3_telefone, contato3_celular, contato3_email, contato3_mes, contato3_dia, contato3_ano
                    )
                    contato3_nome, contato3_sobrenome, contato3_telefone, contato3_celular, contato3_email, contato3_mes, contato3_dia, contato3_ano = (
                        contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano
                    )
                    contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano = (
                        contato5_nome, contato5_sobrenome, contato5_telefone, contato5_celular, contato5_email, contato5_mes, contato5_dia, contato5_ano
                    )
                    contato5_nome = contato5_sobrenome = contato5_telefone = contato5_celular = contato5_email = contato5_mes = contato5_dia = contato5_ano = ""
                
                elif contato_id == 3:
                    nome_removido = contato3_nome + " " + contato3_sobrenome
                    contato3_nome, contato3_sobrenome, contato3_telefone, contato3_celular, contato3_email, contato3_mes, contato3_dia, contato3_ano = (
                        contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano
                    )
                    contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano = (
                        contato5_nome, contato5_sobrenome, contato5_telefone, contato5_celular, contato5_email, contato5_mes, contato5_dia, contato5_ano
                    )
                    contato5_nome = contato5_sobrenome = contato5_telefone = contato5_celular = contato5_email = contato5_mes = contato5_dia = contato5_ano = ""
                
                elif contato_id == 4:
                    nome_removido = contato4_nome + " " + contato4_sobrenome
                    contato4_nome, contato4_sobrenome, contato4_telefone, contato4_celular, contato4_email, contato4_mes, contato4_dia, contato4_ano = (
                        contato5_nome, contato5_sobrenome, contato5_telefone, contato5_celular, contato5_email, contato5_mes, contato5_dia, contato5_ano
                    )
                    contato5_nome = contato5_sobrenome = contato5_telefone = contato5_celular = contato5_email = contato5_mes = contato5_dia = contato5_ano = ""
                
                elif contato_id == 5:
                    nome_removido = contato5_nome + " " + contato5_sobrenome
                    contato5_nome = contato5_sobrenome = contato5_telefone = contato5_celular = contato5_email = contato5_mes = contato5_dia = contato5_ano = ""
                
                total_contatos = total_contatos - 1
                print("SUCESSO: O contato " + nome_removido + " foi excluído com sucesso.")
    
    elif opcao == '6':
        print("Encerrando a agenda... Até logo!")
        break
 
    else:
        print("ERRO: Opção inválida. Por favor, digite um número de 1 a 6.")
