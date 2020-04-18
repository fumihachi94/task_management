import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Title", size=(300,300))
        self.InitializeComponents()

    def InitializeComponents(self):
        mainPanel = wx.Panel(self)
        button1 = wx.Button(mainPanel, -1, "Button 1")
        button2 = wx.Button(mainPanel, -1, "Button 2")
        button3 = wx.Button(mainPanel, -1, "Button 3")
        button4 = wx.Button(mainPanel, -1, "Button 4")
        button5 = wx.Button(mainPanel, -1, "Button 5")
        button6 = wx.TextCtrl(mainPanel, -1, style=wx.TE_MULTILINE)

        # Create a sizer.
        sizer = wx.GridBagSizer(0,0)
        sizer.Add(button1, (0,0), (1,1), flag=wx.EXPAND, border = 5)
        sizer.Add(button2, (0,1), (1,1), flag=wx.EXPAND, border = 5)
        sizer.Add(button3, (1,0), (1,1), flag=wx.EXPAND, border = 5)
        sizer.Add(button4, (1,1), (1,1), flag=wx.EXPAND, border = 5)
        sizer.Add(button5, (0,2), (2,1), flag=wx.EXPAND, border = 5)
        sizer.Add(button6, (2,0), (1,3), flag=wx.EXPAND, border = 5)
        sizer.AddGrowableRow(0)
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)
        mainPanel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    MyFrame().Show(True)
    app.MainLoop()