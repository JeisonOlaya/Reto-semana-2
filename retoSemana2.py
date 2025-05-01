promedio=[]

Menu=True
while Menu:
    print("=="*20,"\n")
    print("Menu de notas")
    print("=="*20,"\n")
    
    print("1) Ingresar Materias: ")
    print("2) Ingresar Notas: ")
    print("3) Calcular promedio: ")
    print("4) Mostrar las Notas mas alta: \n")
    
    escoger = int (input("Que opcion elijes del 1 al 4?: \n"))
    if escoger==1:
        continuar = True
        while continuar:
            print("\n=== INGRESO DE MATERIAS ===")
            materia= input("Por favor ingresa la materia: ")
            promedio.append(materia)
            
            print("Materia añadida correctamente")

            valor = input("¿Deseas continuar agregando materias?: S(si) N(no): ").upper()

            continuar = False if valor == "N" else True
            
        volver = int(input("Para volver al menú anterior, digita 1, o 2 para finalizar: "))

        if volver == 2:

            print("Exitoso ")

            Menu = False
            
    if escoger == 2:
        print("\n=== INGRESO DE MATERIAS ===")
        notas= int(input("Por favor ingresa las nota de la materia (0 a 100)"))
        
        