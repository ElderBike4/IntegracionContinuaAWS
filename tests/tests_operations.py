import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración del navegador
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8081")
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_suma(self):
        # Esperar a que los campos num1 y num2 estén visibles
        num1 = self.wait.until(EC.visibility_of_element_located((By.ID, 'num1')))
        num2 = self.wait.until(EC.visibility_of_element_located((By.ID, 'num2')))
        resultado = self.wait.until(EC.visibility_of_element_located((By.ID, 'resultado')))

        # Ingresar valores
        num1.send_keys("10")
        num2.send_keys("5")

        # Probar suma
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Suma']"))).click()
        self.wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), "15"))
        num1.clear()
        num2.clear()

    def test_resta(self):
        # Repetir la configuración para la resta
        num1 = self.wait.until(EC.visibility_of_element_located((By.ID, 'num1')))
        num2 = self.wait.until(EC.visibility_of_element_located((By.ID, 'num2')))
        resultado = self.wait.until(EC.visibility_of_element_located((By.ID, 'resultado')))

        # Ingresar valores
        num1.send_keys("10")
        num2.send_keys("5")

        # Probar resta
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Resta']"))).click()
        self.wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), "5"))
        num1.clear()
        num2.clear()

    def test_multiplicacion(self):
        # Repetir la configuración para la multiplicación
        num1 = self.wait.until(EC.visibility_of_element_located((By.ID, 'num1')))
        num2 = self.wait.until(EC.visibility_of_element_located((By.ID, 'num2')))
        resultado = self.wait.until(EC.visibility_of_element_located((By.ID, 'resultado')))

        # Ingresar valores
        num1.send_keys("10")
        num2.send_keys("5")

        # Probar multiplicación
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Multiplicar']"))).click()
        self.wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), "50"))
        num1.clear()
        num2.clear()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
