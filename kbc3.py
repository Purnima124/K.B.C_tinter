from tkinter import*
from time import sleep
from tkinter. constants import LEFT
from tkinter .font import BOLD
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter
    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, font=("Arial",20,BOLD),text="Right!")
            right += 1
        else:
            label = Label(view,font=("Arial",20,BOLD) ,text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))
    def getView(self, window):
        view = Frame(window)
        Label(view,font=("Arial",20,BOLD),text=self.question).pack()
        Button(view,font=("Arial",20,BOLD), text=self.answers[0], command=lambda *args: self.check("A", view),fg="red").pack(side=LEFT)
        Button(view,font=("Arial",20,BOLD), text=self.answers[1], command=lambda *args: self.check("B", view),fg="red").pack(side=LEFT)
        Button(view,font=("Arial",20,BOLD), text=self.answers[2], command=lambda *args: self.check("C", view),fg="red").pack(side=LEFT)
        Button(view,font=("Arial",20,BOLD), text=self.answers[3], command=lambda *args: self.check("D", view),fg="red").pack(side=LEFT)
        return view
    def unpackView(self, view):
        view.pack_forget()
        askQuestion()
def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()
questions = []
file = open("question.text")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)
window = Tk()
label=Label(window,font=("Arial",20,BOLD),text="welcome to kbc game")
button = Button(window,font=("Arial",20,BOLD),text="Start", command=askQuestion)
button.pack()
window.mainloop()
