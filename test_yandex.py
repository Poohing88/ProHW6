import unittest
from unittest.mock import patch
from yandex import translate, translate_request_return

API_KEY = 'gjrjdfffffffjsrjsrjsrjsr8y4rys5j9sr2sr5yjs59a5ej9t5j'

class TestYandexTraslate(unittest.TestCase):

    @patch('yandex.input', side_effect=['hello', 'en-ru'])
    def test_translate(self, input_mock):
        correct_answer = 'привет'
        correct_request = 200
        answer, request = translate()
        self.assertEqual(correct_answer, answer)
        self.assertEqual(correct_request, request)

    @patch('yandex.input', side_effect=['hello', 'wrong lang'])
    def test_wrong_lang_translate(self, input_mock):
        correct_request = 200
        request = translate_request_return()
        answer = request['code']
        self.assertNotEqual(correct_request, answer)

    @patch('yandex.input', side_effect=['hello', 'en-ru'])
    @patch('yandex.API_KEY', API_KEY, create=True)
    def test_wrong_api_translate(self, input_mock):
        correct_request = 200
        request = translate_request_return()
        answer = request['code']
        self.assertNotEqual(correct_request, answer)


if __name__ == '__main__':
    unittest.main()