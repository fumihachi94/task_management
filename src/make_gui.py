import sys
import os
import numpy as np
import tkinter as tk

import tkinter.ttk as ttk
from PIL import Image, ImageDraw
from tkinter import messagebox
from tkinter import filedialog


# アプリケーション（GUI）クラス
class Application(tk.Frame):
    DEBUG_LOG = True
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""
        
        # PanedWindow
        ##  orient : 配置（vertical or horizontal）
        ##  bg     : 枠線の色
        # pack
        ##  expand : 可変（True or False(固定)
        ##  fill   : スペースが空いている場合の動き（tk.BOTH　縦横に広がる）
        ##  side   : 配置する際にどの方向からつめていくか（side or top ・・・
        pw_main = tk.PanedWindow(self.master, orient='horizontal',sashwidth = 4)
        pw_main.pack(expand=True, fill = tk.BOTH, side="left")
        pw_left = tk.PanedWindow(pw_main, bg="gray", orient='vertical')
        pw_main.add(pw_left)
        pw_right = tk.PanedWindow(pw_main, bg="yellow", orient='vertical')
        pw_main.add(pw_right)

        # Frame
        ## bg     : 背景色
        ## bd     : ボーダーの幅(default=0)
        ## relief :　枠の装飾　Tk.FLAT(default), Tk.RAISED, Tk.SUNKENN, Tk.GROOVE, Tk.RIDGE
        ## width  : 幅 [pixel]
        ## height : 高さ [pixel]
        fm_select = tk.Frame(pw_left, bg = 'white', bd=4, relief="ridge")
        pw_left.add(fm_select)

        # ラベル
        ## padx , pady ：外側の横、縦の隙間
        label_fpath = tk.Label(fm_select, text="ファイルパス(入力)", width=20, bg='white')
        ## ラベルを配置
        label_fpath.grid(row=0, column=0, padx=2, pady=2)

        # 1行入力
        ##  justify：文字寄せ（center or left or right）
        ##  sticky：スペースが空いている場合の動き（tk.W + tk.E 縦横に広がる）
        entry_fpath = tk.Entry(fm_select, justify="left", width=50)
        entry_fpath.grid(row=1, column=0, sticky=tk.W + tk.E,padx=2, pady=2)
        ## 削除
        entry_fpath.delete( 0, tk.END ) 
        ## 先頭行に値を設定
        entry_fpath.insert( 0, "input your file path..." ) 
        ## 値を取得
        print('Entryの初期値を出力：{}'.format(entry_fpath.get()))

        # ラベル
        label_fpaths = tk.Label(fm_select, text="ファイルパス(複数)", width=20, bg='white')
        label_fpaths.grid(row=2, column=0, padx=2, pady=2)

        # 複数行入力
        ## witdh ：入力する文字数
        ## wrap：長い行の折り返し方法（tk.CHAR: 文字単位で折り返す or tk.NONE: 折り返ししない or ・・・）
        self.selected_files = tk.Text(fm_select, height=10, width=50, wrap=tk.CHAR)
        self.selected_files.grid(row=3, column=0, padx=2, pady=2,sticky=tk.W + tk.E)

        # ボタン
        ## columnspan ：　何列に渡って配置するか
        ## rowspan ：　何行に渡って配置するか
        btn_select_file = tk.Button(fm_select, text="ファイル選択", command=self.select_file) 
        btn_select_file.grid(row=4, column=0, sticky=tk.W + tk.E, padx=2, pady=2)

        # ボタン
        # ボタンイベントに引数を渡す
        fm_btns = tk.Frame(pw_left, bd=2, relief="ridge")
        fm_btns.pack(expand=False,side="top")
        pw_left.add(fm_btns)
        btn_tool_1 = tk.Button(fm_btns, text="Save", command=lambda:self.btn_ivent("Save"), width=15) 
        btn_tool_1.grid(row=5, column=0, sticky=tk.W + tk.E, padx=2, pady=10)
        btn_tool_2 = tk.Button(fm_btns, text="Show", command=lambda:self.img_click("Image show"), width=15) 
        btn_tool_2.grid(row=5, column=1, sticky=tk.W + tk.E, padx=2, pady=10)

        # 画像表示
        # 画面の右側エリアに画像を表示する
        #fm_img = tk.Frame(pw_right, bd=2, relief="ridge")
        fm_img = tk.Canvas(pw_right, bd=2, relief="ridge")
        pw_right.add(fm_img)
        self.panel_img = tk.Label(fm_img)
        self.panel_img.pack()
        # スクロールバー
        bar_y = ttk.Scrollbar(pw_right, orient=tk.VERTICAL)
        #bar_x = ttk.Scrollbar(pw_right, orient=tk.HORIZONTAL)
        bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        #bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        #スクロールバーの制御をCanvasに通知する処理
        bar_y.config(command=fm_img.yview)
        fm_img.config(yscrollcommand=bar_y.set)

        sc_hgt=int(1000)  #スクロールの縦の範囲　リストの数＋ヘッダー分に
        fm_img.config(scrollregion=(0,0,500,sc_hgt))

        # 画像表示用のウィジェットに以下を追記
        self.panel_img.bind("<Button-1>", self.img_click)


    def select_file(self):
        print('select_file...')
        # 選択可能な拡張子を限定
        fTyp =[("", "*.png")]
        #iDir = os.path.abspath(os.path.dirname("__file__"))
        iDir = '/home/fsato/Dropbox/jupyternote/img'
        tk.messagebox.showinfo('file select','処理ファイルを選択してください！')
        files = tk.filedialog.askopenfilenames(filetypes = fTyp, initialdir = iDir)
        # 選択されたファイルパスを表示
        # 前回分を全行削除
        self.selected_files.delete( '1.0', tk.END ) 
        self.file_list = list(files)
        if(len(self.file_list) <= 10):
            for i in np.arange(0, len(self.file_list)):
                self.selected_files.insert("end", "{}\n".format(self.file_list[i]))
    
    def btn_ivent(self, msg):
        print(msg)

    def img_click(self, msg):
        # 先頭の画像ファイルを表示する
        self.show_image(self.file_list[0])
        print(msg)

    def show_image(self, file_path):
        # w,h = 500, 500
        # image = Image.open(file_path)
        # image = image.resize((w, h), Image.ANTIALIAS)
        self.img = tk.PhotoImage(file=file_path)
        self.panel_img.configure(image=self.img)
        self.panel_img.pack()


# 実行
root = tk.Tk()        
myapp = Application(master=root)
myapp.master.title("My Application") # タイトル
myapp.master.geometry("1000x500") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()
