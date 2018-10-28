from django.test import TestCase

# Create your tests here.
class DummyTests(TestCase):
    """
    Created dummy tests to see if CI is working
    """
    def test_dummy(self):
        self.assertEqual(1, 1)
