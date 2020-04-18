import datetime
import calendar
import wx
import wx.lib.scrolledpanel as scrolled
from dateutil.relativedelta import relativedelta

class GanttChart(wx.App):
   def __init__(self, width, height, title='ChanttChart', redirect=False):
      super().__init__(redirect)

      self.frame = wx.Frame(None, -1, title, size=(width,height))
      self.InitMenu()

      self.panel1 = scrolled.ScrolledPanel(self.frame, wx.ID_ANY, size=(500,400))
      self.panel1.SetBackgroundColour('snow')
      self.panel2 = scrolled.ScrolledPanel(self.frame, wx.ID_ANY)
      self.panel2.SetupScrolling()

      # カレンダーの表示
      self.CreateCalendar()

      # Task一覧の表示
      

      hbox  = wx.BoxSizer(wx.HORIZONTAL)
      hbox.Add(self.panel1,  1, wx.ALL | wx.GROW, border=1)
      hbox.Add(self.panel2, 20, wx.ALL | wx.GROW, border=1)
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

   def CreateCalendar(self):
      disp_year = 3
      base_date = datetime.date(2020, 4, 1)
      calendar_size  = {'size_month': (120, 30), 'size_week': (30, 30)}

      layout_calendar = wx.BoxSizer(wx.VERTICAL)
      layout_month    = wx.BoxSizer(wx.HORIZONTAL)
      layout_week     = wx.BoxSizer(wx.HORIZONTAL)

      # Create monthly block
      for i in range(12*disp_year):
         date = base_date + relativedelta(months=i)
         month_button = wx.Button(self.panel2, wx.ID_ANY, '`'+ str(date.year)[2:4] + '/' + str(date.month), size=calendar_size['size_month'])
         layout_month.Add(month_button, 1, wx.ALL | wx.SHAPED, 0)
         # Create weekly block
         for w in range(4):
            monday = self.GetDayofNthDow(date.year, date.month, w+1, 0)
            week_button = wx.Button(self.panel2, wx.ID_ANY, str(monday), size=calendar_size['size_week'])
            layout_week.Add(week_button, 1, wx.ALL | wx.SHAPED, 0)

      layout_calendar.Add(layout_month)
      layout_calendar.Add(layout_week)
      self.panel2.SetSizer(layout_calendar)

   def GetDayofNthDow(self, year, month, nth, dow):
      # [Pythonで第何何曜日（第2月曜日など）の日付を取得 | note.nkmk.me](https://note.nkmk.me/python-calendar-day-of-nth-dow/)
      '''dow: Monday(0) - Sunday(6)'''
      if nth < 1 or dow < 0 or dow > 6:
         return None
      
      first_dow, n = calendar.monthrange(year, month)
      day = 7 * (nth - 1) + (dow - first_dow) % 7 + 1

      return day if day <= n else None


def main():
    app = GanttChart(1200, 480, "New gantt", False)
    app.MainLoop()

if __name__ == "__main__":
    main()