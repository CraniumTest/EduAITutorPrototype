from eduai_tutor import EduAITutor

def main():
    tutor = EduAITutor(user_id='student_123')
    
    # Example: Personalized setup
    tutor.set_learning_profile({'math': 'beginner', 'history': 'intermediate'})
    
    # Interactive query
    response = tutor.ask_question("What is Pythagorean Theorem?")
    print("EduAI Response:", response)

    # Track progress
    tutor.track_progress({'math': 70, 'history': 85})

if __name__ == "__main__":
    main()
