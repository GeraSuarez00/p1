import os

class Persona():
    def __init__(self):
        self.lpersonas = []
        self.persona = {}

    def agregarPersonas(self, cedula, nombre):
        self.persona = {
            'Cedula': cedula,
            'Nombres': nombre,
        }
        self.lpersonas.append(self.persona)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.lempleados=[]
        self.devengado={}
        self.deducciones={}
    
    def agregarEmpleado(self):
        cedula= (input("Ingrese la cédula: "))
        nombre= input("Ingrese el nombre: ")
        salario= float(input("Ingrese el salario: "))
        emp={
            'Cédula': cedula,
            'Nombre':nombre
        }
        
        dev={
            'Salario': salario,
            'Alimentación': 0,
            'Transporte': 0
        }
        ded={
            'Salud': 0,
            'Pensión':0
        }
        super().agregarPersonas(cedula,nombre)
        self.lempleados.append([{'Empleado': emp},{'Devengado':dev},{'Deducciones':ded}])

    # def mostrarPersonas(self):
    #     for (indice,persona) in enumerate (self.lpersonas):
    #         print(f"{indice}: {persona}")
    def mostrarEmpleados(self):
            for (indice,empleado) in enumerate (self.lempleados):
                print(f"Empleado #{indice+1}")
                for emp in empleado:
                    print(f"{emp}")
        
    
    def eliminarEmpleados(self):
        ced=input("Ingrese la cedula del empleado a eliminar: ")
        for empleado in range (len(self.lempleados)):
            
            if(self.lempleados[empleado][0]['Empleado']['Cédula']==ced):
                self.lempleados.pop(empleado) 
                print("Eliminado correctamente")                   
    def mostrarMenu(self,menu):
        while(True):
            os.system('clear')
            for item in range (len(menu)):
                print(menu[item])
            
            opcion=input("Elija una opcion: ")
            if opcion == "1":
                os.system('clear')               
                self.agregarEmpleado()
                input("Presione una tecla para continuar")
            if opcion == "2":
                os.system('clear')
                # print("op 2")
                self.mostrarEmpleados()
                input("Presione una tecla para continuar")
            if opcion == "3":
                os.system('clear')
                self.eliminarEmpleados()
                input("Presione una tecla para continuar")
            if opcion == "4":
                break

def menu():
    menu =(
        "------ Menu -----",
        "1. Agregar Empleado",
        "2. Mostrar Empleado",
        "3. Eliminar Empleado",
        "4. Salir",
    )
    emp= Empleado()
    emp.mostrarMenu(menu)


def main():
    menu()


if __name__ == "__main__":
    main()