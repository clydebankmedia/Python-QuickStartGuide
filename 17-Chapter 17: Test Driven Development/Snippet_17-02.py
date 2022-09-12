# Import the unittest module
import unittest

# Import our greeting module
import greeting

class GreetingTests(unittest.TestCase):
    def test_greeting_without_name(self):
        # Test without an argument
        self.assertEqual(greeting.say_greeting(), "Hello, World!")

    def test_greeting_with_name(self):
        # Test with an argument
        self.assertEqual(greeting.say_greeting("Robert"), "Hello, Robert!")

if __name__ == '__main__':
    unittest.main()
