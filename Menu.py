print "*****************************************************************************************************"
print "*****************************************************************************************************"
print "*                                                                                                   *"
print "*                                 INSTITUTO POLITECNICO DE BEJA                                     *"
print "*                                                                                                   *"
print "*                        ESCOLA SUPERIOR DE TECNOLOGIAS E GESTAO DE BEJA                            *"
print "*                                                                                                   *"
print "*                        MESTRADO EM ENGENHARIA DE SEGURANCA INFORMATICA                            *"
print "*                                                                                                   *"
print "*                                LINGUAGENS DE PROGRAMACAO DINAMICA                                 *"
print "*                                                                                                   *"
print "*****************************************************************************************************"
print "*****************************************************************************************************"
print "*                                                                                                   *"
print "*                                            MENU                                                   *"
print "*                                                                                                   *"
print "*****************************************************************************************************"
print "*****************************************************************************************************"
def print_menu():
print "*                                                                                                   *"
print "*                                      1. Menu Option 1                                             *"
print "*                                                                                                   *"
print "*                                      2. Menu Option 2                                             *"
print "*                                                                                                   *"
print "*                                      3. Menu Option 3                                             *"
print "*                                                                                                   *"
print "*                                      4. Menu Option 4                                             *"
print "*                                                                                                   *"
print "*                                      5. Sair                                                      *"
print "*                                                                                                   *"
print "*****************************************************************************************************"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Escolha a sua opcao [1-5]: ")
     
    if choice==1:     
        print "Menu 1 has been selected"
        ## You can add your code or functions here
    elif choice==2:
        print "Menu 2 has been selected"
        ## You can add your code or functions here
    elif choice==3:
        print "Menu 3 has been selected"
        ## You can add your code or functions here
    elif choice==4:
        print "Menu 4 has been selected"
        ## You can add your code or functions here
    elif choice==5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Essa opcao nao e valida. Tente novamente")
