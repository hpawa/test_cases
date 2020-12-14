import unittest

from tasks.dict_flatter import flatter, value_by_key
from tasks.xml_depth import get_xml_depth


class TaskTest(unittest.TestCase):
    def setUp(self):
        self.true_a_d = {'a__b__c': 1, 'a__d': 2, 'a__e__f': 3, 'g': 4, 'e__f__h': 5, 'e__z': 6}

    def test_flatter(self):
        d = {
            "c": {
                "f": 9,
                "g": {
                    "m": 17,
                    "n": 3
                }
            },
            "a": 5,
            "b": 6,
        }
        true_res = {
            'a': 5,
            'b': 6,
            'c.f': 9,
            'c.g.m': 17,
            'c.g.n': 3
        }
        a = {}
        flatter(d, p_d=a)
        self.assertDictEqual(a, true_res)

    def test_flatter_delimeter(self):
        a_d = {
            'a': {
                'b': {
                    'c': 1
                },
                'd': 2,
                'e': {
                    'f': 3
                }
            },
            'g': 4,
            'e': {
                'f': {
                    'h': 5
                },
                'z': 6
            }
        }
        b = {}
        flatter(a_d, p_d=b, delimeter='__')
        self.assertEqual(b, self.true_a_d)

    def test_value_by_key(self):
        self.assertEqual(value_by_key(self.true_a_d, 'a__e__f'), 3)

    def test_xml(self):
        xml = """
        <feed xml:lang='en'>
            <title>NPBFX</title>
            <subtitle lang='en'>Programming challenges</subtitle>
            <link rel='alternate' type='text/html' href='http://npbfx.com/' />
            <updated>2020-10-28T12:00:00</updated>
        </feed>
        """
        self.assertEqual(get_xml_depth(xml), 1)


if __name__ == "__main__":
    unittest.main()
