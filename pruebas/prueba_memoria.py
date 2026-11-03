#!/usr/bin/env python3
"""Pruebas sin internet de herramientas/memoria.py: python3 pruebas/prueba_memoria.py"""
import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from herramientas import memoria  # noqa: E402

AHORA = dt.datetime(2026, 11, 1, 13, 0, tzinfo=memoria.MIAMI)


class Pruebas(unittest.TestCase):
    def test_comillas_escapadas(self):
        sql = memoria.sql_anotar("Sedano's #32", "Nicole dijo 'ok'", "Gmail", "Claude Code",
                                 "obra")
        self.assertIn("'Sedano''s #32'", sql)
        self.assertIn("'Nicole dijo ''ok'''", sql)
        self.assertIn("on conflict (nombre) do update set actualizado = now()", sql)

    def test_ficha_solo_pisa_lo_que_se_pasa(self):
        sql = memoria.sql_ficha("Kilwins", "obra", "TABLERO", estado="propuesta enviada")
        self.assertIn("estado = excluded.estado", sql)
        self.assertNotIn("resumen", sql)
        self.assertNotIn("nombre = excluded", sql)

    def test_ficha_rechaza_tipo_y_resumen_largo(self):
        with self.assertRaises(ValueError):
            memoria.sql_ficha("X", "cliente", "F")
        with self.assertRaises(ValueError):
            memoria.sql_ficha("X", "obra", "F", resumen="a" * 601)

    def test_buscar(self):
        self.assertEqual(memoria.sql_buscar("kilwin"),
                         "select * from public.memoria_buscar('kilwin', 5);")

    def test_caliente_entra_en_2_kb_y_ordena(self):
        filas = [{"tipo": "obra", "nombre": "Obra %d" % i, "estado": "cotizando",
                  "proximo": "mandar la propuesta con todos los detalles " * 3,
                  "vence": "2026-11-0%d" % (1 + i % 8)} for i in range(60)]
        filas.append({"tipo": "bot", "nombre": "Bot multiactivo", "estado": "sin aprobar",
                      "proximo": None, "vence": None})
        texto = memoria.armar_caliente(filas, AHORA, ["- 1-nov: Cerebro MOP aprobado"])
        self.assertLessEqual(len(texto.encode()), memoria.TOPE_BYTES)
        self.assertIn("## Vence en 7 días", texto)
        self.assertIn("(hay más: buscar en la memoria)", texto)

    def test_caliente_marca_vencidas_y_bots(self):
        filas = [{"tipo": "tramite", "nombre": "Auditoría del seguro", "estado": "en curso",
                  "proximo": "llamada NEIS", "vence": "2026-10-31"},
                 {"tipo": "bot", "nombre": "Bot D", "estado": "en papel", "vence": None},
                 {"tipo": "constructora", "nombre": "Lehman", "estado": "espera seguimiento",
                  "proximo": None, "vence": None}]
        texto = memoria.armar_caliente(filas, AHORA)
        self.assertIn("31-10 Auditoría del seguro (VENCIDA): llamada NEIS", texto)
        self.assertIn("## Bots\n- Bot D: en papel", texto)
        self.assertIn("## Esperando (a Martin o al cliente)\n- Lehman: espera seguimiento", texto)

    def test_revisar_y_caliente_son_solo_lectura(self):
        for sql in (memoria.SQL_REVISAR, memoria.SQL_CALIENTE):
            self.assertTrue(sql.startswith("select "))


if __name__ == "__main__":
    unittest.main()
