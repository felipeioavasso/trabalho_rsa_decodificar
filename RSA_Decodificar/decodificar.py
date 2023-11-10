############## Import ##############
import menus
import motor



def decodificar_mensagem():
# Buscar as chaves
    chave = motor.buscar_chaves()

    # Se as chaves foram encontradas, continuar
    if chave is not None:
        # Buscar o texto criptografado
        texto_criptografado = motor.buscar_texto()

        # Se o texto criptografado foi encontrado, continuar
        if texto_criptografado is not None:
            # Chamar a função de decodificação
            motor.decodificando(texto_criptografado, chave)

    #menus.print_menu_final()
    

