import unittest
from main import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        result = self.app.get("/")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode("utf-8"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
