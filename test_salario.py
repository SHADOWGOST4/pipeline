import unittest
from salario import calcular_pago
class TestSalario(unittest.TestCase):

    def test_01(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 40, 0, 0, 0), 1456000.0)

    def test_02(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 0, 5, 0, 0), 113750.0)

    def test_03(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 0, 0, 5, 5), 546000.0)

    def test_04(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 20, 10, 5, 5), 1729000.0)

    def test_05(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 0, 0, 0, 0), 0.0)

    def test_06(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 50, 20, 10, 10), 1911000.0)

    def test_07(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 0, 5, 0, 0), 227500.0)

    def test_08(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 0, 0, 5, 0), 273000.0)

    def test_09(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 0, 0, 0, 5), 273000.0)

    def test_10(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 5, 0, 0, 0), 91000.0)

    def test_11(self):
        self.assertEqual(calcular_pago("docente medio tiempo", -5, 0, 0, 0), 'Error: Las horas no pueden ser negativas.')

    def test_12(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 0, 5, 0, 0), 113750.0)

    def test_13(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 0, 0, 5, 0), 136500.0)

    def test_14(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 0, 0, 0, 5), 136500.0)

    def test_15(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 5, 0, 0, 5), 455000.0)

    def test_16(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 5, 5, 0, 5), 682500.0)

    def test_17(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 5, 0, 0, 5), 227500.0)

    def test_18(self):
        self.assertEqual(calcular_pago("docente medio tiempo", 0, 0, 5, 5), 273000.0)

    def test_19(self):
        self.assertEqual(calcular_pago("docente tiempo completo", 500, 0, 0, 0), 'Error: Excede el máximo de horas permitidas por mes.')

    def test_20(self):
        self.assertEqual(calcular_pago("Freelance", 0, 5, 0, 0), 'Error: Tipo de contrato no válido.')

if __name__ == '__main__':
    unittest.main()