import unittest
import main

class TestParentNode(unittest.TestCase):

    # ---------- extract_title() ---------- #
    def test_extract_title_provided(self):
        expected = "A HEADING"
        contents = "# A HEADING\n\n and some text"
        actual = main.extract_title(contents)
        self.assertEqual(actual, expected)

    def test_extract_title_not_provided(self):
        contents = "No header here\n## Maybe a header 2?\n and some text"

        with self.assertRaises(ModuleNotFoundError) as context:
            main.extract_title(contents)

        self.assertTrue('Heading not found' in str(context.exception))

if __name__ == "__main__":
    unittest.main()