from unittest import TestCase, mock
import os
import shutil
import tempfile
from tools.tools import check_dir_existence


class TestTools(TestCase):

    def setUp(self):
        self.root_dir = os.path.abspath(os.path.dirname(__file__))
        self.temp_root_dir = tempfile.mkdtemp()
        self.existing_dirs = []

        for _i in range(3):
            self.existing_dirs.append(
                os.path.basename(
                    tempfile.mkdtemp(prefix='h_', dir=self.temp_root_dir)
                )
            )

    def tearDown(self):
        shutil.rmtree(self.temp_root_dir)

    def test_check_dir_existence_sub_dir_not_found(self):
        """
        Tests if there is no such a sub dir passed in list
        """
        self.assertFalse(self.existing_dirs.append('unexpected_dir'))

    def test_check_dir_existence_all_ok(self):
        """
        Tests if the result is OK
        """
        self.assertTrue(check_dir_existence(self.temp_root_dir, self.existing_dirs))

    def test_check_dir_existence_root_is_wrong(self):
        """
        Tests if the the check returns False if the root dir is wrong
        """
        self.assertFalse(check_dir_existence('/some/wrong/path', self.existing_dirs))

    def test_check_dir_existence_wrong_second_param_but_iterable(self):
        """
        Tests if the the check returns False if the second parameter is a string
        """
        self.assertFalse(check_dir_existence(self.temp_root_dir, self.existing_dirs[0]))

    def test_check_dir_existence_wrong_second_param_not_iterable(self):
        """
        Tests if the the check rise exception if the second parameter is not an iterable
        """
        with self.assertRaises(TypeError):
            check_dir_existence(self.temp_root_dir, 1)

    def test_check_dir_existence_wrong_first_param_not_iterable(self):
        """
        Tests if the the check rise exception if the first parameter is not a path sting
        """
        with self.assertRaises(TypeError):
            check_dir_existence(1, self.existing_dirs)
