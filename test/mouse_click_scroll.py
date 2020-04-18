import tkinter as tk
import random


class ClassCanvas(tk.Canvas):
    def __init__(self, master, img_width, img_height, bg):
        super().__init__(master, bg=bg, height=img_height, width=img_width)
        self.bar_x = tk.Scrollbar(self, orient="horizontal", command=self.xview)
        self.bar_y = tk.Scrollbar(self, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.bar_y.set, xscrollcommand=self.bar_x.set)
        self.configure(scrollregion=(0, 0, 1000, 1000))

        self.bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        for n in range(50):
            x0 = random.randint(0, 900)
            y0 = random.randint(50, 900)
            x1 = x0 + random.randint(50, 100)
            y1 = y0 + random.randint(50, 100)
            color = ("red", "orange", "yellow", "green", "blue")[random.randint(0, 4)]
            self.create_rectangle(x0, y0, x1, y1, outline="black", fill=color, activefill="black", tags=n)


class ClassForm:
    def __init__(self, width, height):
        self.root = tk.Tk()
        # windowサイズの初期化
        self.window_width = width
        self.window_height = height
        self.root.geometry(str(self.window_width) + "x" + str(self.window_height) + "+100+100")
        self.bg_color = "snow"

        self.canvas = ClassCanvas(self.root, 1000, 1000, bg="white")
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        self.canvas.bind("<MouseWheel>", self.zoom_in_out)

        self.root.mainloop()

    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def zoom_in_out(self, event):
        if event.delta > 0:
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif event.delta < 0:
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


def main():
    ClassForm(640, 480)


if __name__ == "__main__":
    main()