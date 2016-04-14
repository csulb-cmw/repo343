import unittest
from commit import ignore 
import pathing

class CommitTests(unittest.TestCase):
    """Tests for `commit.py`."""

    def test_ignore_success(self):
        """This file shouldn't be ignored"""
        self.assertFalse(ignore('/user/documents/test'))
        
    def test_ignore_dot(self):
        """This path should be ignored because of the '.' preceding it's name"""
        self.assertTrue(ignore('/user/documents/.test'))

    def test_ignore_dot_parent(self):
        """This path should be ignored because of the '.' preceding the name of
        one of it's parent folders."""
        self.assertTrue(ignore('/user/documents/.hidden/foo/bar'))
        
    def test_ignore_repo343_parent(self):
        """This path should be ignored, because it is the repo folder"""
        self.assertTrue(ignore('/user/documents/repo343/test.py'))
        self.assertTrue(ignore('/user/repo343/test/another/test.py'))

    def test_ignore_file_type_extension(self):
        """This path should be ignored, because of the file type extension"""
        self.assertTrue(ignore('/user/test/program.o'))

class PathingTests(unittest.TestCase):
    """Tests for `pathing.py`."""

    def test_convert_abs_file_path_into_abs_repo_file_path_unix_macos(self):
        """Test for unix/Mac OS style paths"""
        path = pathing.convert_abs_file_path_into_abs_repo_file_path(
            '/test/this/thing/deep/deeper/deepest.txt', '/test/this/thing')
        self.assertEquals(
                path, '/test/this/thing/repo343/thing/deep/deeper/deepest.txt')
        
if __name__ == '__main__':
    unittest.main()
