from pydantic import BaseModel

class Usuario (BaseModel):
    id: int
    nombre: str
    apellido: str

    def ToString(self) -> str:
        return f"id: {self.id}, Nombre y apellido: {self.nombre} {self.apellido}"