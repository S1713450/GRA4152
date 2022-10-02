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
    # Converting all words to upper and removing spaces
    # converting both to lower would also work
    def checkAnswer(self, response) :
        return response.upper().replace(" ","") == self._answer.upper().replace(" ","")
    
    ## Displays this question.
    #
    def display(self) :
        print(self._text)

# Testing

q = Question()
q.setText("Which country has the longest coastline?")
q.setAnswer("Canada")
q.display()
print(q.checkAnswer("CaNADA"))#true expected
print(q.checkAnswer("CANADA"))#true expected
print(q.checkAnswer("can ada"))#true expected

