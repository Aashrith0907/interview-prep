import unittest
from interview_engine import InterviewEngine  # Adjust the import based on your actual module structure


class TestInterviewEngine(unittest.TestCase):
    
    def setUp(self):
        self.engine = InterviewEngine()

    def test_start_session(self):
        self.engine.start_session()
        self.assertTrue(self.engine.is_session_active)

    def test_add_question(self):
        self.engine.start_session()
        self.engine.add_question("What is your favorite programming language?")
        self.assertIn("What is your favorite programming language?", self.engine.current_session['questions'])

    def test_end_session(self):
        self.engine.start_session()
        self.engine.end_session()
        self.assertFalse(self.engine.is_session_active)
        self.assertIsNotNone(self.engine.session_history)

    def test_retrieve_session_history(self):
        self.engine.start_session()
        self.engine.add_question("What is your favorite programming language?")
        self.engine.end_session()
        history = self.engine.retrieve_session_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]['questions'], ["What is your favorite programming language?"])


if __name__ == '__main__':
    unittest.main()