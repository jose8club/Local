Empleados
===========

controller.def obtener_empleados_por_local(id_local):
	obtiene los empleados pertenecientes al id_local que se entrega

controller.def agregar_empleado(rut, nombre, cargo, genero, sueldo,fk_id_local):
	agrega un nuevo empleado con sus atributos

controller.def editar_empleado(rut, nombre, cargo, genero, sueldo):
	edita la informacion de un empleado existente, pero no se puede modificar el rut

controller.def obtener_empleado_por_rut(rut):
	esta función permite obtener a los empleados mediante su rut

controller.def eliminar_empleado(rut):
	esta función permite eliminar a los empleados mediante su rut

