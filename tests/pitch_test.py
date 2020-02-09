from app.models import User, Pitch
import unittest


class UserPitchTest(unittest.TestCase):
    def setUp(self):
        self.user_joy = User(username='Joy', user_password='shoe', email='joy@gmail.com')
        self.new_pitch = Pitch(id=1, title='Restuarants', pitch='Best restuarants', type="product",
                               user=self.user_joy, upvote=0, downvote=0)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'Resturants')
        self.assertEquals(self.new_pitch.pitch, 'Best restuarants')
        self.assertEquals(self.new_pitch.type, "product")
        self.assertEquals(self.new_pitch.user, self.user_joy)

    def test_save_pitch(self):
        self.new_pitch.save_user_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_user_pitch()
        got_pitch = Pitch.obtain_user_pitch(1)
        self.assertTrue(got_pitch is not None)
