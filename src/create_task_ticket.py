import wx
import wx.adv
import wx.xrc as xrc
import datetime
import json

class TicketForm(wx.App):
    def __init__(self, width, height, title='TicketForm', redirect=False):
        super().__init__(redirect)
        
        self.data = {
            'created' : "",
            'updated' : "",
            'title' : "No title",
            'assign' : "",
            'description' : "",
            'status' : "New",
            'priority' : "Normal",
            'start' : {'year': 0, 'month': 0, 'day': 0},
            'limit' : {'year': 0, 'month': 0, 'day': 0},
        }

        self.frame = wx.Frame(None, -1, title, size=(width,height))
        panel = wx.Panel(self.frame, -1)

        hbox  = wx.BoxSizer(wx.HORIZONTAL)
        
        # wx.FlexGridSizer(行数, 列数, [各行の間隔], [各列の間隔])
        fgs   = wx.FlexGridSizer(8, 2, 9, 25)

        title    = wx.StaticText(panel, -1, 'Title')
        assign   = wx.StaticText(panel, -1, 'Assign')
        desc     = wx.StaticText(panel, -1, 'Description')
        status   = wx.StaticText(panel, -1, 'Status')
        priority = wx.StaticText(panel, -1, 'Priority')
        space    = wx.StaticText(panel, -1, ' ')
        start    = wx.StaticText(panel, -1, '開始日')
        limit    = wx.StaticText(panel, -1, '期限')

        # element_assign = ('Member 1', 'Member 2', 'Member 3',
        #          'Member 4', 'Member 5')
        # choice_assign = wx.ComboBox(panel, -1, '',
        #                  choices=element_assign, style=wx.CB_SIMPLE)
        self.choice_assign = wx.ComboBox(panel)
        self.choice_assign.Append('Member 1', 'Assign 1')
        self.choice_assign.Append('Member 2', 'Assign 2')
        self.choice_assign.Append('Member 3', 'Assign 3')
        self.choice_assign.Append('Member 4', 'Assign 4')

        self.choice_status = wx.Choice(panel)
        self.choice_status.Append('New', 'Status 1')
        self.choice_status.Append('Open', 'Status 2')
        self.choice_status.Append('Close', 'Status 3')
        self.choice_status.SetSelection(0)

        self.choice_priority = wx.Choice(panel)
        self.choice_priority.Append('High',    'Priority 1')
        self.choice_priority.Append('Normal',  'Priority 2')
        self.choice_priority.Append('Low',     'Priority 3')
        self.choice_priority.Append('Urgent',  'Priority 4')
        self.choice_priority.Append('Put off', 'Priority 5')
        self.choice_priority.SetSelection(1)

        self.text_ctrl_title = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE)
        self.text_ctrl_desc  = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE)

        # Calendar
        self.datepick_start = wx.adv.DatePickerCtrl(panel, wx.adv.DP_DROPDOWN, pos = (100, 30))
        self.datepick_limit = wx.adv.DatePickerCtrl(panel, wx.adv.DP_DROPDOWN, pos = (100, 30))
        # Create button
        ticket_create_button = wx.Button(panel, -1, "Create")
        ticket_create_button.Bind(wx.EVT_BUTTON, self.PushCreateButton)
        
        fgs.AddMany([(title),    (self.text_ctrl_title, 1, wx.EXPAND),
                     (assign),   (self.choice_assign,   1, wx.EXPAND),
                     (desc),     (self.text_ctrl_desc,  1, wx.EXPAND),
                     (status),   (self.choice_status,   1, wx.EXPAND),
                     (priority), (self.choice_priority, 1, wx.EXPAND),
                     (start), (self.datepick_start),
                     (limit), (self.datepick_limit),
                     (space), (ticket_create_button)])

        fgs.AddGrowableRow(2)
        fgs.AddGrowableCol(1)

        hbox.Add(fgs, 1, wx.ALL | wx.EXPAND, 15)
        panel.SetSizer(hbox)

        #self.MessageBox()
        self.frame.Show()

    def PushCreateButton(self, event):
        print("push button") 
        if self.text_ctrl_title.GetValue():
            self.data['title'] = self.text_ctrl_title.GetValue()
        if self.text_ctrl_desc.GetValue():
            self.data['description']= self.text_ctrl_desc.GetValue()
        self.data['assign']   = self.choice_assign.GetValue()
        self.data['status']   = self.choice_status.GetStringSelection()
        self.data['priority'] = self.choice_priority.GetStringSelection()
        start_date = self.Wxdate2Pydate(self.datepick_start.GetValue())
        self.data['start']['year']  = start_date.year
        self.data['start']['month'] = start_date.month 
        self.data['start']['day']   = start_date.day
        limit_date = self.Wxdate2Pydate(self.datepick_limit.GetValue())
        self.data['limit']['year']  = limit_date.year
        self.data['limit']['month'] = limit_date.month 
        self.data['limit']['day']   = limit_date.day

        self.data['created'] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.data['updated'] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        print(self.data)
        self.SaveJsonFormat()
        self.MessageBox()
        self.frame.Close()

    def Wxdate2Pydate(self, date):
        assert isinstance(date, wx.DateTime), 'Please input wx.DateTime format date.'
        if date.IsValid():
            ymd = map(int, date.FormatISODate().split('-'))
            return datetime.date(*ymd)
        else:
            return None 

    def SaveJsonFormat(self):
        with open('../dst/Ticket_test.json', 'w') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    # def Clicked(self,event):
    #     self.text = self.frame.box.GetValue()
    #     self.frame.Close(True)

    def MessageBox(self):
        wx.MessageBox("保存しました。", "Save ticket")
        return True


def main():
    app = TicketForm(640, 480, "New Ticket", False)
    app.MainLoop()


if __name__ == "__main__":
    main()