import wx
import wx.grid as gridlib
import wx.lib.scrolledpanel as scrolled
from wx.lib.splitter import MultiSplitterWindow
import wx.lib.mixins.listctrl as listmix
import create_calendar

class TaskList(wx.ListCtrl, listmix.TextEditMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LC_REPORT):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.LsitItemActivated)

        listmix.TextEditMixin.__init__(self)

        # カラム
        self.InsertColumn(0, "#",           wx.LIST_FORMAT_CENTRE, wx.LIST_AUTOSIZE_USEHEADER)
        self.InsertColumn(1, "Task",        wx.LIST_FORMAT_CENTRE, 150)
        self.InsertColumn(2, "Assign",      wx.LIST_FORMAT_CENTRE, 100)
        self.InsertColumn(3, "Priority",    wx.LIST_FORMAT_CENTRE, 100)
        self.InsertColumn(4, "Status",      wx.LIST_FORMAT_CENTRE, 100)
        self.InsertColumn(5, "Description", wx.LIST_FORMAT_CENTRE, 100)

        # ListCtrlにアイテムを追加
        for x in range(40):
            self.InsertItem(x, '%s' % x)
            self.SetItem(x, 1, 'Task%s' % x)
            self.SetItem(x, 2, 'Member%s' % x)
            self.SetItem(x, 3, str((x + 1) * 5))
            self.SetItem(x, 4, str((x + 3) * 5))
            self.SetItem(x, 5, str((x + 5) * 5))
    
    # Item編集後に呼び出されるcallback
    def LsitItemActivated(self, evt):
        row = evt.GetIndex()
        print(self.GetItem(row, 1).GetText())
        print(self.GetItem(row, 2).GetText())
        print(self.GetItem(row, 3).GetText())


class LeftPanel(scrolled.ScrolledPanel):
    """Task list"""
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent=parent)
        self.SetupScrolling()

        self.list = TaskList(self, 0, style=wx.LC_REPORT|wx.LC_HRULES, size = self.Size)

        button = wx.Button(self, -1, "Create")

        layout = wx.GridSizer(rows=1, cols=1, gap=(0, 0))
        layout.Add(self.list, flag=wx.EXPAND | wx.TOP,   border=35)
        self.SetSizer(layout)


class RightPanel(scrolled.ScrolledPanel):
    """Task schedule"""
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent=parent)
        self.SetupScrolling()
        self.SetBackgroundColour('snow')

        create_calendar.CreateCalendar(self)
        

class GanttChart(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='ChanttChart', size = (1200, 480))

        self.InitMenu()
 
        splitter = wx.SplitterWindow(self, style = wx.SP_LIVE_UPDATE)
        leftP = LeftPanel(splitter)
        rightP = RightPanel(splitter)
        
        # split the window
        splitter.SplitVertically(leftP, rightP, 400,)
        splitter.SetMinimumPaneSize(200)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def InitMenu(self):
        # Menubar
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        f_item1 = fileMenu.Append(wx.ID_ANY,'&New(N)', 'Create new task')
        f_item3 = fileMenu.Append(wx.ID_ANY,'&Quit(Q)', 'Quit application')
        menubar.Append(fileMenu, '&File(F)')
        self.SetMenuBar(menubar)
        # Event call definition
        self.Bind(wx.EVT_MENU, self.Quit, f_item3)
        # Frame definition
        self.Centre()
        # Status bar
        self.CreateStatusBar()
        self.SetStatusText("...")

    def Quit(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App(False)
    root_frame = GanttChart()
    root_frame.Show()
    app.MainLoop()