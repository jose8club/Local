#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_locales():
    con = connect()
    c = con.cursor()
    query = """SELECT id_local,nombre,direccion FROM local"""
    result = c.execute(query)
    locales = result.fetchall()
    con.close()
    return locales

def obtener_locales_por_ciudad(id_ciudad):
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_local, a.nombre, a.direccion, b.nombre as 'ciudad'
            FROM local a, ciudad b WHERE a.fk_id_ciudad = b.id_ciudad
            AND a.fk_id_ciudad = ?"""
    result = c.execute(query, [id_marca])
    locales = result.fetchall()
    con.close()
    return locales

def buscar_por_ciudad(text): 
    con = connect()
    c = con.cursor()
    query = "SELECT id_ciudad FROM ciudad WHERE nombre=?"
    try:
    	resultado = c.execute(query,text)
    	local = resultado.fetchone()
    except sqlite3.Error as e:
    	exito = False
    print "Error:", e.args[0]
    con.close()
    return local


def obtener_empleados_por_local(id_local):
    con = connect()
    c = con.cursor()
    query = """SELECT a.rut, a.nombre, a.cargo, a.genero, a.sueldo, b.nombre as 'local'
            FROM empleado a, local b WHERE a.fk_id_local = b.id_local
            AND a.fk_id_local = ?"""
    result = c.execute(query, [id_local])
    empleados = result.fetchall()
    con.close()
    return empleados

def eliminar_local(id_local):
    """función que elimina el local al ser señalado mediante su id_local"""
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM local WHERE id_local = ?"
    try:
        result = c.execute(query, [id_local])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agregar_empleado(rut, nombre, cargo, genero, sueldo,fk_id_local):
    """función que permite agregar empleados mediante sus diferentes campos"""
    success = False
    con = connect()
    c = con.cursor()
    values = [rut, nombre, cargo, genero, sueldo,fk_id_local]
    query = "INSERT INTO empleado (rut, nombre, cargo, genero, sueldo,fk_id_local) VALUES(?,?,?,?,?,?)"
    try:
        result = c.execute(query, values)
        success = True
        con.commit()
    except sqlite3.Error as e:
        success = False
        print "Error: ", e.args[0]
    con.close()
    return success

def editar_empleado(rut, nombre, cargo, genero, sueldo,fk_id_local):
    """función que permite editar los campos de los empleados"""
    success = False
    con = connect()
    c = con.cursor()
    values = [nombre, cargo, genero, sueldo,fk_id_local, rut]
    query = "UPDATE empleado SET nombre = ?, cargo = ?, genero = ?, sueldo = ?, fk_id_local = ? WHERE rut = ?"
    try:
        result = c.execute(query, values)
        success = True
        con.commit()
    except sqlite3.Error as e:
        success = False
        print "Error: ", e.args[0]
    con.close()
    return success

def obtener_empleado_por_rut(rut):
    """esta función permite obtener a los empleados mediante su rut"""
    con = connect()
    c = con.cursor()
    query = """SELECT rut, nombre, cargo, genero, sueldo
            FROM empleado WHERE rut = ?"""
    result = c.execute(query, [rut])
    empleados = result.fetchall()
    con.close()
    return empleados

def eliminar_empleado(rut):
    """esta función permite eliminar a los empleados mediante su rut"""
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

def agregar_locales(nombre, direccion, fk_id_ciudad):
    success = False
    con = connect()
    c = con.cursor()
    values = [nombre, direccion,fk_id_local]
    query = "INSERT INTO local (nombre, direccion,fk_id_ciudad) VALUES(?,?,?)"
    try:
        result = c.execute(query, values)
        success = True
        con.commit()
    except sqlite3.Error as e:
        success = False
        print "Error: ", e.args[0]
    con.close()
    return success