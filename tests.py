import unittest
from commit import ignore 

class CommitTests(unittest.TestCase):
    """Tests for `commit.py`."""

    def test_ignore(self):
        """Is five successfully determined to be prime?"""
        self.assertFalse(ignore('user/documents/test'))
        self.assertTrue(ignore('user/documents/.test'))
        self.assertTrue(ignore('user/documents/repo343/test.py'))
        self.assertTrue(ignore('user/repo343/test/another/test.py'))
        self.assertTrue(ignore('user/test/program.o'))

if __name__ == '__main__':
    unittest.main()
