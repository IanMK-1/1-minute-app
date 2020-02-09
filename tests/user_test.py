import unittest
from app.models import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch_user = User(password='password')

    def test_user_password_not_empty(self):
        self.assertTrue(self.new_pitch_user.user_password is not None)

    def test_block_access_to_password(self):
        with self.assertRaises(AttributeError):
            self.new_pitch_user.password

    def test_verify_password(self):
        self.assertTrue(self.new_pitch_user.verify_password('password'))
