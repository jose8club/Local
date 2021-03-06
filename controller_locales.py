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
	query = """SELECT * FROM local"""
	result = c.execute(query)
	locales = result.fetchall()
	con.close()
	return locales

def obtener_ciudades():
	con = connect()
	c = con.cursor()
	query = """SELECT * FROM ciudad"""
	result = c.execute(query)
	ciudades = result.fetchall()
	con.close()
	return ciudades

def obtener_locales_por_ciudad(id_ciudad):
	con = connect()
	c = con.cursor()
	query = """SELECT a.id_local, a.nombre, a.direccion, b.nombre as 'ciudad'
			FROM local a, ciudad b WHERE a.fk_id_ciudad = b.id_ciudad
			AND a.fk_id_ciudad = ?"""
	result = c.execute(query, [id_ciudad])
	locales = result.fetchall()
	con.close()
	return locales

def eliminar_local(id_local):
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