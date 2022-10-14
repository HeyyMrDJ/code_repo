"""Language survey"""
from survey import AnonymousSurvey

# Define a question, and make a survey
QUESTION = "What langauge did you first learn to speak?"
my_survey = AnonymousSurvey(QUESTION)

# Show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
