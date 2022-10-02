# -*- coding: utf-8 -*-
class Question :
    ## Constructs a question with empty question and answer strings.
    #
    def __init__(self) :
        self._text = ""
        self._answer = ""
    
    ## Sets the question text.
    # @param questionText the text of this question
    #
    def setText(self, questionText) :
        self._text = questionText
    
    ## Sets the answer for this question.
    # @param correctResponse the answer
    #
    def setAnswer(self, correctResponse) :
        self._answer = correctResponse
    
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    #
    def checkAnswer(self, response) :
        return response == self._answer
    
    ## Displays this question.
    #
    def display(self) :
        print(self._text)

class NumericQuestion(Question) :
    # Creating an own constructor for the subclass NumericQuestion
    def __init__(self) :
        super().__init__()  

    def checkAnswer(self, response):
        # converts answer and response to float
        # Checks if difference between answer and response is less than 0.01
        # Returns Correct if difference is less, false otherwise
        try:
            dif = abs(float(self._answer) - float(response))
            if float("{0:.10f}".format(dif)) <= 0.01:
                return print("Correct")
            else:
                return print("False")
        except: 
            raise ValueError("The answer must be a number.") # Error if not possible
    def setAnswer(self, correctResponse) :
        try:
            self._answer = float(correctResponse) # tries to convert answer fo float
        except: 
            raise ValueError("The answer must be a number.") # Error if not possible

# Testing
q = NumericQuestion()
q.setText("What is the value of pi?") # creating question text
q.setAnswer(3.1415926) #Sets answer
q.display() #Displays question, uses method from superclass
q.checkAnswer(3.14) #Since answer is less than 0.01 from true answer, correct is expected
print("Correct was expected, since difference is less than 0.01")

q2 = NumericQuestion()
q2.setText("What is the value of pi?") # creating question text
q2.setAnswer(3.1415926) #Sets answer
q2.display() #Displays question, uses method from superclass
q2.checkAnswer(3.13) #Since answer is more than 0.01 from true answer, false is expected
print("False was expected, since difference is more than 0.01")

q3 = NumericQuestion()
q3.setText("What is the value of pi?") # creating question text
q3.setAnswer("3.1415926") #Sets answer as string, but its able to convert numbers inside string
q3.display() #Displays question, uses method from superclass
q3.checkAnswer(3.14) #Since answer is less than 0.01 from true answer, correct is expected
print("Correct was expected, since float function is able to convert numbers inside string")

q4 = NumericQuestion()
q4.setText("What is the value of pi?") # creating question text
q4.setAnswer(3.1415926) #Sets answer
q4.display() #Displays question, uses method from superclass
print("Error message informing that it must be a number is expected, since its a non numeric string")
q4.checkAnswer("Error") #Error message since its a non numeric strig
