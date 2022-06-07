from django.test import TestCase

class CalculatorTests(TestCase):

    def test_calculator_correct_params(self):
        response = self.client.get('/calculators/v1/qcalculus?uery=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['result'], '-132.889')

    def test_calculator_wrong_params(self):
        response = self.client.get('/calculators/v1/qcalculus?uery=12345')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], True)
        self.assertEqual(response.data['message'], 'Invalid request')
    