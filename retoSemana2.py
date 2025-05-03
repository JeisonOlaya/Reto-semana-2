def mostrar_menu():
    print("\nMENU DE NOTAS")
    print("1. Ingresar materia")
    print("2. Agregar nota a materia")
    print("3. Mostrar materias y notas")
    print("4. Calcular promedio y estado por materia")
    print("5. Contar y mostrar calificaciones mayores a un valor")
    print("6. Salir")

def calcular_estado(promedio):
    if promedio >= 90 and promedio <= 100:
        return "Aprobado (excelente)"
    elif promedio >= 80 and promedio < 90:
        return "Aprobado (sobresaliente)"
    elif promedio >= 70 and promedio < 80:
        return "Aprobado (aceptable)"
    elif promedio >= 60 and promedio < 70:
        return "Aprobado (regular)"
    elif promedio >= 0 and promedio < 60:
        return "Reprobaste"
    else:
        return "Promedio inválido"

def main():
    notas_por_materia = {} # Aca creamos un diccionario con (clave= materia) y (valor= lista de notas)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1': # aca creamos un bucle para seguir agregando materias
            while True:
                materia = input("Ingrese el nombre de la materia (o escriba 'salir' para volver al menú): ").strip()
                if materia.lower() == 'salir':
                    break
                if materia in notas_por_materia:
                    print(f"La materia '{materia}' ya existe.")
                else:
                    notas_por_materia[materia] = []
                    print(f"Materia '{materia}' agregada.")

        elif opcion == '2':
            if not notas_por_materia:
                print("No hay materias. Ingrese alguna materia primero.")
                continue

            while True:
                print("\nMaterias disponibles:")
                for m in notas_por_materia:
                    print(f"- {m}")
                materia = input("Escriba el nombre de la materia a la que desea agregar notas (o 'salir' para volver al menú): ")
                if materia.lower() == 'salir':
                    break
                if materia not in notas_por_materia:
                    print(f"La materia '{materia}' no existe.")
                    continue

                # Aca hacemos un bucle interno para agregar varias notas a la misma materia
                while True:
                    entrada = input(f"Ingrese las notas separadas por coma para '{materia}' de 0 a 100(o 'cambiar' para otra materia, 'salir' para volver al menú): ")
                    if entrada.lower() == 'salir':
                        break
                    if entrada.lower() == 'cambiar':
                        break
                    try:
                        # Aca estamos convertiendo la cadena a una lista de floats
                        notas = [float(n.strip()) for n in entrada.split(",")]
                        # aca verificamos que todas las notas estén en el rango válido
                        if all(0 <= n <= 100 for n in notas):
                            notas_por_materia[materia].extend(notas)
                            print(f"Notas {notas} agregadas a la materia '{materia}'.")
                        else:
                            print("Todas las notas deben estar entre 0 y 100.")
                    except ValueError:
                        print("Entrada inválida. Asegúrese de ingresar solo números separados por comas.")


        elif opcion == '3':
            if not notas_por_materia:
                print("No hay materias para mostrar.")
            else:
                print("\nMaterias y sus notas:")
                for m, notas in notas_por_materia.items():
                    print(f"- {m}: {notas}")

        elif opcion == '4':
            if not notas_por_materia:
                print("No hay materias para mostrar.")
                continue
            
            print("\nPromedio y estado por materia:")
            for m, notas in notas_por_materia.items():
                if len(notas) == 0:
                    print(f"- {m}: No hay notas ingresadas para calcular promedio.")
                else:
                    promedio = sum(notas) / len(notas)
                    estado = calcular_estado(promedio)
                    print(f"- {m}: Promedio = {promedio:.2f} -> {estado}")

        elif opcion == '5':
            if not notas_por_materia:
                print("No hay materias ni notas para contar.")
                continue
            try:
                valor = float(input("Ingrese la nota de referencia para contar las calificaciones mayores: "))
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                continue

            # Lista para almacenar las calificaciones mayores al valor ingresado
            calificaciones_mayores = []

            for materia, notas in notas_por_materia.items():
                # Filtramos las notas mayores al valor ingresado
                notas_mayores = [nota for nota in notas if nota > valor]
                
                if notas_mayores:
                    print(f"\nMaterias con notas mayores a {valor}:")
                    print(f"Materia '{materia}' -> Notas mayores: {notas_mayores}")
                    calificaciones_mayores.extend(notas_mayores)

            # Mostrar las calificaciones mayores en general
            if calificaciones_mayores:
                print(f"\nTodas las calificaciones mayores a {valor} son: {calificaciones_mayores}")
                print(f"Total de calificaciones mayores a {valor}: {len(calificaciones_mayores)}")
            else:
                print(f"No se encontraron calificaciones mayores a {valor}.")


if __name__ == "__main__":
    main()
