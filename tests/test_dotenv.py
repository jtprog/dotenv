import os
from tempfile import mkstemp

from dotenv import set_variable, Dotenv, get_variable, get_variables

from unittest import TestCase

try:
    # TestCase.assertIsInstance()
    CompatibilityTestCase = TestCase
except AttributeError:
    class CompatibilityTestCase(TestCase):
        def assertIsInstance(self, obj, cls, **kwargs):
            assert obj, cls

        def assertNotIn(self, key, coll, **kwargs):
            assert key not in coll

        def assertIn(self, key, coll, **kwargs):
            assert key in coll


class DotenvTest(CompatibilityTestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("FOO='bar'\n")
            file.write("Bar=foo'\n")
            file.write("baz=1234'\n")
            file.write("url='https://test.oi/do?it=fast'\n")
        self.dtenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

    def test_create(self):
        self.assertIsInstance(self.dtenv, Dotenv)
        self.assertIsInstance(self.dtenv, dict)

    def test_get_keys(self):
        expected = {'FOO', 'Bar', 'baz', 'url'}

        self.assertEqual(expected, set(self.dtenv.keys()))

    def test_get_values(self):
        expected = {'bar', 'foo', '1234', 'https://test.oi/do?it=fast'}

        self.assertEqual(expected, set(self.dtenv.values()))

    def test_set_new_key_value(self):
        self.dtenv['asd'] = 'qwe'

        newdtenv = Dotenv(self.file_path)

        self.assertIn('asd', newdtenv)
        self.assertEqual('qwe', newdtenv['asd'])

    def test_set_existing_key(self):
        self.dtenv['baz'] = 987

        newdtenv = Dotenv(self.file_path)

        self.assertEqual('987', newdtenv['baz'])
        with open(self.file_path, 'r') as file:
            self.assertEqual(4, len(file.readlines()))

    def test_del_key(self):
        del self.dtenv['baz']

        newdtenv = Dotenv(self.file_path)

        self.assertNotIn('baz', newdtenv)
        with open(self.file_path, 'r') as file:
            self.assertEqual(3, len(file.readlines()))


class FunctionalTest(CompatibilityTestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("FOO='bar'\n")
            file.write("Bar=foo'\n")
            file.write("baz=1234'\n")
        self.dtenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

    def test_set_new_variable(self):
        set_variable(self.file_path, 'asd', 'qwe')

        dtenv = Dotenv(self.file_path)
        self.assertIn('asd', dtenv)
        self.assertEqual('qwe', dtenv['asd'])

    def test_set_existing_variable(self):
        set_variable(self.file_path, 'baz', '987')

        dtenv = Dotenv(self.file_path)
        self.assertIn('baz', dtenv)
        self.assertEqual('987', dtenv['baz'])

    def test_get_variable(self):
        result = get_variable(self.file_path, 'baz')

        self.assertEqual('1234', result)

    def test_get_variables(self):
        result = get_variables(self.file_path)

        dtenv = Dotenv(self.file_path)

        self.assertEqual(result, dtenv)


class CommentTest(CompatibilityTestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("# a commented .env file, for testing\n")
            file.write("SOMEVAR='12345' # a var, with an inline comment\n")
            file.write("VAR='giggles'\n")
            file.write("####################\n")
            file.write("\n")
            file.write("# another comment, notice the blank line above\n")
            file.write("    # an indented comment\n")
            file.write("cheese='cake'\n")
            file.write("COMMENT='#comment#test' # a value containing a comment\n")
        self.dtenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

    def test_create(self):
        self.assertIsInstance(self.dtenv, Dotenv)
        self.assertIsInstance(self.dtenv, dict)

    def test_get_keys(self):
        expected = {'SOMEVAR', 'VAR', 'cheese', 'COMMENT'}

        self.assertEqual(expected, set(self.dtenv.keys()))

    def test_get_values(self):
        expected = {'12345', 'giggles', 'cake', '#comment#test'}

        self.assertEqual(expected, set(self.dtenv.values()))
