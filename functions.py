import random
import tkinter
import consts


def random_dice():
    FONT_SIZE = 40

    root = tkinter.Tk()
    root.geometry("300x200")
    root.title("DICE")

    rnd_number = random.randint(1,6)
    if rnd_number == 1:
        dice_label = tkinter.Label(root, text='1', font=(consts.FONT_NAME, FONT_SIZE))
        dice_label.place(x=150, y=70)
    if rnd_number == 2:
        dice_label = tkinter.Label(root, text='2', font=(consts.FONT_NAME, FONT_SIZE))
        dice_label.place(x=150, y=70)
    if rnd_number == 3:
        dice_label = tkinter.Label(root, text='3', font=(consts.FONT_NAME, FONT_SIZE))
        dice_label.place(x=150, y=70)
    if rnd_number == 4:
        dice_label = tkinter.Label(root, text='4', font=(consts.FONT_NAME, FONT_SIZE))
        dice_label.place(x=150, y=70)
    if rnd_number == 5:
        dice_label = tkinter.Label(root, text='5', font=(consts.FONT_NAME, FONT_SIZE))
        dice_label.place(x=150, y=70)
    if rnd_number == 6:
        dice_label = tkinter.Label(root, text='6', font=(consts.FONT_NAME, FONT_SIZE))
        dice_label.place(x=150, y=70)
    root.mainloop()
    return rnd_number


random_dice()