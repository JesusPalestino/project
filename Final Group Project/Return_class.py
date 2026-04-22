
class Game:
    def __init__(self, region): 
        self.region = region
        self.guesses = []
        self.data = {}
    
    def add_guess(self, data):
        self.guesses.append(data)
    def get_guesses(self):
        return self.guesses
    def load_data(self, filename):
        file = open(filename, 'r', encoding = 'utf-8')

        for line in file:
            state, capital = line.strip().split(',')
            self.data[state.lower()] = capital.lower()
        
        file.close()
    def run(self):
        while True:
            user_input = input('Enter a guess or done: ').lower()
            if user_input == 'done':
                    return self.guesses
            
            if user_input in self.guesses:
                print('You have already guessed this capital.')
                continue
           
            self.add_guess(user_input)

            if user_input in self.data.values():
                print('Correct!')
            else:
                print('That is incorrect')
    def remaining(self):
        correct_capitals = set(self.data.values())
        guessed_capitals = set(self.guesses)
        return correct_capitals - guessed_capitals
    
g = Game('Africa')
g.load_data('australia.csv')
results = g.run()
print(results)    
print(g.remaining())    
