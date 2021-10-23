import sqlite3
URL_DB = 'db_vuelos.db'


def seleccion(sql) -> list:
    """ Ejecuta una consulta de selección sobre la base de datos """
    try:
        with sqlite3.connect(URL_DB) as con:
            cur = con.cursor()
            res = cur.execute(sql).fetchall()
    except Exception:
        res = ['0']
    return res


def seleccionb(sql) -> int:
    """ Ejecuta una consulta de selección sobre la base de datos """
    try:
        with sqlite3.connect(URL_DB) as con:
            cur = con.cursor()
            res = cur.execute(sql).fetchall()
            res = len(res)
    except Exception:
        res = 0
    return res


def accion(sql, datos) -> int:
    """ Ejecuta una consulta de acción sobre la base de datos """
    try:
        with sqlite3.connect(URL_DB) as con:
            cur = con.cursor()
            res = cur.execute(sql, datos).rowcount
            if res != 0:
                con.commit()
    except Exception:
        res = 0
    return res


def accionb(sql) -> int:
    """ Ejecuta una consulta de acción sobre la base de datos """
    try:
        with sqlite3.connect(URL_DB) as con:
            cur = con.cursor()
            res = cur.execute(sql).rowcount
            if res != 0:
                con.commit()
    except Exception:
        res = 0
    return res
