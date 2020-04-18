import tkinter as tk
import tkinter.ttk as ttk

class ClassCanvas(tk.Canvas):
    def __init__(self, master, img_width, img_height, bg):
        super().__init__(master, bg=bg, height=img_height, width=img_width)
        self.bar_x = tk.Scrollbar(self, orient="horizontal", command=self.xview)
        self.bar_y = tk.Scrollbar(self, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.bar_y.set, xscrollcommand=self.bar_x.set)
        self.configure(scrollregion=(0, 0, img_height, img_width))

        self.bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.place(x=0, y=0, relheight=1, relwidth=1)

class TicketForm:
    def __init__(self, width, height, title='TicketForm'):
        self.root = tk.Tk()
        self.window_width  = width
        self.window_height = height
        self.root.geometry(str(self.window_width) + "x" + str(self.window_height))
        self.root.title(title) 
        self.bg_color = "snow"

        #self.CreatePanedWindow()
        self.CreateFrame()
        self.CreateWidgets()

        #self.canvas = ClassCanvas(self.root, self.window_width, self.window_height, bg="snow")
        #self.canvas.bind("<ButtonPress-1>", self.move_start)
        #self.canvas.bind("<B1-Motion>", self.move_move)
        #self.canvas.bind("<MouseWheel>", self.zoom_in_out)
        #self.CreateFrame()
        #self.CreateWidgets()
        #self.test()


        self.root.mainloop()

    def test(self):
        print("test")
        # label_title = tk.Label(self.canvas, text="Title", width=10, bg='snow')
        # label_title.pack(side='top', anchor=tk.W, padx=5, pady=5, fill = 'none')
        # entry_title = tk.Entry(self.canvas, justify="left", width=100)
        # entry_title.pack(side='top', anchor=tk.W, padx=30, pady=5, fill = 'x')

        # label_description = tk.Label(self.canvas, text="Description", width=10, bg='snow')
        # label_description.pack(side='top', anchor=tk.W, padx=5, pady=5, fill = 'none')
        # entry_description = tk.Text(self.canvas, height=5, width=50, wrap=tk.CHAR)
        # entry_description.pack(side='top', anchor=tk.W, padx=30, pady=5, fill = 'x')

        # label_status = tk.Label(self.canvas, text="Status", width=10, bg='snow')
        # label_status.pack(side='top', anchor=tk.W, padx=5, pady=5, fill = 'none')

    def CreateFrame(self):
        self.frame = tk.Frame(self.root, bg = 'snow', bd=4, relief='ridge')
        self.frame.pack(expand=True, fill = tk.BOTH, side="left")

    def CreateWidgets(self):
        # Label
        label_title = tk.Label(self.frame, text="Title", width=20, bg='snow')
        ## padx , pady ：外側の横、縦の隙間
        label_title.grid(row=0, column=0, padx=2, pady=2)

        label_title2 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title3 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title4 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title5 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title6 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title7 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title8 = tk.Label(self.frame, text="Title", width=20, bg='snow')
        label_title2.grid(row=1, column=0, padx=2, pady=2)
        label_title3.grid(row=2, column=0, padx=2, pady=2)
        label_title4.grid(row=3, column=0, padx=2, pady=2)
        label_title5.grid(row=4, column=0, padx=2, pady=2)
        label_title6.grid(row=5, column=0, padx=2, pady=2)
        label_title7.grid(row=6, column=0, padx=2, pady=2)
        label_title8.grid(row=7, column=0, padx=2, pady=2)


        # Input line
        ##  justify：文字寄せ（center or left or right）
        ##  sticky：スペースが空いている場合の動き（tk.W + tk.E 縦横に広がる）
        entry_title = tk.Entry(self.frame, justify="left", width=50)
        entry_title.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)

        # Create button
        ## columnspan ：　何列に渡って配置するか
        ## rowspan ：　何行に渡って配置するか
        btn_select_file = tk.Button(self.frame, text="Create", command=self.CreateTicketJson) 
        btn_select_file.grid(row=4, column=0, sticky=tk.W + tk.E, padx=2, pady=2)

        # Combobox
        self.v1 = tk.StringVar()
        cb = ttk.Combobox(self.frame, textvariable=self.v1)
        cb.bind('<<ComboboxSelected>>', self.cb_selected)
        
        cb['values']=('Foo', 'Bar', 'Baz')
        cb.set("Foo")
        cb.grid(row=5, column=0)

    def cb_selected(self, event):
        print('v1 = %s' % self.v1.get())

    def callback(self, event):
        # Main Window以外のイベントは無視
        if (event.type != 'configure') and (event.widget != self.root):
            print("move")


        # サイズが変わってなかった無視
        # if (event.width == width) and (event.height == height):
        #     return

        # グローバル変数を更新
        # width = event.width
        # height = event.height

        # ボタンを移動する
        #btn.place_forget() #不要かもしれないが、とりあえず明示的に記述しておく
        #btn.place(x=(width-200), y=0, width=200, height=30)


    def CreateTicketJson(self):
        print('json ファイルに保存')

def main():
    TicketForm(640, 480, "New Ticket")


if __name__ == "__main__":
    main()