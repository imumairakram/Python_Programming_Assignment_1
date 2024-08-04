# Question_1:
class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_list(self):
        print("Grocery List:")
        for item in self.items:
            print(item)

grocery_list = GroceryList()

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        grocery_list.add_item(item)
    elif choice == "2":
        item = input("Enter item to remove: ")
        grocery_list.remove_item(item)
    elif choice == "3":
        grocery_list.display_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")


#Quesgtion_2
def calculate_average_grade(grades):
    return sum(grades.values()) / len(grades)

grades = {
    "Student 1": 85,
    "Student 2": 90,
    "Student 3": 78,
    "Student 4": 92,
    "Student 5": 88
}

average_grade = calculate_average_grade(grades)
print("Average grade:", average_grade)



#Question_3:
def count_word_frequencies(word_list):
    frequencies = {}
    for word in word_list:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
frequencies = count_word_frequencies(word_list)
print("Word frequencies:")
for word, frequency in frequencies.items():
    print(word, ":", frequency)



#Question_4:
def check_password_strength(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

password = input("Enter a password: ")
if check_password_strength(password):
    print("Password is strong")
else:
    print("Password is weak")


#Question_5
class VotingSystem:
    def __init__(self):
        self.candidates = ["Candidate A", "Candidate B", "Candidate C"]
        self.votes = {candidate: 0 for candidate in self.candidates}

    def vote(self):
        print("Candidates:")
        for i, candidate in enumerate(self.candidates):
            print(f"{i+1}. {candidate}")
        choice = input("Enter the number of your chosen candidate: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.candidates):
            chosen_candidate = self.candidates[int(choice) - 1]
            self.votes[chosen_candidate] += 1
            print("Vote recorded successfully!")
        else:
            print("Invalid choice. Please try again.")

    def display_results(self):
        print("Voting results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")

voting_system = VotingSystem()
num_voters = int(input("Enter the number of voters: "))

for _ in range(num_voters):
    voting_system.vote()

voting_system.display_results()