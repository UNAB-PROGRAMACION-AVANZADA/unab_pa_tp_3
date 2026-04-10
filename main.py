# ===== IMPORTS ====
from src.punto  import Punto
from src.linea import Linea

def main():
    p1 = Punto(3,2)
    print(p1.impresion())
    opuesto_p1 = p1.opuesto()
    print(opuesto_p1.impresion())
    
    print("==== PRUEBA CLASE LINEA ====")
    p2 = Punto (5,8)
    linea = Linea(p1,p2)
    print(linea)
    linea.mueve_abajo(3)
    print(linea)
    
    
if __name__ == "__main__":
    main()