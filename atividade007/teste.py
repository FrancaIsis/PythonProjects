 '''qual_lista_editar = int(input('Escolha qual informaçao deseja editar:\n'
                                          '1 - nome\n'
                                          '2 - endereço\n'
                                          '3 - telefone\n'
                                          '0 - desistir\n'))
                     print('-'*70)
                     if qual_lista_editar == 1:
                          # exclui o nome no indice indicado
                          nome.pop(indice)
                          #del nome[indice]
                          # solicita o nome correto
                          edicao = input('Informe o nome correto: ')
                          # insere novo nome
                          nome.insert(indice,edicao)
                          print('Dado alterado com sucesso.')
                          break

                               
                     elif qual_lista_editar == 2:
                          # exclui o endereço no indice indicado
                          endereco.pop(indice)
                          # solicita o endereço correto
                          edicao = input('Informe o endereço correto: ')
                          # insere novo endereço
                          endereco.insert(indice,edicao)
                          print('Dado alterado com sucesso.')
                          break
                          
                     elif qual_lista_editar == 3:
                          # exclui o telefone no indice indicado
                          telefone.pop(indice)
                          # solicita o telefone correto
                          edicao = input('Informe o nome correto: ')
                          # insere novo telefone
                          telefone.insert(indice,edicao)
                          print('Dado alterado com sucesso.')
                          break'''
                     

                     #if qual_lista_editar == 0:
                     #     break
                     