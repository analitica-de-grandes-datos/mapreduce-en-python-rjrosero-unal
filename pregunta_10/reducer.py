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
            diccionarioLetras[i].append(key)

        sortedDict = sorted(diccionarioLetras.items(), key=lambda x: x[0])

        for k, v in sortedDict:
            res = sorted(v, key = int)
            v = ",".join(map(str, res))

            sys.stdout.write("{}\t{}\n".format(k, v))