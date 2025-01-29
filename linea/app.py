import funciones
import argparse

def calcular_y(x, m, b):
    return m * x + b

def main(m, b):
    '''
    Funcion principal que calcula las coordenandas de
    una linea recta
    Recibimos m y b
    Regresa: nada
    '''
    X = [x/10.0 for x in range(10, 110, 5)]
    Y = [calcular_y(x, m, b) for x in X]
    coordenadas_flotantes = list(zip(X, Y))
    print('flotantes')
    print(coordenadas_flotantes)
    funciones.grafica_linea(X, Y, m, b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=float, help='Pendiente de la recta', default=2.0)
    parser.add_argument('-b', type=float, help='Ordenada al origen', default=3.0)
    args = parser.parse_args()
    main(args.m, args.b)