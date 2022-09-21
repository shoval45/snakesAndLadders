# Import the required Libraries
from tkinter import *
from tkinter import ttk


def question1():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("500x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text=" :בישראל זיהום אוויר בולט באזור",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="תל אביב", command=open_popup_lose).pack()
    ttk.Button(win, text="חיפה", command=open_popup_win).pack()
    win.mainloop()


def question2():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("500x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text=" ?איזה מזהם אוויר כרוך בסכנת קרינה",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="חנקן חד חמצני", command=open_popup_lose).pack()
    ttk.Button(win, text="ראדון", command=open_popup_win).pack()
    win.mainloop()


def question3():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("500x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text=" ?מה מבין הבאים הוא דוגמה לזיהום אוויר ממקורות טבעיים",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="גשם חומצי", command=open_popup_lose).pack()
    ttk.Button(win, text="התפרצות הר געש", command=open_popup_win).pack()
    win.mainloop()


def question4():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("500x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text=" ?לכמה סוגים נחלקים מזהמי האוויר",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="4", command=open_popup_lose).pack()
    ttk.Button(win, text="2", command=open_popup_win).pack()
    win.mainloop()


def question5():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("500x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text=" ?מהו מקור גז הראדון בבתים",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="זיהום מפחמן חד חמצני",
               command=open_popup_lose).pack()
    ttk.Button(win, text="האדמה עליה ממוקם הבית",
               command=open_popup_win).pack()
    win.mainloop()


def question6():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("500x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text="?בזמן נהיגה נפלטים לאוויר גזים וגרגרי אבק. למה הם גורמים",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="אבק", command=open_popup_lose).pack()
    ttk.Button(win, text="גשם חומצי", command=open_popup_win).pack()
    win.mainloop()


def question7():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("700x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win,
          text="...למעלה ממחצית מקרי המוות המוקדם כתוצאה מזיהום אוויר מתרחשים ב",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="אפריקה והודו", command=open_popup_lose).pack()
    ttk.Button(win, text="הודו וסין", command=open_popup_win).pack()
    win.mainloop()


def question8():
    # Create an instance of Tkinter frame
    win = Tk()
    win.title("Question")

    # Set the geometry of Tkinter frame
    win.geometry("700x150")

    def open_popup_win():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Correct answer")
        Label(top, text="!תשובה נכונה", font=('Mistral 18 bold')).place(x=150,
                                                                        y=80)
        win.after(2500, lambda: win.destroy())

    def open_popup_lose():
        top = Toplevel(win)
        top.geometry("500x150")
        top.title("Wrong answer")
        Label(top, text="תשובה שגויה", font=('Mistral 18 bold')).place(x=150,
                                                                       y=80)

    win.after(2500, lambda: win.destroy())

    Label(win, text="הפחמן החד-חמצני הוא גז חסר ריח, צבע וטעם",
          font=('Helvetica 14 bold')).pack(pady=20)

    # Create a button in the main Window to open the popup
    ttk.Button(win, text="לא נכון", command=open_popup_lose).pack()
    ttk.Button(win, text="נכון", command=open_popup_win).pack()
    win.mainloop()
