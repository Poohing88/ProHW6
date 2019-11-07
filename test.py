import unittest
from unittest.mock import patch
import json
import os.path
from app import delete_doc, move_doc_to_shelf, remove_doc_from_shelf, add_new_doc, get_doc_shelf


documents = []
directories = {}
workdir = os.path.dirname(__file__)


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        with open(f'{workdir}/fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
            documents.extend(json.load(out_docs))
        with open(f'{workdir}/fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
            directories.update(json.load(out_dirs))

    @patch('app.input', return_value='10006')
    def test_delete_doc(self, input_mock):
        start_len = len(documents)
        delete_doc()
        self.assertGreater(start_len, len(documents))

    @patch('app.input', side_effect=["11-2", '3'])
    def test_move_doc_to_shelf(self, input_mock):
        start_len_shelf_out = len(directories['1'])
        start_len_shelf_come = len(directories['3'])
        move_doc_to_shelf()
        self.assertGreater(start_len_shelf_out, len(directories['1']))
        self.assertGreater(len(directories['3']), start_len_shelf_come)

    def test_remove_doc_from_shelf(self):
        start_len_shelf = len(directories['1'])
        remove_doc_from_shelf('2207 876234')
        self.assertGreater(start_len_shelf, len(directories['1']))

    def test_remove_doc_from_shelf_wrong_document_number(self):
        start_len_shelf = len(directories['1'])
        remove_doc_from_shelf('11111')
        self.assertEqual(start_len_shelf, len(directories['1']))

    @patch('app.input', side_effect=["101010", 'passport', 'alexey alexeev', '3'])
    def test_add_new_doc(self, input_mock):
        start_len_shelf = len(directories['3'])
        add_new_doc()
        self.assertGreater(len(directories['3']), start_len_shelf)

    @patch('app.input', return_value='11-2')
    def test_get_doc_shelf(self, input_mock):
        directori_number = get_doc_shelf()
        real_number = '1'
        self.assertEqual(directori_number, real_number)


if __name__ == '__main__':
    unittest.main()
