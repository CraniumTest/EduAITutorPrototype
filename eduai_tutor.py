import openai

class EduAITutor:

    def __init__(self, user_id):
        self.user_id = user_id
        self.learning_path = {}
        self.performance = {}

    def set_learning_profile(self, profile):
        self.learning_path = profile

    def ask_question(self, question):
        # Interact with OpenAI API
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def track_progress(self, scores):
        self.performance.update(scores)
        print(f"Updated Scores: {self.performance}")
