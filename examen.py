import heapq

class Paciente:
    def __init__(self, nombre, urgencia):
        self.nombre = nombre
        self.urgencia = urgencia

    def __lt__(self, otro):
        return self.urgencia < otro.urgencia  # Prioridad más alta para valores menores

    def __repr__(self):
        return f"{self.nombre} (Urgencia: {self.urgencia})"

class SalaEmergencias:
    def __init__(self):
        self.cola = []

    def ingresar_paciente(self, nombre, urgencia):
        paciente = Paciente(nombre, urgencia)
        heapq.heappush(self.cola, paciente)
        print(f"Paciente ingresado: {paciente}")

    def atender_paciente(self):
        if self.cola:
            paciente = heapq.heappop(self.cola)
            print(f"Atendiendo a: {paciente}")
            return paciente
        else:
            print("No hay pacientes en espera.")
            return None

    def extraer_todos_pacientes(self):
        print("Extrayendo todos los pacientes en orden de atención:")
        while self.cola:
            self.atender_paciente()

    def mostrar_pacientes(self):
        print("Pacientes en espera:", self.cola)

# Ejemplo de uso
if __name__ == "__main__":
    sala = SalaEmergencias()
    sala.ingresar_paciente("Juan Pérez", 3)
    sala.ingresar_paciente("Ana Gómez", 1)
    sala.ingresar_paciente("Carlos Ruiz", 5)
    sala.ingresar_paciente("Laura Méndez", 2)
    
    sala.mostrar_pacientes()
    
    sala.extraer_todos_pacientes()
    sala.mostrar_pacientes()
