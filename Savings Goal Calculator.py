# Lab9 - Savings Goal Calculator
# Name: Alisha
# Date: 12/1/2025
# Description: This program calculates how many weeks it will take to reach a
#              savings goal based on weekly savings amount, gives feedback
#              based on time to reach the goal, and prints summary information
#              after the user is done.
# input: Savings goal amount and weekly savings amount
# output: Number of weeks needed to reach the savings goal, feedback, and summary statistics after all runs

# ---------------- Sample Run ----------------
# Enter your savings goal amount: 1000
# Enter how much you can save each week: 40
# You will reach your savings goal in 25.00 weeks.
# You will reach your goal in about a year. You're doing great!
# Do you want to run the program again? (y/n): y
#
# Enter your savings goal amount: 800
# Enter how much you can save each week: 20
# You will reach your savings goal in 40.00 weeks.
# You will reach your goal in about a year. You're doing great!
# Do you want to run the program again? (y/n): n
#
# ----- Summary of Your Savings Plans -----
# You completed 2 calculations.
# Average weekly savings: $30.00
# Largest saving goal entered: $1000.00
# Thank you for using the Savings Goal Calculator!
# --------------------------------------------


import valid

class SavingsEntry:
    """Class to store savings goal information for one calculation."""

    def __init__(self, goal=0.0, weekly=0.0):
        self.__goal = goal
        self.__weekly = weekly
        self.__weeks_needed = 0.0
        self.__feedback = ""

    def get_goal(self):
        return self.__goal

    def get_weekly(self):
        return self.__weekly

    def get_weeks_needed(self):
        return self.__weeks_needed

    def get_feedback(self):
        return self.__feedback

    def set_goal(self, goal):
        self.__goal = goal

    def set_weekly(self, weekly):
        self.__weekly = weekly

    def set_weeks_needed(self, weeks):
        self.__weeks_needed = weeks

    def set_feedback(self, feedback):
        self.__feedback = feedback

    def __str__(self):
        result = f"Savings goal: ${self.__goal:.2f}, Weekly savings: ${self.__weekly:.2f}, Weeks needed: {self.__weeks_needed:.2f}\nFeedback: {self.__feedback}"
        return result


def get_goal_amount():
    goal_amount = 0.0
    while goal_amount <= 0:
        goal_amount = valid.get_real("Enter your savings goal amount: ")
        if goal_amount <= 0:
            print("Please enter a positive amount greater than 0.")
    return goal_amount

def get_weekly_savings():
    weekly_savings = 0.0
    while weekly_savings <= 0:
        weekly_savings = valid.get_real("Enter how much you can save each week: ")
        if weekly_savings <= 0:
            print("Please enter a positive amount greater than 0.")
    return weekly_savings

def calc_weeks_needed(goal_amount, weekly_savings):
    """
    Calculates the weeks needed to save goal amount
    :param goal_amount: float - Total savings goal amount
    :param weekly_savings: float - Weekly savings amount
    :return: float - Number of weeks required to reach the goal
    """
    result = goal_amount / weekly_savings
    return result

def generate_feedback(weeks_needed, weekly_savings):
    feedback = ""
    if weekly_savings < 20:
        feedback += "That's a slow start, try saving a little more each week. "
    elif weekly_savings >= 200:
        feedback += "Perfect! You are saving a lot every week! "

    if weeks_needed <= 24:
        feedback += "Nice work! You will reach your goal in less than 6 months."
    elif weeks_needed <= 52:
        feedback += "You will reach your goal in about a year. You're doing great!"
    else:
        feedback += "This will take more than a year. Consider saving more weekly!"
    return feedback

def print_result(entry):
    """Prints result using the SavingsEntry object."""
    print(f"You will reach your savings goal in {entry.get_weeks_needed():.2f} weeks.")
    print(entry.get_feedback())

def print_summary(entries):
    print("----- Summary of Your Savings Plans -----")
    count = len(entries)
    print(f"You completed {count} calculations.")

    if count == 0:
        print("No calculations to summarize.")
        return

    total_weekly = 0.0
    max_goal = entries[0].get_goal()
    for e in entries:
        total_weekly += e.get_weekly()
        if e.get_goal() > max_goal:
            max_goal = e.get_goal()

    avg_weekly = total_weekly / count

    print(f"Average weekly savings: ${avg_weekly:.2f}")
    print(f"Largest saving goal entered: ${max_goal:.2f}")


def main():
    entries = []
    run_again = 'y'

    while run_again.lower() == 'y':
        goal = get_goal_amount()
        weekly = get_weekly_savings()
        weeks_needed = calc_weeks_needed(goal, weekly)
        feedback = generate_feedback(weeks_needed, weekly)

        entry = SavingsEntry(goal, weekly)
        entry.set_weeks_needed(weeks_needed)
        entry.set_feedback(feedback)

        print_result(entry)
        entries.append(entry)

        run_again = valid.get_y_or_n("Do you want to run the program again? (y/n): ")
        print()

    print_summary(entries)
    print("Thank you for using the Savings Goal Calculator!")

main()
