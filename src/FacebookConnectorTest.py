import unittest
import FacebookConnector

class FacebookConnectorTest(unittest.TestCase):

    def test_getFriends_returns_a_list(self):
        result = FacebookConnector.getFriends('me')
        self.assertIs(type(result), list)

    def test_getFriends_returns_a_list_of_strings(self):
        result = FacebookConnector.getFriends('me')
        for item in result:
            self.assertIs(type(item), unicode)

if __name__ == '__main__':
    unittest.main()
