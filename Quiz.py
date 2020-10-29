from tkinter import *
import tkinter.messagebox


def root():
    root = Tk()
    root.geometry("3840x2160")
    window2.destroy()

    def destroy():
        root.destroy()

    def easy():
        def incorrect():
            tkinter.messagebox.showinfo('Radar gaming', "     Incorrect!     ")
            answer = tkinter.messagebox.askquestion('question 1', 'Do you want to move to next question')
            if answer == 'yes':
                medium()

        def correct():
            tkinter.messagebox.showinfo('Answer', "     Correct!   ")
            answer = tkinter.messagebox.askquestion('question 1', 'Do you want to move to next question')
            with open("result.txt", "w") as f:
                f.write("1" + "\n")
            if answer == 'yes':
                medium()

        def shows():
            Button2 = Button(easyquestion, text="Three", font=("Halvatica", 20), bg="orange", command=incorrect,
                             width=7)
            Button2.grid(row=6, column=0, padx=10, pady=20)
            Button3 = Button(easyquestion, text="Four", font=("Halvatica", 20), bg="orange", command=incorrect, width=7)
            Button3.grid(row=6, column=2, padx=10, pady=20)
            Button4 = Button(easyquestion, text="Two", font=("Halvatica", 20), bg="orange", command=correct, width=7)
            Button4.grid(row=7, column=0, padx=10, pady=20)
            Button5 = Button(easyquestion, text="Five", font=("Halvatica", 20), bg="orange", command=incorrect, width=7)
            Button5.grid(row=7, column=2, padx=10, pady=20)

        easyquestion = Tk()
        easyquestion["bg"] = "skyblue"
        easyquestion.geometry("1900x500")
        easyquestion.counter = 0

        label1 = Label(easyquestion, text="1) How many marks you get for 75% attandence in LPU?",
                       font=("Halvatica", 30), bg="skyblue")
        label1.grid(row=2, column=1, padx=20, pady=40)
        showbutton = Button(easyquestion, text="Show-Option", font=("Halvatica", 20), bg="skyblue", command=shows)
        showbutton.grid(row=4, column=0, padx=10, pady=10)
        easyquestion.mainloop()

    def medium():

        def backbutton2():
            easy()

        def incorrect():
            tkinter.messagebox.showinfo('Radar gaming', "     Incorrect!     ")
            answer = tkinter.messagebox.askquestion('question 1', 'Do you want to move to next question')
            if answer == 'yes':
                hard()

        def correct():
            tkinter.messagebox.showinfo('Radar gaming', "     Correct!   ")
            answer = tkinter.messagebox.askquestion('question 1', 'Do you want to move to next question')
            with open("result.txt", "a") as f:
                f.write("1" + "\n")
            if answer == 'yes':
                hard()

        def shows2():
            Button6 = Button(mediumquestion, text="lion", font=("Halvatica", 20), bg="orange", command=incorrect,
                             width=7)
            Button6.grid(row=6, column=0, padx=10, pady=20)
            Button7 = Button(mediumquestion, text="penguins", font=("Halvatica", 20), bg="orange", command=correct,
                             width=7)
            Button7.grid(row=6, column=2, padx=10, pady=20)
            Button8 = Button(mediumquestion, text="tiger", font=("Halvatica", 20), bg="orange", command=incorrect,
                             width=7)
            Button8.grid(row=7, column=0, padx=10, pady=20)
            Button9 = Button(mediumquestion, text="wolf", font=("Halvatica", 20), bg="orange", command=incorrect,
                             width=7)
            Button9.grid(row=7, column=2, padx=10, pady=20)

        mediumquestion = Tk()
        mediumquestion.geometry("1900x500")
        mediumquestion['bg'] = "skyblue"

        backbutton2 = Button(mediumquestion, text="back", font=("Halvatica", 10), bg="gray", command=backbutton2)
        backbutton2.grid(row=0, column=0, padx=5, pady=5)

        label3 = Label(mediumquestion, text="2) Which animal sleeps keeping eyes open?", font=("Halvatica", 30),
                       bg="skyblue")
        label3.grid(row=2, column=1, padx=20, pady=40)
        showbutton2 = Button(mediumquestion, text="Show-Option", font=("Halvatica", 20), bg="skyblue", command=shows2)
        showbutton2.grid(row=4, column=0, padx=10, pady=10)

        mediumquestion.mainloop()

    def hard():

        def backbutton3():
            medium()

        def incorrect():
            tkinter.messagebox.showinfo('Radar gaming', "     Incorrect!     ")
            answer = tkinter.messagebox.askquestion('question 1', 'Do you want to move to next question')
            if answer == 'yes':
                answer1()

        def correct():
            tkinter.messagebox.showinfo('Radar gaming', "     Correct!   ")
            answer = tkinter.messagebox.askquestion('question 1', 'Do you want to move to next question')
            with open("result.txt", "a") as f:
                f.write("1" + "\n")
            if answer == 'yes':
                answer1()

        def answer1():
            f = open("output.txt", "r")
            output = f.read()
            output = str(output)
            output.strip('}')
            f.close()
            answer = Tk()
            answer.geometry("3840x2160")
            answer["bg"] = "black"
            label = Label(answer, text=output, font=("Halvatica", 20), bg="black", fg="red")
            label.pack()
            label2 = Label(answer, text="You have completed the test", font=("Halvatica", 20), bg="black", fg="red")
            label2.pack()
            label1 = Label(answer, text="THANKYOU", font=("Fantasy", 50), bg="black", fg="red")
            label1.pack()
            with open('result.txt', 'r') as f:
                result = sum(map(int, f))

            def score():
                score = Tk()
                score["bg"] = "black"
                with open('result.txt', 'r') as f:
                    result = sum(map(int, f))
                label = Label(score, text=result, font=("Halvatica", 50), bg="black", fg="red")
                label.pack()

            buttonv = Button(answer, text="Check Score", font=("Halvatica", 20), bg="orange", command=score)
            buttonv.pack()

            answer.mainloop()

        def shows2():
            Button_6 = Button(hardquestion, text="December 1989", font=("Halvatica", 20), bg="orange", command=correct,
                              width=15)
            Button_6.grid(row=6, column=0, padx=10, pady=20)
            Button_7 = Button(hardquestion, text="December 1987", font=("Halvatica", 20), bg="orange",
                              command=incorrect, width=15)
            Button_7.grid(row=6, column=2, padx=10, pady=20)
            Button_8 = Button(hardquestion, text="December 1988", font=("Halvatica", 20), bg="orange",
                              command=incorrect, width=15)
            Button_8.grid(row=7, column=0, padx=10, pady=20)
            Button_9 = Button(hardquestion, text="December 1980", font=("Halvatica", 20), bg="orange",
                              command=incorrect, width=15)
            Button_9.grid(row=7, column=2, padx=10, pady=20)

        hardquestion = Tk()
        hardquestion.geometry("1900x500")
        hardquestion['bg'] = "skyblue"

        backbutton3 = Button(hardquestion, text="back", font=("Halvatica", 10), bg="gray", command=backbutton3)
        backbutton3.grid(row=0, column=0, padx=5, pady=5)

        label5 = Label(hardquestion, text="3) When was python implementation started?", font=("Halvatica", 30),
                       bg="skyblue")
        label5.grid(row=2, column=1, padx=20, pady=40)

        showbutton2 = Button(hardquestion, text="Show-Option", font=("Halvatica", 20), bg="skyblue", command=shows2)
        showbutton2.grid(row=4, column=0, padx=10, pady=10)

        hardquestion.mainloop()

    button_1 = Button(root, text="Easy", font=("Halvatica", 30), bg="maroon", command=lambda: [destroy(), easy()],
                      width=7)
    button_1.pack(side=LEFT, padx=100)
    button_2 = Button(root, text="Medium", font=("Halvatica", 30), bg="maroon", command=lambda: [destroy(), medium()],
                      width=7)
    button_2.pack(side=LEFT, padx=300)
    button_3 = Button(root, text="Hard", font=("Halvatica", 30), bg="maroon", command=lambda: [destroy(), hard()],
                      width=7)
    button_3.pack(side=RIGHT, padx=100)
    root.title("types")
    root['bg'] = "black"
    root.mainloop()


def window():
    def Quit():
        window.destroy()

    window = Tk()
    window['bg'] = 'black'
    window.geometry("3840x2160")
    window.title("QUIZ")
    label = Label(window, text="WELCOME TO QUIZ", font=("Helvetica", 100), bg="maroon")
    label.pack(fill=X)
    buttons = Button(window, text="Start", bg="maroon", font=("Halvatica", 30), command=lambda: [Quit(), root()])
    buttons.pack(side=LEFT, padx=250)
    button1 = Button(window, text="Quit", bg="maroon", font=("Helvatica", 30), command=Quit)
    button1.pack(side=RIGHT, padx=250)
    window.mainloop()


window2 = Tk()
window2["bg"] = "black"
labe = Label(window2, text="Name", font=("Halvatica", 10), bg="orange")
labe.grid(row=1, column=0, padx=5, pady=5)
entry = Entry(window2)
entry.grid(row=1, column=1, padx=5, pady=5)
button = Button(window2, text="Login", font=("Halvatice", 10), bg="orange", command=lambda: [save_data(), window()])
button.grid(row=5, column=1, padx=20, pady=20)


def save_data():
    with open("output.txt", "w") as f:
        f.write("Dear" + " " + entry.get())


window2.mainloop()
