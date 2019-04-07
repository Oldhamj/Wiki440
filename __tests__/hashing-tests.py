import unittest
from wiki.web.user import UserManager
from config import TEST_USER_DIR

class TestHashing(unittest.TestCase):

  def test_user_create_with_hash(self):
    manager = UserManager(TEST_USER_DIR)
    manager.add_user('User', 'Password'.encode())
    user = manager.get_user('User')
    self.assertIsNotNone(user)
    self.assertNotEqual('Password', user.get('hash'))

if __name__ == '__main__':
  unittest.main()
