def primeiro_nome(nome_completo: str, separador: str=' ', posicao: int=1):

    primeiro_nome = nome_completo.split(separador)[posicao]

    return primeiro_nome