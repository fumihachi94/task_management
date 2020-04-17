import wx


class TicketDefault():
    def __init__(self):
        self.title = "No title"
        self.description = ""

class TicketForm(wx.App):
    def __init__(self, width, height, title='TicketForm', redirect=False):
        super().__init__(redirect)
        
        self.input = TicketDefault()
        self.input.title = "No title"
        self.input.description = ""

        self.frame = wx.Frame(None, -1, title, size=(width,height))
        panel = wx.Panel(self.frame, -1)

        hbox  = wx.BoxSizer(wx.HORIZONTAL)
        
        # wx.FlexGridSizer(行数, 列数, [各行の間隔], [各列の間隔])
        fgs   = wx.FlexGridSizer(6, 2, 9, 25)

        title  = wx.StaticText(panel, -1, 'Title')
        assign = wx.StaticText(panel, -1, 'Assign')
        desc   = wx.StaticText(panel, -1, 'Description')
        status = wx.StaticText(panel, -1, 'Status')
        priority = wx.StaticText(panel, -1, 'Priority')
        space = wx.StaticText(panel, -1, ' ')

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

        self.choice_priority = wx.Choice(panel)
        self.choice_priority.Append('High',    'Priority 1')
        self.choice_priority.Append('Medium',  'Priority 2')
        self.choice_priority.Append('Low',     'Priority 3')
        self.choice_priority.Append('Urgent',  'Priority 4')
        self.choice_priority.Append('Put off', 'Priority 5')

        self.text_ctrl_title = wx.TextCtrl(panel, -1)
        self.text_ctrl_desc  = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE)

        # Create button
        ticket_create_button = wx.Button(panel, -1, "Create")
        ticket_create_button.Bind(wx.EVT_BUTTON, self.PushCreateButton)

        fgs.AddMany([(title),    (self.text_ctrl_title, 1, wx.EXPAND),
                     (assign),   (self.choice_assign,   1, wx.EXPAND),
                     (desc),     (self.text_ctrl_desc,  1, wx.EXPAND),
                     (status),   (self.choice_status,   1, wx.EXPAND),
                     (priority), (self.choice_priority, 1, wx.EXPAND),
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
            self.input.title = self.text_ctrl_title.GetValue()
        if self.text_ctrl_desc.GetValue():
            self.input.description = self.text_ctrl_desc.GetValue()
        print(self.input.title)
        print(self.input.description)

    def Clicked(self,event):
        self.text = self.frame.box.GetValue()
        self.frame.Close(True)

    def MessageBox(self):
        wx.MessageBox("Hello wxPython", "wxApp")
        return True


def main():
    app = TicketForm(640, 480, "New Ticket", False)
    app.MainLoop()
    #TicketForm()


if __name__ == "__main__":
    main()