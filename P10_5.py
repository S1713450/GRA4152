# A question with a text and an answer.
#
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

class ChoiceQuestion(Question) :
    # The subclass has its own constructor.
    def __init__(self) :
        super().__init__()  
        self._choices = []

    # This method is added to the subclass.
    def addChoice(self, choice, correct) :
        self._choices.append(choice)
        if correct :
            # Convert the length of the list to a string.
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)

    # This method overrides a method from the superclass.
    def display(self) :
        # Display the question text.
        super().display()
        # Display the answer choices.
        for i in range(len(self._choices)) :
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices[i]))

class MultiChoiceQuestion(ChoiceQuestion) :
    # The subclass has its own constructor.
    def __init__(self) :
        super().__init__()

    def setAnswer(self, correctResponse) :
        # if _answer is not empty
        # concatenate " " and the answer 
        if self._answer != "": 
            self._answer = self._answer + " " + correctResponse
        else:
            self._answer = correctResponse
    

    # @return True if the response was correct, False otherwise
    #
    def checkAnswer(self, response) :
        # split the _answer and response into a lists
        responseList = response.split()
        answersList = self._answer.split()
        # sort and check if two lists are equal
        return sorted(responseList) == sorted(answersList)

    # This method overrides a method from the superclass.
    def display(self) :
        super().display()
        # add instruction
        print("More than one option can be correct. You should write all, separated by spaces.")

        
# testing
q = MultiChoiceQuestion()
q.setText("Which countries has won the world cup in football?")
q.addChoice("Germany", True)
q.addChoice("France", True)
q.addChoice("Italy", True)
q.addChoice("Norway", False)
q.addChoice("Brazil", True)

q.display()
print(q.checkAnswer("1 2 3 5")) #true expected
print(q.checkAnswer("1 2 3")) # false expected since brazil isnt mentioned
print(q.checkAnswer("12 3 5")) # false expected since no space 
