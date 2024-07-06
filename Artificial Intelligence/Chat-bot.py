import random
import re

class NLPBot:
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    
    nlp_questions = (
        ("What is NLP (Natural Language Processing)?", "about_nlp_intent"),
        ("How does NLP enable machines to understand human language?", "about_nlp_intent"),
        ("Can you explain text classification in NLP?", "about_nlp_intent"),
        ("What are some applications of NLP?", "about_nlp_intent"),
        ("Tell me about sentiment analysis in NLP.", "about_nlp_intent"),
    )
    
    def __init__(self):
        self.name = ""
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_nlp_intent': r'.*\s*nlp.*',
        }
    
    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am NLPBot. How can I assist you with NLP?\n")
        if any(command in will_help.lower() for command in self.exit_commands):
            print("Have a nice day!")
            return
        self.chat()
        
    def make_exit(self, reply):
        return any(reply.lower() == command for command in self.exit_commands)

    def chat(self):
        while True:
            reply = input("Ask me something about NLP:\n").lower()
            if self.make_exit(reply):
                print("Have a nice day!")
                break
            response = self.match_reply(reply)
            print(response)
    
    def match_reply(self, reply):
        for question, intent in self.nlp_questions:
            if re.match(question.lower(), reply):
                return self.choose_response(intent)
        
        for intent, regex_pattern in self.alienbabble.items():
            if re.match(regex_pattern, reply):
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_nlp_intent':
                    return self.about_nlp_intent()
        
        return self.no_match_intent()
    
    def choose_response(self, intent):
        if intent == 'about_nlp_intent':
            return self.about_nlp_intent()
        else:
            return "I'm sorry, I didn't understand that question."
    
    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms.\n",
                     "I heard the coffee is good.\n")
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = ("I come in peace.\n",
                     "I am here to collect data on your planet and its inhabitants.\n",
                     "I heard the coffee is good.\n")
        return random.choice(responses)
    
    def about_nlp_intent(self):
        responses = ("NLP (Natural Language Processing) is a field of AI focused on enabling machines to understand and process human language.\n",
                     "NLP involves tasks like text classification, sentiment analysis, and language translation.\n",
                     "NLP is crucial for developing chatbots, language models, and other AI applications.\n")
        return random.choice(responses)
    
    def no_match_intent(self):
        responses = ("Please tell me more.\n",
                     "Tell me more!\n",
                     "I see. Can you elaborate?\n",
                     "Interesting. Can you tell me more?\n",
                     "I see. How do you think?\n",
                     "Why?\n",
                     "How do you think I feel when I say that? Why?\n")
        return random.choice(responses)

bot = NLPBot()
bot.greet()
