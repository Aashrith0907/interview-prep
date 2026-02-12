# interview_engine.py

class InterviewEngine:
    def __init__(self):
        self.sessions = []
        self.current_session = None

    def start_session(self, candidate_name):
        self.current_session = {'candidate': candidate_name, 'questions': [], 'score': 0}
        self.sessions.append(self.current_session)

    def add_question(self, question):
        if self.current_session is not None:
            self.current_session['questions'].append(question)
        else:
            raise Exception("No active session")

    def evaluate_answer(self, question, answer):
        # This method should include logic to evaluate the answer
        pass  # Placeholder for answer evaluation logic

    def end_session(self):
        if self.current_session is not None:
            # Logic to finalize the session
            final_score = self.current_session['score']
            self.current_session = None
            return final_score
        else:
            raise Exception("No active session to end")

    def get_sessions(self):
        return self.sessions

# Example Usage:
# engine = InterviewEngine()
# engine.start_session('John Doe')
# engine.add_question('What is Python?')
# engine.evaluate_answer('What is Python?', 'A programming language.')
# score = engine.end_session()
# print(score)