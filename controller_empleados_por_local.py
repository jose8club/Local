#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_empleados_por_local(id_local=None):
    id_local = 1
    con = connect()
    c = con.cursor()
    query = """SELECT a.rut, a.nombre, a.cargo, a.genero, a.sueldo, b.nombre as 'local'
            FROM empleado a, local b WHERE a.fk_id_local = b.id_local
            AND a.fk_id_local = ?"""
    result = c.execute(query, [id_local])
    empleados = result.fetchall()
    con.close()
    return empleados


def eliminar_empleado(rut):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM empleado WHERE rut = ?"
    try:
        result = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito