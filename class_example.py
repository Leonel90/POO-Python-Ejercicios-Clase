class persona:
    nombre  = str
    edad    = int

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'

#todo lo q esta desde aki para arriba corre lo q este para abajo no
if __name__ == "__main__":
    David = persona("David", 33)
    Erika = persona("Erika", 35)
    
    print(David.saluda(Erika))
