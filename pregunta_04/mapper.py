#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split(',',1)
        letra = fields[0]

        sys.stdout.write("{}\t{}\n".format(letra))