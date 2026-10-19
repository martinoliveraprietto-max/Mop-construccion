#!/usr/bin/env python3
"""Pruebas sin internet de herramientas/tablero.py: python3 pruebas/prueba_tablero.py"""
import datetime as dt
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from herramientas import tablero  # noqa: E402

AHORA = dt.datetime(2026, 10, 19, 19, 0, tzinfo=dt.timezone.utc)  # 15:00 en Miami


def fila(frente, clave, valor, fecha="2026-10-19 11:58:00.123456+00", quien="cazador",
         fuente=""):
    return {"frente": frente, "clave": clave, "valor": valor, "fecha": fecha,
            "fuente": fuente, "quien_escribio": quien}


class Pruebas(unittest.TestCase):
    def test_fechas_de_execute_sql_y_de_la_api(self):
        esperada = dt.datetime(2026, 10, 19, 11, 58, tzinfo=dt.timezone.utc)
        for texto in ("2026-10-19 11:58:00+00", "2026-10-19T11:58:00+00:00",
                      "2026-10-19T11:58:00Z", "2026-10-19 11:58:00.12+00"):
            self.assertEqual(tablero.leer_fecha(texto).replace(microsecond=0), esperada, texto)

    def test_seccion_ordena_frentes_y_usa_hora_de_miami(self):
        texto = tablero.seccion([
            fila("vigilante", "respuestas", "0", quien="vigilante"),
            fila("cazador", "esperan decisión", "2"),
            fila("cazador", "constructoras en cola", "3", fuente="avisos/cazador"),
            fila("otro", "x", "1", quien="otro"),
        ], AHORA)
        lineas = texto.splitlines()
        self.assertTrue(lineas[0].startswith("2. Sistema de asistentes"))
        self.assertIn("19-10 15:00", lineas[0])
        self.assertEqual(lineas[1], "- Cazador (19-10 7:58, cazador): constructoras en cola: 3; "
                                    "esperan decisión: 2. Fuente: avisos/cazador.")
        self.assertTrue(lineas[2].startswith("- Vigilante"))
        self.assertTrue(lineas[3].startswith("- Otro"))
        self.assertNotIn("ATRASADO", texto)

    def test_marca_atrasos(self):
        texto = tablero.seccion([
            fila("guardián", "tareas fallidas", "0", fecha="2026-10-17 11:00:00+00",
                 quien="guardián")], AHORA)
        self.assertIn("ATRASADO: 56 horas", texto)
        texto = tablero.seccion([
            fila("cazador", "a", "1"),
            fila("cazador", "b", "2", fecha="2026-10-16 11:00:00+00")], AHORA)
        self.assertIn("Sin actualizar: b.", texto)

    def test_tabla_vacia(self):
        self.assertIn("Sin datos", tablero.seccion([], AHORA))

    def test_sql_poner_escapa_comillas(self):
        sql = tablero.sql_poner("cazador", "nota", "O'Brien's", "", "cazador")
        self.assertIn("'O''Brien''s'", sql)
        self.assertIn("on conflict (frente, clave) do update", sql)

    def test_comando_con_filas_y_sin_llave(self):
        os.environ.pop("SUPABASE_SERVICE_ROLE_KEY", None)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as a:
            json.dump({"result": [fila("cazador", "constructoras en cola", "3")]}, a)
        salida = io.StringIO()
        with redirect_stdout(salida):
            self.assertEqual(tablero.main(["--filas", a.name]), 0)
        os.unlink(a.name)
        self.assertIn("constructoras en cola: 3", salida.getvalue())
        error = io.StringIO()
        with redirect_stderr(error), redirect_stdout(io.StringIO()):
            self.assertEqual(tablero.main([]), 2)
        self.assertIn("from public.tablero", error.getvalue())
        salida = io.StringIO()
        with redirect_stdout(salida), redirect_stderr(io.StringIO()):
            self.assertEqual(tablero.main(["poner", "vigilante", "respuestas", "1",
                                           "--quien", "vigilante"]), 2)
        self.assertIn("insert into public.tablero", salida.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=1)
