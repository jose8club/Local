Metodos del programa
=====================

main.py ventana principal

class Locales(QtGui.QMainWindow):
    """Esta es la clase de la ventana principal que creará la grilla dond estan los locales"""

def __init__(self,parent=None):
        """constructor que crea la ventana"""

def render_table(self):
        """funcion que define las funciones de la tabla"""

def conectar_tabla_empleados(self):
        """funcion que conecta la grilla principal con la tabla de empleados"""

def set_signals(self):
        """función que establece las señales con los diferentes botones, el filtro de texto y el combobox"""

def load_ciudades(self):
        """funcion que define el combobox"""

def setup_search_bar(self):
        """función que agrega la caracteristica de autocompletacion"""

def update_search(self):
	"""completer para la busqueda de locales"""

def textChanged(self,string):
        """función que filtra la tabla con la palabra ingresada en la barra de busqueda"""

def pressAdd(self):
        """funcion que abre y hace funcionar la ventana de agregar locales mediante el boton PushAceptar"""

def load_datos(self, locales=None):
        """función que carga todos los locales en la ventana principal"""

def pressDelete(self):
        """función que borra los locales"""

def pressEdit(self):
        """función que edita los locales"""

controller_locales.py

def connect():
    """funcion que conecta a la base de datos"""

def get_locales_by_ciudad(id_ciudad):
    """funcion que obtiene los locales por ciudad"""

def get_regiones():
    """funcion que obtiene las regiones"""

def get_ciudades():
    """funcion que obtiene las ciudades"""

def get_names():
    """devuelve un arreglo con los nombres de los locales"""

def buscar_por_ciudad(text):
    """funcion que obtiene la ciudad por su nombre"""

def get_empleados_by_local(id_local):
    """funcion que obtiene los empleados por cada local"""

def delete_local(id_local):
    """funcion que borra los locales por su id_local"""

def add_local(nombre, direccion, fk_id_ciudad):
    """funcion que agrega los locales"""

def search(pre='*',mar='*'):
    """funcion que obtiene los locales
    devuelve las entradas en que los nombres comienzan con la variable 'pre' de ciudad 'mar'."""



empleados_grid.py grilla de los empleados

class Form(QtGui.QDialog):
	"""clase que crea la grilla de empleados de cada local"""

def __init__(self, parent=None, id_local=None):
		"""constructor que abre la ventana que muestra los empleados"""

def conectar(self):
	"""función que conecta la grilla de empleados con la forma de ingreso de empleados"""

def datos(self, id_local):
		"""función que muestra los empleados de un local en específico, usando su id_local"""

def eliminar(self):
		"""función que elimina los empleados de cada local que solo pueden ser eliminados a través de la selección del registro a eliminar"""


controller_local.py controller de los locales

def connect():
    """funcion que conecta a la base de datos"""

def get_regiones():
    """funcion que obtiene las regiones"""
    
def get_ciudades():
    """funcion que obtiene las ciudades"""

def get_names():
    """devuelve un arreglo con los nombres de los locales"""

def get_locales():
    """función que busca todos los locales"""

def get_locales_by_ciudad(id_ciudad):
    """función que busca los locales por ciudad"""

def buscar_por_ciudad(text):
    """funcion que obtiene la ciudad por su nombre"""

def get_empleados_by_local(id_local):
    """funcion que obtiene los empleados por cada local"""

def delete_local(id_local):
    """funcion que borra los locales por su id_local"""

def add_local(nombre, direccion, fk_id_ciudad):
    """funcion que agrega los locales"""

def search(pre='*',mar='*'):
    """funcion que obtiene los locales
    devuelve las entradas en que los nombres comienzan con la variable 'pre' de ciudad 'mar'."""

controller.py controller general que usaremos para los empleados

def connect():
    """funcion que conecta a la base de datos"""

def obtener_empleados_por_local(id_local):
    """funcion que obtiene todos los empelados por local usando su id_local como identificador"""

def eliminar_local(id_local):
    """función que elimina el local al ser señalado mediante su id_local"""

def agregar_empleado(rut, nombre, cargo, genero, sueldo,fk_id_local):
    """función que permite agregar empleados mediante sus diferentes campos"""

def editar_empleado(rut, nombre, cargo, genero, sueldo,fk_id_local):
    """función que permite editar los campos de los empleados"""

def obtener_empleado_por_rut(rut):
    """esta función permite obtener a los empleados mediante su rut"""

def eliminar_empleado(rut):
    """esta función permite eliminar a los empleados mediante su rut"""

view_local_form es el programa que crea la ventana de ingreso y edición de locales

class Form(QtGui.QDialog):
    """clase que crea la ventana de agregar locales"""

def __init__(self, parent=None):
        """constructor de la ventana de agregar locales"""

def add(self):
        """función que se llama para agregar locales"""

def cancel(self):
        """función para cancelar el agregar un local nuevo"""

empleados_form.py forma de agregar y editar empleados

class Form(QtGui.QDialog):
    """clase que crea la ventana de ingreso de empleados"""

def __init__(self, parent=None):
        """constructor que crea la ventana de ingreso de empleados"""

def add(self):
        """función que crea el ingreso de empleados"""

def cancel(self):
        """ventana que permite la cancelación de la ventana"""





