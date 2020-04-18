import datetime
import calendar
import wx
import wx.lib.scrolledpanel as scrolled
from dateutil.relativedelta import relativedelta

def CreateCalendar(panle : scrolled.ScrolledPanel):
    disp_year = 3
    base_date = datetime.date(2020, 4, 1)
    calendar_size  = {'size_month': (120, 30), 'size_week': (30, 30)}

    layout_calendar = wx.BoxSizer(wx.VERTICAL)
    layout_month    = wx.BoxSizer(wx.HORIZONTAL)
    layout_week     = wx.BoxSizer(wx.HORIZONTAL)

    # Create monthly block
    for i in range(12*disp_year):
        date = base_date + relativedelta(months=i)
        month_button = wx.Button(panle, wx.ID_ANY, '`'+ str(date.year)[2:4] + '/' + str(date.month), size=calendar_size['size_month'])
        layout_month.Add(month_button, 1, wx.ALL | wx.SHAPED, 0)
        # Create weekly block
        for w in range(4):
            monday = GetDayofNthDow(date.year, date.month, w+1, 0)
            week_button = wx.Button(panle, wx.ID_ANY, str(monday), size=calendar_size['size_week'])
            layout_week.Add(week_button, 1, wx.ALL | wx.SHAPED, 0)

    layout_calendar.Add(layout_month)
    layout_calendar.Add(layout_week)
    panle.SetSizer(layout_calendar)

def GetDayofNthDow(year, month, nth, dow):
    # [Pythonで第何何曜日（第2月曜日など）の日付を取得 | note.nkmk.me](https://note.nkmk.me/python-calendar-day-of-nth-dow/)
    '''dow: Monday(0) - Sunday(6)'''
    if nth < 1 or dow < 0 or dow > 6:
        return None
    
    first_dow, n = calendar.monthrange(year, month)
    day = 7 * (nth - 1) + (dow - first_dow) % 7 + 1

    return day if day <= n else None