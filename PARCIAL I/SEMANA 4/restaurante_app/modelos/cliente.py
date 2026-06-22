# Módulo: cliente.py
# Descripción: Define la clase Cliente que representa a los clientes del restaurante

from datetime import datetime

class Cliente:
    """
    Clase que representa un cliente del restaurante.
    
    Atributos:
        id (int): Identificador único del cliente
        nombre (str): Nombre completo del cliente
        telefono (str): Número de teléfono del cliente
        email (str): Correo electrónico del cliente
        fecha_registro (str): Fecha de registro del cliente
    """
    
    def __init__(self, id, nombre, telefono, email):
        """
        Constructor de la clase Cliente.
        
        Args:
            id (int): Identificador único
            nombre (str): Nombre del cliente
            telefono (str): Teléfono del cliente
            email (str): Email del cliente
        """
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        # Registra la fecha actual del sistema
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y")
    
    def __str__(self):
        """
        Representación en texto del objeto Cliente.
        
        Returns:
            str: Información formateada del cliente
        """
        return f"[{self.id}] {self.nombre} - {self.telefono}"
    
    def obtener_info_completa(self):
        """
        Obtiene la información completa del cliente.
        
        Returns:
            str: Información detallada del cliente
        """
        return (f"Cliente: {self.nombre}\n"
                f"  Teléfono: {self.telefono}\n"
                f"  Email: {self.email}\n"
                f"  Fecha de Registro: {self.fecha_registro}")
    
    def actualizar_contacto(self, nuevo_telefono=None, nuevo_email=None):
        """
        Actualiza la información de contacto del cliente.
        
        Args:
            nuevo_telefono (str, optional): Nuevo número de teléfono
            nuevo_email (str, optional): Nuevo email
        """
        if nuevo_telefono:
            self.telefono = nuevo_telefono
            print(f"Teléfono de {self.nombre} actualizado a {nuevo_telefono}")
        
        if nuevo_email:
            self.email = nuevo_email
            print(f"Email de {self.nombre} actualizado a {nuevo_email}")
    
    def es_cliente_vip(self, numero_pedidos_minimo=5):
        """
        Determina si el cliente podría ser considerado VIP.
        Este es un método básico que podría expandirse en el futuro.
        
        Args:
            numero_pedidos_minimo (int): Número mínimo de pedidos para ser VIP
        
        Returns:
            bool: True si cumple con criterios de VIP, False en caso contrario
        """
        # En una versión más completa, esto se basaría en el historial de pedidos
        return False
