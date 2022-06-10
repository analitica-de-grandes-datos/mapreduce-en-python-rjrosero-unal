#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    diccionarioLetras = {}

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = val.split(",")

        #por cada letra de val obtener cada uno de los key asociados
        for i in val:
            #si no existe la clave la crea y le asigna el valor
            if i not in diccionarioLetras:
                diccionarioLetras[i] = [key]
            #si ya existe la clave la agrega al valor
            else:
                diccionarioLetras[i].append(key)

            #if i not in diccionarioLetras.keys():
            #    diccionarioLetras[i] = key
            #else:
            #    diccionarioLetras[i] += ',' + key           

        sortedDict = sorted(diccionarioLetras.items(), key=lambda x: x[0])

    #imprimir el diccionario
    for key, valorOrdenado in sortedDict:
        resultado = sorted(valorOrdenado.split(','), key = int)
        valorOrdenado = ",".join(map(str, resultado))

        sys.stdout.write("{}\t{}\n".format(key, valorOrdenado))