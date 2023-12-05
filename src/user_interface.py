# src/user_interface.py

class UserInterface:
    def __init__(self):
        # Initialize any necessary variables or data structures
        pass

    def get_user_input(self):
        # Prompt the user to input their ideas for the song
        # Return the input as a string
        pass

    def display_ideas(self, ideas):
        # Display the user's ideas to the user
        pass

    def save_ideas(self, ideas):
        # Save the user's ideas to a file for future reference
        pass
    def load_ideas(self):
        # Load the user's saved ideas from a file
        with open("ideas.txt", "r") as file:
            self.ideas = file.read()
