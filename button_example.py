import tkinter as tk


class App:
    def __init__(self, root):
        root.title("打招呼测试")
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame, text="打招呼", fg="blue", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("您刚才通过点击打招呼触发了我:大家好，我是badao！")


root = tk.Tk()
app = App(root)

root.mainloop()