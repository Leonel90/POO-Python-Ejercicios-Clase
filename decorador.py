def funcion_decorador(funcion):
    def wrapper():
        print("Este es el primer mensaje")
        funcion()
        print("este es el segundo mensaje")
        return wrapper
    
    def zumbido():
        print("buzzzzzz")
        
        zumbido = funcion_decorador(zumbido)
        
        print(zumbido())