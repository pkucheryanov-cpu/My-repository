import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # створюю тестовий клієнт Flask
        self.client = app.test_client()
        self.client.testing = True

    def test_environment_endpoint(self):
        # Виконую GET-запит до ендпоінту
        response = self.client.get('/api/environment')

        # Перевірка на статус код
        self.assertEqual(response.status_code, 200)

        # Перевіряю що у відповіді правильна назва додатку
        data = response.get_json()
        self.assertEqual(data["app"], "ShopEasy")
        self.assertEqual(data["env"], "development")

if __name__ == '__main__':
    unittest.main()
