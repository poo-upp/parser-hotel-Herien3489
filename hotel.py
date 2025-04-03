import random

def generar_nombre_aleatorio():
    nombres = ["Alex",]
    apellidos = ["Guzman"]
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

class Reserva:
    def __init__(self, nombre_cliente, check_in, check_out, noches, habitaciones, personas, detalles_habitacion, email):
        self.nombre_cliente = nombre_cliente if nombre_cliente else generar_nombre_aleatorio()
        self.check_in = check_in
        self.check_out = check_out
        self.noches = noches
        self.habitaciones = habitaciones
        self.personas = personas
        self.detalles_habitacion = detalles_habitacion
        self.email = email
    
    def calcular_total(self):
        return sum(hab["precio"] for hab in self.detalles_habitacion)
    
    def generar_resumen(self):
        resumen = f"\n¡Hola {self.nombre_cliente}! Aquí tienes los detalles de tu reserva:\n\n"
        resumen += f"Check-in:\t{self.check_in}\nCheck-out:\t{self.check_out}\n\n"
        resumen += f"Reservaste\t{self.noches} noches, {self.habitaciones} habitaciones, {self.personas} personas\n\n"
        resumen += "Detalles de reserva\n"
        for hab in self.detalles_habitacion:
            resumen += f"[{hab['cantidad']}] {hab['tipo']}\n"
        resumen += f"\nE-mail de contacto: {self.email}\n\n"
        resumen += "Detalles del precio:\n"
        for hab in self.detalles_habitacion:
            resumen += f"[{hab['cantidad']}] {hab['tipo']}\t {hab['precio']:.2f}$\n"
        resumen += "-" * 50 + "\n"
        resumen += f"Total:\t{self.calcular_total():.2f}$\n"
        return resumen


detalles = [
    {"tipo": "Habitacion individual", "cantidad": 1, "precio": 5000.00},
    {"tipo": "Suite de Lujo", "cantidad": 1, "precio": 70000.00}
]

reserva = Reserva("", "07-07-2025", "10-07-2025", 3, 2, 6, detalles, "andlops@dmail.com")
print(reserva.generar_resumen())

