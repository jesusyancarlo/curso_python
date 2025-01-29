def dibuja_tablero(simbolos: dict):
    '''
    Función para imprimir el tablero de gato con los símbolos proporcionados.
    '''
    print(f'''
     {simbolos[1]} | {simbolos[2]} | {simbolos[3]}
    ---+---+---
     {simbolos[4]} | {simbolos[5]} | {simbolos[6]}
    ---+---+---
     {simbolos[7]} | {simbolos[8]} | {simbolos[9]}
    ''')

    if __name__ == '__main__':
        numeros = [str(x) for x in range(1, 10)]
        simbolos = {x:'' for x in numeros}
        dibuja_tablero(simbolos)
        simbolos['1']='X'
        dibuja_tablero(simbolos)
        simbolos['5']='0'
        dibuja_tablero(simbolos)