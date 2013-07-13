#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    """funcion que conecta a la base de datos"""

    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con

def get_regiones():
    """funcion que obtiene las regiones"""
    
    con = connect()
    c = con.cursor()
    query = """SELECT * FROM region"""
    result = c.execute(query)
    regiones = result.fetchall()
    con.close()
    return regiones


def get_ciudadess():
    con = connect()
    c = con.cursor()
    query = "SELECT * FROM ciudad"
    try:
       resultado= c.execute(query)
       ciudades = resultado.fetchall()
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return ciudades

def get_ciudades():
    """funcion que obtiene las ciudades"""

    con = connect()
    c = con.cursor()
    query = """SELECT id_ciudad, nombre FROM ciudad"""
    result = c.execute(query)
    ciudades = result.fetchall()
    con.close()
    return ciudades


def get_names():
    """devuelve un arreglo con los nombres de los locales"""
    con = connect()
    c = con.cursor()
    query = "SELECT nombre FROM local"
    c.execute(query)
    names = []
    resultado = c.fetchall()
    for row in resultado:
        names.append(row[0])
    con.close()
    return names

def get_localess():
    con = connect()
    c = con.cursor()
    query = """SELECT nombre,direccion,fk_id_ciudad FROM local"""
    result = c.execute(query)
    locales = result.fetchall()
    con.close()
    return locales

def get_locales():
    """funcion que obtiene los locales"""
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_local, a.nombre, a.direccion, b.nombre as 'ciudad'
            FROM local a, ciudad b WHERE a.fk_id_ciudad = b.id_ciudad"""
    result = c.execute(query)
    locales = result.fetchall()
    con.close()
    return locales

def get_locales_by_ciudad(id_ciudad):
    """funcion que obtiene los locales por ciudad"""
    con = connect()
    c = con.cursor()
    query = """SELECT a.id_local, a.nombre, a.direccion, b.nombre as 'ciudad'
            FROM local a, ciudad b WHERE a.fk_id_ciudad = b.id_ciudad
            AND a.fk_id_ciudad = ?"""
    result = c.execute(query, [id_ciudad])
    locales = result.fetchall()
    con.close()
    return locales

def buscar_por_ciudad(text):
    """funcion que obtiene la ciudad por su nombre"""
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


def get_empleados_by_local(id_local):
    """funcion que obtiene los empleados por cada local"""
    con = connect()
    c = con.cursor()
    query = """SELECT a.rut, a.nombre, a.cargo, a.genero, a.sueldo, b.nombre as 'local'
            FROM empleado a, local b WHERE a.fk_id_local = b.id_local
            AND a.fk_id_local = ?"""
    result = c.execute(query, [id_local])
    empleados = result.fetchall()
    con.close()
    return empleados

def delete_local(id_local):
    """funcion que borra los locales por su id_local"""
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

def add_empleado(rut, nombre, cargo, genero, sueldo,fk_id_local):
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


def add_local(nombre, direccion, fk_id_ciudad):
    """funcion que agrega los locales"""
    success = False
    con = connect()
    c = con.cursor()
    values = [nombre, direccion,fk_id_ciudad]
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

def search(pre='*',mar='*'):
    """funcion que obtiene los locales
    devuelve las entradas en que los nombres comienzan con la variable 'pre' de ciudad 'mar'."""
    con = connect()
    c = con.cursor()
    if mar != '*':
    #Query donde obtiene todos los locales determinados por la barra de busqueda y la ciudad filtrada.
        try:
           query = "SELECT id_ciudad FROM ciudad WHERE nombre = ?"
	   resultado = c.execute(query,[mar])
	   num = resultado.fetchone()
	   query = "SELECT * FROM local WHERE nombre LIKE ? AND fk_id_ciudad LIKE ?"
	   resultado = c.execute(query,[pre,num[0]])
        except sqlite3.Error as e:
            exito = False
	    print "Error:", e.args[0]
    else:
    #Query donde no hay filtro de ciudad, solo busca elementos relacionados en la barra de busqueda.
        num = '*'
        query = "SELECT * FROM local WHERE nombre LIKE ?"
        try:
           resultado = c.execute(query,[pre])
        except sqlite3.Error as e:
            exito = False
            print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod


