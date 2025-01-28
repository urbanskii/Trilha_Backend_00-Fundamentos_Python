lista_de_dados = []

def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
    return int(tamanho_em_bytes)/ (2**10) **2

with open('sample_data/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((tamanho_em_disco, usuario))


cabecalho='''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

'''

lista_de_dados.sort(reverse=True)

escolha_usuario = int(input('Digite quantos usuarios deseja mostrar: '))

with open('sample_data/relatorio.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for tamanho, _  in lista_de_dados])
    media = tamanho_total_consumido / len(lista_de_dados)

    arquivo.writelines(cabecalho)

    
    for indice, dados in enumerate(lista_de_dados, start=1):
        tamanho_em_disco, usuario = dados
        arquivo.writelines(
            f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB          '
            f'{tamanho_em_disco/tamanho_total_consumido:>6.2%}\n'
        )
                
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')
