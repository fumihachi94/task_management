import datetime
import calendar
import wx
import wx.lib.scrolledpanel as scrolled
from dateutil.relativedelta import relativedelta
from create_calendar import  CreateCalendar

class GanttChart(wx.App):
   def __init__(self, width, height, title='ChanttChart', redirect=False):
      super().__init__(redirect)

      self.frame = wx.Frame(None, -1, title, size=(width,height))
      self.InitMenu()

      self.base_panel1 = scrolled.ScrolledPanel(self.frame, wx.ID_ANY, size=(500,400))
      self.base_panel1.SetBackgroundColour('snow')
      self.base_panel2 = scrolled.ScrolledPanel(self.frame, wx.ID_ANY)
      self.base_panel2.SetupScrolling()

      # カレンダーの表示
      CreateCalendar(self.base_panel2)

      # Task一覧の表示


      hbox  = wx.BoxSizer(wx.HORIZONTAL)
      hbox.Add(self.base_panel1,  1, wx.ALL | wx.GROW, border=1)
      hbox.Add(self.base_panel2, 20, wx.ALL | wx.GROW, border=1)
      self.frame.SetSizer(hbox)

      self.frame.Show()

   def CreatePanelWindow(self):
      print("craeet panel")

   def InitMenu(self):
      # Menubar
      menubar = wx.MenuBar()
      fileMenu = wx.Menu()
      f_item3 = fileMenu.Append(wx.ID_ANY, '&Quit(Q)', 'Quit application')
      menubar.Append(fileMenu, '&File(F)')

      self.frame.SetMenuBar(menubar)

      # Event call definition
      self.frame.Bind(wx.EVT_MENU, self.Quit, f_item3)

      # Frame definition
      self.frame.Centre()

      # Status bar
      self.frame.CreateStatusBar()
      self.frame.SetStatusText("Please drop/load a image file.")

   def Quit(self, event):
      self.frame.Close()


def main():
    app = GanttChart(1200, 480, "New gantt", False)
    app.MainLoop()

if __name__ == "__main__":
    main()