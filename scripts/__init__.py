import os
import sys

def ejecutar_comando(directorio, comando):
    os.chdir(directorio)
    os.system(comando)

def main():
    if len(sys.argv) != 3:
        print("Uso: mi_proyecto <directorio> <comando>")
        sys.exit(1)

    directorio = sys.argv[2]
    comando = sys.argv[1]

    ejecutar_comando(directorio, comando)

if __name__ == "__main__":
    main()
