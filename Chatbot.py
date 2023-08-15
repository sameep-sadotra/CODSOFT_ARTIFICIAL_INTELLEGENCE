import re
import tkinter as tk
import random
from tkinter import scrolledtext

class SimpleChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")
        
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=40)
        self.text_area.pack(padx=10, pady=10)
        
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(padx=10, pady=10)
        
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)
        
        self.chat_log = []
        self.patterns_responses = [
            (r'\b(hi|hello|hey)\b', "Hello! How can I assist you today?"),
            (r'\b(how are you|how\s+are\s+you\s+doing)\b', "I'm just a chatbot, but I'm here to help you!"),
            (r'\b(bye|goodbye)\b', "Goodbye! Have a great day!"),
            (r'\b(thank you|thanks)\b', "You're welcome! If you have more questions, feel free to ask."),
            (r'\b(quote|quotes|quo|qote|give a quote|any other)\b', self.get_random_quote),
            (r'\b(joke|jokes|tell me a joke|give me a joke|jok|another one)\b', self.get_random_joke),
            
        ]
        
    def send_message(self):
        user_input = self.entry.get()
        self.chat_log.append("You: " + user_input)
        response = self.get_response(user_input)
        self.chat_log.append("Chatbot: " + response)
        self.update_text_area()
        self.entry.delete(0, tk.END)
    
    def get_response(self, user_input):
        for pattern, response in self.patterns_responses:
            if callable(response):
                if re.search(pattern, user_input.lower()):
                    return response()
            else:
                if re.search(pattern, user_input.lower()):
                    return response
        return "I'm sorry, I didn't quite understand that. Can you please rephrase or ask something else?"
    
    def update_text_area(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        for message in self.chat_log:
            self.text_area.insert(tk.END, message + "\n")
        self.text_area.config(state=tk.DISABLED)
        
    def get_random_quote(self):
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
        ]
        return random.choice(quotes)
    
    def get_random_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
            "I used to play piano by ear, but now I use my hands.",
            "I told my wife she was overreacting. She just flipped."
        ]
        return random.choice(jokes)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = SimpleChatbotGUI(root)
    root.mainloop()
