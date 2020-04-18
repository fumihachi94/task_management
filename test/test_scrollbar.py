import tkinter
import tkinter.ttk
 
root = tkinter.Tk()
root.title('ブログ検索順位取得ツール') #タイトル
root.geometry('500x200') #サイズ
 
#表用のリスト（あとでExcel読み込みに対応させる）
list_keyword = ['理系夫婦','BabyKumon 効果','Python GIF','fortran 配列','python google','BabyKumon 絵本','VBA 入門 ユーザーフォーム']
list_rank = [4,5,8,7,10,12,35]
list_title = ['xxxxxx','yyyyyy','zzzzzz','ssss','dddd','ffff','gggg']
 
num_list = len(list_keyword) #リストの数
 
#Canvas widgetを生成
canvas = tkinter.Canvas(root,width=480,height=150,bg='white') #背景を白に
canvas.grid(row=1,rowspan=num_list,column=0,columnspan=5)     #7行x5列分
 
#スクロールバー
vbar=tkinter.ttk.Scrollbar(root,orient=tkinter.VERTICAL) #縦方向
vbar.grid(row=1,rowspan=7,column=5,sticky='ns')          #7行分の長さで設置
 
#スクロールバーの制御をCanvasに通知する処理
vbar.config(command=canvas.yview)
 
#Canvasの可動域をスクロールバーに通知する処理
canvas.config(yscrollcommand=vbar.set)

#スクロール可動域＜＝これがないと、どこまでもスクロールされてしまう。
sc_hgt=int(150/6*(num_list+1))  #スクロールの縦の範囲　リストの数＋ヘッダー分に
canvas.config(scrollregion=(0,0,500,sc_hgt))
 
#Frameを作成
frame = tkinter.Frame(canvas,bg='white') #背景を白に
 
#frameをcanvasに配置
canvas.create_window((0,0),window=frame,anchor=tkinter.NW,width=canvas.cget('width'))   #anchor&lt;=NWで左上に寄せる
 
#header row=1に設定する文字列 余白は0に
e0=tkinter.Label(frame,width=5,text='select',background='white')
e0.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0) #0列目
 
e1=tkinter.Label(frame,width=25,text='keyword',background='white')
e1.grid(row=1,column=1,padx=0,pady=0,ipadx=0,ipady=0) #1列目
 
e2=tkinter.Label(frame,width=5,text='rank',background='white')
e2.grid(row=1,column=2,padx=0,pady=0,ipadx=0,ipady=0) #2列目
 
e3=tkinter.Label(frame,width=30,text='title',background='white')
e3.grid(row=1,column=3,padx=0,pady=0,ipadx=0,ipady=0) #3列目
 
irow = 2
irow0=2
erow=num_list+irow0

	
#ウィンドウを動かす
root.mainloop()