from tabela import ascii_table

# Objeto ChaveRSA
class ChaveRSA:
    def __init__(self, D, N):
        self.D = D
        self.N = N


# Buscar texto criptografado
def buscar_texto():
    try:
        with open("./criptografados.txt", "r") as arquivo:
            texto_criptografado = arquivo.read()
            print(f"O texto criptografado é: {texto_criptografado}")
            return texto_criptografado
    
    except FileNotFoundError:
        print("Arquivo criptografados.txt não encontrado.")
        return None
    
# Buscar as chaves no arquivo
def buscar_chaves():
    try:
        with open("./chaves.txt", "r") as arquivo:
            linha = arquivo.readline().strip()

            elementos = linha.split()

            D, N = None, None

            # Encontrar os valores de D e N
            for elemento in elementos:
                if "D:" in elemento:
                    D = int(''.join(filter(str.isdigit, elemento.split(":")[1])))
                elif "N:" in elemento:
                    N = int(''.join(filter(str.isdigit, elemento.split(":")[1])))
            
            # Verificar se D e N são nulos
            if D is not None and N is not None:
                # Criando o objeto chave
                chave = ChaveRSA(D, N)
                print(f"A chave N: {chave.N}\nA chave D: {chave.D}")
                return chave
            else:
                print("Chaves não encontradas no formato esperado em 'chaves.txt'.")
                return None
        
    except FileNotFoundError:
        print("Arquivo chaves.txt não encontrado.")
        return None

# Texto criptografado para decimal
def decodificando(texto_criptografado, chave):
    texto_decodificado = []
    
    for valor_criptografado_str in texto_criptografado.split():
        # Convertendo cada valor criptografado para inteiro
        valor_criptografado = int(valor_criptografado_str)
        
        valor_decodificado = (valor_criptografado ** chave.D) % chave.N
        texto_decodificado.append(valor_decodificado)

    print(f"O texto em decimal é: {texto_decodificado}")

    mensagem_original = converter_para_caracteres(texto_decodificado)
    print(f"A mensagem original é: {mensagem_original}")

# Converter decimal para caracteres
def converter_para_caracteres(texto_decodificado):
    caracteres = [chr(ascii_table.get(valor_decimal, valor_decimal)) for valor_decimal in texto_decodificado]
    return ''.join(caracteres)
   
""" 
Texto original = (TEXTO CRIPTOGRAFADO ^ D) mod N 
"""