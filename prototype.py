# 🌸 StutterAware AI — simple conceptual prototype
# student-led neuroscience & communication awareness project

import random

class StutterAwareAI:

    def __init__(self):

        self.support_messages = [
            "Take your time. Your voice matters 💛",
            "Communication is more than fluency 🧠",
            "You deserve patience and understanding 🌸",
            "Speaking differently does not make you less intelligent ✨"
        ]

        self.learning_topics = [
            "What is stuttering?",
            "How the brain controls speech",
            "Speech anxiety & communication",
            "Neurodiversity awareness",
            "Understanding synapses"
        ]

    def welcome(self):
        print("🌸 Welcome to StutterAware AI")
        print("A student-led digital health & neuroscience awareness concept.\n")

    def show_topics(self):
        print("🧠 Available Learning Topics:")
        for topic in self.learning_topics:
            print("-", topic)

    def encouragement(self):
        print("\n💛 Support Message:")
        print(random.choice(self.support_messages))

    def user_goal(self):
        print("\n🎤 Project Goal:")
        print("Creating safer and more accessible communication spaces.")


# run prototype
app = StutterAwareAI()

app.welcome()
app.show_topics()
app.encouragement()
app.user_goal()

Added simple StutterAware AI prototype
