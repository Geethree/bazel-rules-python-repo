import unittest

from libs.lib import main


class ExampleTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(
            """\
-  -
A  1
B  2
-  -""",
            main([["A", 1], ["B", 2]]),
        )


if __name__ == "__main__":
    unittest.main()
