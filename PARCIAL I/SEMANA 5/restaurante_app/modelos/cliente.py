# Modelo de Cliente
# Representa una persona registrada en el sistema del restaurante

class Cliente:
    """
    Clase que representa un cliente registrado en el restaurante.
    Almacena información de contacto y estado del cliente.
    """
    
    def __init__(
        self,
        id_cliente: int,
        nombre: str,
        email: str,
        telefono: str,
        es_cliente_frecuente: bool = False
    ):
        """
        Constructor de la clase Cliente.
        
        Args:
            id_cliente: Identificador único del cliente
            nombre: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono del cliente
            es_cliente_frecuente: Indica si es cliente frecuente (False por defecto)
        """
        self.id_cliente: int = id_cliente
        self.nombre: str = nombre
        self.email: str = email
        self.telefono: str = telefono
        self.es_cliente_frecuente: bool = es_cliente_frecuente
    
    def registrar_cliente_frecuente(self) -> None:
        """Marca al cliente como cliente frecuente."""
        self.es_cliente_frecuente = True
    
    def actualizar_telefono(self, nuevo_telefono: str) -> None:
        """
        Actualiza el número de teléfono del cliente.
        
        Args:
            nuevo_telefono: Nuevo número de teléfono
        """
        self.telefono = nuevo_telefono
    
    def __str__(self) -> str:
        """Representación en texto del cliente."""
        tipo_cliente = "Cliente Frecuente" if self.es_cliente_frecuente else "Cliente Regular"
        return (
            f"ID: {self.id_cliente} | Nombre: {self.nombre} | "
            f"Email: {self.email} | Teléfono: {self.telefono} | "
            f"Tipo: {tipo_cliente}"
        )
