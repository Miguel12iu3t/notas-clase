#importancion necesaria para utilizar una dataclass
from dataclasses import dataclass

#definimos los componentes de la clase
@dataclass
class User:
    id: str
    name: str
    age: int
    
    def show_data(self):
        return f"ID: {self.id}\nNombre: {self.name}\nEdad: {self.age}"

#funcion para la creacion de un nuevo usuario
def create_user(id, name, age):
    pass

#forma de visualizar los distintos usuarios (1,2,3 y 4)
#donde __name__ tendra que ser igual a la funcion __main__
if __name__ == "__main__":
    usuario1 = User(1, "Hugo", 25)
    usuario2 = User(2, "Ana", 30)
    usuario3 = User(3, "Juan", 40)
    usuario4 = User(4, "Maria", 35)
    usuarios = [usuario1, usuario2, usuario3, usuario4]
#ejecutando con un ciclo for para poder visualizar todos los usuarios
    for usuario in usuarios:
        print(usuario.show_data())    
    