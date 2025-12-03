"""8. Viết chương trình graphic sử dụng thư viện Tkinter thực hiện:
a) Xây dựng form hiển thị thôn tin cá nhân (họ tên, ngày tháng năm sinh, MSSV,
ngành học)
b) Xây dựng form có nội dung như hình ở dưới, khi bấm vào nút “Click Me”
thông tin nút radio button đang lựa chọn sẽ được chỉ ra (tương ứng với các số 1,
2, 3)"""
import tkinter
import random

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 120      # Bước 2: đổi 30 → 120s

def startGame(event):
    if timeleft == 120:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # Bước 3: thay đổi điểm
        if e.get().lower() == colours[1].lower():
            score += 2        # đúng +2
        else:
            score -= 1        # sai -1

        e.delete(0, tkinter.END)
        random.shuffle(colours)

        label.config(fg = colours[1], text = colours[0])

        scoreLabel.config(text = "Score: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root, 
    text = "Type the COLOR of the word, not the text!",
    font = ('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press Enter to start",
                           font = ('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft),
                          font = ('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
