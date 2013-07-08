#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con

def get_regiones():
    con = connect()
    c = con.cursor()
    query = """SELECT * FROM region"""
    result = c.execute(query)
    regiones = result.fetchall()
    con.close()
    return regiones

def get_locales():
    con = connect()
    c = con.cursor()
    query = """SELECT id_local,nombre,direccion FROM local"""
    result = c.execute(query)
    locales = result.fetchall()
    con.close()
    return locales

def get_locales_by_ciudad(id_ciudad):
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


def get_empleados_by_local(id_local):
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

def search(pre='*',mar='*'):
    #devuelve las entradas en que los nombres comienzan con la variable 'pre' de ciudad 'mar'.
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


