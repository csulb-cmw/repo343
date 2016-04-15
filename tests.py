import unittest
from commit import ignore 
import pathing
import sys
import repo343
class Repo343Tests(unittest.TestCase):
    def test_get_argv_option_success(self):
        #mock args
        sys.argv[0] = '-t'
        sys.argv[1] = 'test'
        self.assertEquals(repo343.get_argv_option('-t'), 'test')

    def test_get_argv_option_doesnt_exist_fail(self):
        #mock args
        sys.argv[0] = '-t'
        sys.argv[1] = 'test'
        self.assertFalse(repo343.get_argv_option('-f'))

    def test_get_argv_option_end_of_line_fail(self):
        #mock args
        sys.argv[0] = '-t'
        sys.argv[1] = '-m'
        self.assertFalse(repo343.get_argv_option('-m'))

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

    def test_convert_abs_repo_path_into_relative_repo_file_path_unix_macos(self):
        """Test for unix/Mac OS style paths"""
        path = pathing.convert_abs_repo_path_into_relative_repo_file_path(
            '/test/this/thing/repo343/deeper/deepest.txt', '/test/this/thing')
        self.assertEquals(
                path, 'deeper/deepest.txt')

        
if __name__ == '__main__':
    unittest.main()
