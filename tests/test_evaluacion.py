from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.generar_dataset import generar_filas
from src.evaluacion import calcular_metricas, normalizar_etiqueta


class Pruebas(unittest.TestCase):
    def test_dataset_balanceado(self):
        filas = generar_filas()
        self.assertEqual(len(filas), 60)
        for etiqueta in ["POS", "NEG", "NEU"]:
            self.assertEqual(sum(f["etiqueta"] == etiqueta for f in filas), 20)
        self.assertEqual(len({f["id"] for f in filas}), 60)

    def test_normalizacion(self):
        self.assertEqual(normalizar_etiqueta("positive"), "POS")
        self.assertEqual(normalizar_etiqueta("NEG"), "NEG")
        self.assertEqual(normalizar_etiqueta("neutral"), "NEU")
        with self.assertRaises(ValueError):
            normalizar_etiqueta("LABEL_5")

    def test_metricas_perfectas(self):
        etiquetas = ["NEG", "NEU", "POS"]
        m = calcular_metricas(etiquetas, etiquetas)
        self.assertEqual(m["f1_macro"], 1.0)
        self.assertEqual(m["accuracy"], 1.0)
        self.assertEqual(m["recall_neg"], 1.0)


if __name__ == "__main__":
    unittest.main()
