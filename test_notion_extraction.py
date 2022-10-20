import imp
import unittest
import notion_extraction


class TestCalc(unittest.TestCase):

    def test_extract_id_from_url(self):
        result = notion_extraction.extract_id_from_url("https://www.notion.so/Discord-Bot-Overhaul-HIPPO-Jackson-Choyce-0d2f115bca5a4eb7bbfcc4de333207a9")
        self.assertEqual(result, "0d2f115bca5a4eb7bbfcc4de333207a9")


if __name__ == '__main__':
    unittest.main()
    