
class Game:
    def __init__(self, region): 
        self.region = region
        self.guesses = []
        self.data = {}

    def add_guess(self, data):
        self.guesses.append(data)

    def get_guesses(self):
        return self.guesses
    
# Accessing file from folder *****Used online Resources as reference*****
    def load_data(self, filename):
        file = open(filename, 'r', encoding = 'utf-8')
        header = file.readline()
        for line in file:
            state, capital = line.strip().split(',')
            self.data[state.lower()] = capital.lower()
        
        file.close()

# Taking input from user (guess or done)
        while True:
            user_input = input('Enter a guess or done: ').lower()
            if user_input == 'done':
                    return self.guesses
            
            # Check for redundancy
            if user_input in self.guesses:
                print('You have already guessed this capital.')
                continue

            # Add guess to list
            self.add_guess(user_input)

            # Reference csv file against user input
            if user_input in self.data.values():
                print('Correct!')
            else:
                print('That is incorrect')

    # Return remaining capitals
    def remaining(self):
        correct_capitals = set(self.data.values())
        guessed_capitals = set(self.guesses)
        return correct_capitals - guessed_capitals
    
 
