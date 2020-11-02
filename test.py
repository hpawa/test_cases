import unittest
import requests

from tasks.dict_flatter import flatter
from tasks.xml_depth import get_xml_depth


class TaskTest(unittest.TestCase):
    def test_dict(self):
        d = {
            "a": 5,
            "b": 6,
            "c": {
                "f": 9,
                "g": {
                    "m": 17,
                    "n": 3
                }
            }
        }
        true_res = {
            'a': 5,
            'b': 6,
            'c.f': 9,
            'c.g.m': 17,
            'c.g.n': 3
        }
        self.assertDictEqual(flatter(d), true_res)

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
        print(get_xml_depth(requests.get('https://www.npbfx.com/en/feed/').content))


if __name__ == "__main__":
    unittest.main()
