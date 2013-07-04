# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class RummageFrame
###########################################################################

class RummageFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rummage", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bFrameSizer = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer13 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer13.AddGrowableCol( 0 )
		fgSizer13.AddGrowableRow( 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_grep_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH|wx.NB_NOPAGETHEME )
		self.m_settings_panel = wx.Panel( self.m_grep_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_settings_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_searchin_panel = wx.Panel( self.m_settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_searchin_panel, wx.ID_ANY, u"Search In" ), wx.VERTICAL )
		
		fgSizer121 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer121.AddGrowableCol( 0 )
		fgSizer121.SetFlexibleDirection( wx.BOTH )
		fgSizer121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		m_searchin_textChoices = []
		self.m_searchin_text = wx.ComboBox( self.m_searchin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_searchin_textChoices, wx.TE_PROCESS_ENTER )
		fgSizer121.Add( self.m_searchin_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_searchin_dir_picker = wx.DirPickerCtrl( self.m_searchin_panel, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DIR_MUST_EXIST )
		fgSizer121.Add( self.m_searchin_dir_picker, 0, wx.ALIGN_CENTER|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer1.Add( fgSizer121, 0, wx.EXPAND, 5 )
		
		
		self.m_searchin_panel.SetSizer( sbSizer1 )
		self.m_searchin_panel.Layout()
		sbSizer1.Fit( self.m_searchin_panel )
		fgSizer2.Add( self.m_searchin_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_search_panel = wx.Panel( self.m_settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_search_panel, wx.ID_ANY, u"Search" ), wx.VERTICAL )
		
		fgSizer6 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer6.AddGrowableCol( 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.AddGrowableCol( 1 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_searchfor_label = wx.StaticText( self.m_search_panel, wx.ID_ANY, u"Search for:", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.m_searchfor_label.Wrap( -1 )
		fgSizer8.Add( self.m_searchfor_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_searchfor_textboxChoices = []
		self.m_searchfor_textbox = wx.ComboBox( self.m_search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_searchfor_textboxChoices, wx.TE_PROCESS_ENTER|wx.TAB_TRAVERSAL|wx.WANTS_CHARS )
		fgSizer8.Add( self.m_searchfor_textbox, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer6.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		fgSizer9 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_regex_search_checkbox = wx.CheckBox( self.m_search_panel, wx.ID_ANY, u"Search with regex", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_regex_search_checkbox.SetValue(True) 
		fgSizer9.Add( self.m_regex_search_checkbox, 0, wx.ALL, 5 )
		
		self.m_case_checkbox = wx.CheckBox( self.m_search_panel, wx.ID_ANY, u"Search case-sensitive", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_case_checkbox, 0, wx.ALL, 5 )
		
		self.m_dotmatch_checkbox = wx.CheckBox( self.m_search_panel, wx.ID_ANY, u"Dot matches newline", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_dotmatch_checkbox, 0, wx.ALL, 5 )
		
		self.m_utf8_checkbox = wx.CheckBox( self.m_search_panel, wx.ID_ANY, u"Treat all as UTF-8", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_utf8_checkbox, 0, wx.ALL, 5 )
		
		
		fgSizer6.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer6.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer17 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer17.AddGrowableCol( 1 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_regex_test_button = wx.Button( self.m_search_panel, wx.ID_ANY, u"Test Regex", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_regex_test_button, 0, wx.ALL, 5 )
		
		
		fgSizer17.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_save_search_button = wx.Button( self.m_search_panel, wx.ID_ANY, u"Save Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_save_search_button, 0, wx.ALL, 5 )
		
		self.m_load_search_button = wx.Button( self.m_search_panel, wx.ID_ANY, u"Load Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_load_search_button, 0, wx.ALL, 5 )
		
		
		fgSizer6.Add( fgSizer17, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		
		self.m_search_panel.SetSizer( sbSizer2 )
		self.m_search_panel.Layout()
		sbSizer2.Fit( self.m_search_panel )
		fgSizer2.Add( self.m_search_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_limiter_panel = wx.Panel( self.m_settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_limiter_panel, wx.ID_ANY, u"Limit Search" ), wx.VERTICAL )
		
		fgSizer26 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer26.AddGrowableCol( 2 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_limit_size_panel = wx.Panel( self.m_limiter_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer11 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer12 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_size_is_label = wx.StaticText( self.m_limit_size_panel, wx.ID_ANY, u"Size is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_size_is_label.Wrap( -1 )
		fgSizer12.Add( self.m_size_is_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_logic_choiceChoices = [ u"any", u"greater than", u"equal to", u"less than" ]
		self.m_logic_choice = wx.Choice( self.m_limit_size_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_logic_choiceChoices, 0 )
		self.m_logic_choice.SetSelection( 0 )
		fgSizer12.Add( self.m_logic_choice, 0, wx.ALL, 5 )
		
		self.m_size_text = wx.TextCtrl( self.m_limit_size_panel, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_size_text, 0, wx.ALL, 5 )
		
		self.m_size_type_label = wx.StaticText( self.m_limit_size_panel, wx.ID_ANY, u"KB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_size_type_label.Wrap( -1 )
		fgSizer12.Add( self.m_size_type_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer11.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_subfolder_checkbox = wx.CheckBox( self.m_limit_size_panel, wx.ID_ANY, u"Include subfolders", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_subfolder_checkbox.SetValue(True) 
		gSizer1.Add( self.m_subfolder_checkbox, 0, wx.ALL, 5 )
		
		self.m_hidden_checkbox = wx.CheckBox( self.m_limit_size_panel, wx.ID_ANY, u"Include hidden", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_hidden_checkbox, 0, wx.ALL, 5 )
		
		self.m_binary_checkbox = wx.CheckBox( self.m_limit_size_panel, wx.ID_ANY, u"Include binary files", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_binary_checkbox, 0, wx.ALL, 5 )
		
		
		fgSizer11.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_limit_size_panel.SetSizer( fgSizer11 )
		self.m_limit_size_panel.Layout()
		fgSizer11.Fit( self.m_limit_size_panel )
		fgSizer26.Add( self.m_limit_size_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_limiter_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer26.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_limit_panel = wx.Panel( self.m_limiter_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_filematch_label = wx.StaticText( self.m_limit_panel, wx.ID_ANY, u"Files which match:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_filematch_label.Wrap( -1 )
		fgSizer4.Add( self.m_filematch_label, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		m_filematch_textboxChoices = []
		self.m_filematch_textbox = wx.ComboBox( self.m_limit_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_filematch_textboxChoices, wx.TE_PROCESS_ENTER|wx.TAB_TRAVERSAL|wx.WANTS_CHARS )
		fgSizer4.Add( self.m_filematch_textbox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_fileregex_checkbox = wx.CheckBox( self.m_limit_panel, wx.ID_ANY, u"Regex", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_fileregex_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_exclude_label = wx.StaticText( self.m_limit_panel, wx.ID_ANY, u"Exclude dirs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_exclude_label.Wrap( -1 )
		fgSizer4.Add( self.m_exclude_label, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		m_exclude_textboxChoices = []
		self.m_exclude_textbox = wx.ComboBox( self.m_limit_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_exclude_textboxChoices, wx.TE_PROCESS_ENTER|wx.TAB_TRAVERSAL|wx.WANTS_CHARS )
		fgSizer4.Add( self.m_exclude_textbox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_dirregex_checkbox = wx.CheckBox( self.m_limit_panel, wx.ID_ANY, u"Regex", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_dirregex_checkbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_limit_panel.SetSizer( fgSizer3 )
		self.m_limit_panel.Layout()
		fgSizer3.Fit( self.m_limit_panel )
		fgSizer26.Add( self.m_limit_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sbSizer4.Add( fgSizer26, 1, wx.EXPAND, 5 )
		
		
		self.m_limiter_panel.SetSizer( sbSizer4 )
		self.m_limiter_panel.Layout()
		sbSizer4.Fit( self.m_limiter_panel )
		fgSizer2.Add( self.m_limiter_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_action_panel = wx.Panel( self.m_settings_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bActionSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_search_button = wx.Button( self.m_action_panel, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bActionSizer.Add( self.m_search_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.m_action_panel.SetSizer( bActionSizer )
		self.m_action_panel.Layout()
		bActionSizer.Fit( self.m_action_panel )
		fgSizer2.Add( self.m_action_panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer10.Add( fgSizer2, 0, wx.EXPAND, 5 )
		
		
		self.m_settings_panel.SetSizer( bSizer10 )
		self.m_settings_panel.Layout()
		bSizer10.Fit( self.m_settings_panel )
		self.m_grep_notebook.AddPage( self.m_settings_panel, u"Search", True )
		self.m_result_file_panel = wx.Panel( self.m_grep_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_result_file_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_result_file_list = wx.ListCtrl( self.m_result_file_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VIRTUAL )
		bSizer7.Add( self.m_result_file_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_result_file_panel.SetSizer( bSizer7 )
		self.m_result_file_panel.Layout()
		bSizer7.Fit( self.m_result_file_panel )
		self.m_grep_notebook.AddPage( self.m_result_file_panel, u"Files", False )
		self.m_result_content_panel = wx.Panel( self.m_grep_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_result_content_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_result_list = wx.ListCtrl( self.m_result_content_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VIRTUAL )
		bSizer6.Add( self.m_result_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_result_content_panel.SetSizer( bSizer6 )
		self.m_result_content_panel.Layout()
		bSizer6.Fit( self.m_result_content_panel )
		self.m_grep_notebook.AddPage( self.m_result_content_panel, u"Content", False )
		
		fgSizer13.Add( self.m_grep_notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_progressbar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,2 ), wx.GA_HORIZONTAL )
		fgSizer13.Add( self.m_progressbar, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		bFrameSizer.Add( fgSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bFrameSizer )
		self.Layout()
		bFrameSizer.Fit( self )
		self.m_statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menu = wx.MenuBar( 0 )
		self.m_file_menu = wx.Menu()
		self.m_preferences = wx.MenuItem( self.m_file_menu, wx.ID_PREFERENCES, u"&Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file_menu.AppendItem( self.m_preferences )
		
		self.m_menu.Append( self.m_file_menu, u"File" ) 
		
		self.SetMenuBar( self.m_menu )
		
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.m_searchin_text.Bind( wx.EVT_COMBOBOX, self.m_searchin_selected )
		self.m_searchin_text.Bind( wx.EVT_TEXT, self.m_searchin_changed )
		self.m_searchin_text.Bind( wx.EVT_TEXT_ENTER, self.m_searchin_enter )
		self.m_searchin_dir_picker.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_dir_changed )
		self.m_regex_search_checkbox.Bind( wx.EVT_CHECKBOX, self.on_regex_search_toggle )
		self.m_regex_test_button.Bind( wx.EVT_BUTTON, self.on_test_regex )
		self.m_save_search_button.Bind( wx.EVT_BUTTON, self.on_save_search )
		self.m_load_search_button.Bind( wx.EVT_BUTTON, self.on_load_search )
		self.m_fileregex_checkbox.Bind( wx.EVT_CHECKBOX, self.on_fileregex_toggle )
		self.m_dirregex_checkbox.Bind( wx.EVT_CHECKBOX, self.on_dirregex_toggle )
		self.m_search_button.Bind( wx.EVT_BUTTON, self.on_search_click )
		self.Bind( wx.EVT_MENU, self.on_preferences, id = self.m_preferences.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()
	
	def m_searchin_selected( self, event ):
		event.Skip()
	
	def m_searchin_changed( self, event ):
		event.Skip()
	
	def m_searchin_enter( self, event ):
		event.Skip()
	
	def on_dir_changed( self, event ):
		event.Skip()
	
	def on_regex_search_toggle( self, event ):
		event.Skip()
	
	def on_test_regex( self, event ):
		event.Skip()
	
	def on_save_search( self, event ):
		event.Skip()
	
	def on_load_search( self, event ):
		event.Skip()
	
	def on_fileregex_toggle( self, event ):
		event.Skip()
	
	def on_dirregex_toggle( self, event ):
		event.Skip()
	
	def on_search_click( self, event ):
		event.Skip()
	
	def on_preferences( self, event ):
		event.Skip()
	

###########################################################################
## Class LoadSearchDialog
###########################################################################

class LoadSearchDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Searches", pos = wx.DefaultPosition, size = wx.Size( 470,288 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_load_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_load_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer36 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer36.AddGrowableCol( 0 )
		fgSizer36.AddGrowableRow( 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_search_list = wx.ListCtrl( self.m_load_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		fgSizer36.Add( self.m_search_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer37 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer37.AddGrowableCol( 0 )
		fgSizer37.AddGrowableCol( 4 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer37.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_delete_button = wx.Button( self.m_load_panel, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_delete_button, 0, wx.ALL, 5 )
		
		self.m_load_button = wx.Button( self.m_load_panel, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_load_button, 0, wx.ALL, 5 )
		
		self.m_cancel_button = wx.Button( self.m_load_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_cancel_button, 0, wx.ALL, 5 )
		
		
		fgSizer37.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer36.Add( fgSizer37, 1, wx.EXPAND, 5 )
		
		
		self.m_load_panel.SetSizer( fgSizer36 )
		self.m_load_panel.Layout()
		fgSizer36.Fit( self.m_load_panel )
		bSizer13.Add( self.m_load_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer13 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_delete_button.Bind( wx.EVT_BUTTON, self.on_delete )
		self.m_load_button.Bind( wx.EVT_BUTTON, self.on_load )
		self.m_cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_delete( self, event ):
		event.Skip()
	
	def on_load( self, event ):
		event.Skip()
	
	def on_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class SettingsDialog
###########################################################################

class SettingsDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Preferences", pos = wx.DefaultPosition, size = wx.Size( 350,186 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_settings_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer17 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer17.AddGrowableCol( 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_settings_panel, wx.ID_ANY, u"Editor" ), wx.VERTICAL )
		
		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.AddGrowableCol( 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_editor_text = wx.TextCtrl( self.m_settings_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer13.Add( self.m_editor_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_editor_button = wx.Button( self.m_settings_panel, wx.ID_ANY, u"Change", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_editor_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer7.Add( fgSizer13, 1, wx.EXPAND, 5 )
		
		
		fgSizer17.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_settings_panel, wx.ID_ANY, u"Toggles" ), wx.VERTICAL )
		
		self.m_single_checkbox = wx.CheckBox( self.m_settings_panel, wx.ID_ANY, u"Single Instance", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_single_checkbox, 0, wx.ALL, 5 )
		
		
		fgSizer17.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.AddGrowableCol( 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer22.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_close_button = wx.Button( self.m_settings_panel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.m_close_button, 0, wx.ALL, 5 )
		
		
		fgSizer17.Add( fgSizer22, 1, wx.EXPAND, 5 )
		
		
		self.m_settings_panel.SetSizer( fgSizer17 )
		self.m_settings_panel.Layout()
		fgSizer17.Fit( self.m_settings_panel )
		bSizer7.Add( self.m_settings_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_editor_button.Bind( wx.EVT_BUTTON, self.on_editor_change )
		self.m_single_checkbox.Bind( wx.EVT_CHECKBOX, self.on_single_toggle )
		self.m_close_button.Bind( wx.EVT_BUTTON, self.on_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_editor_change( self, event ):
		event.Skip()
	
	def on_single_toggle( self, event ):
		event.Skip()
	
	def on_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class EditorDialog
###########################################################################

class EditorDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configure Editor", pos = wx.DefaultPosition, size = wx.Size( 350,450 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_editor_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_editor_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer14 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer14.AddGrowableCol( 0 )
		fgSizer14.AddGrowableRow( 2 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_instructions_label = wx.StaticText( self.m_editor_panel, wx.ID_ANY, u"Select the application and then set the arguments.\n\nUse {$file}, {$line}, and {$col} syntax to specify the\nfile, line, and column respectively.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_instructions_label.Wrap( -1 )
		fgSizer14.Add( self.m_instructions_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_editor_panel, wx.ID_ANY, u"Application" ), wx.VERTICAL )
		
		self.m_editor_picker = wx.FilePickerCtrl( self.m_editor_panel, wx.ID_ANY, wx.EmptyString, u"Select Editor", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer6.Add( self.m_editor_picker, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer14.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_editor_panel, wx.ID_ANY, u"Arguments" ), wx.VERTICAL )
		
		fgSizer15 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer15.AddGrowableCol( 0 )
		fgSizer15.AddGrowableRow( 1 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_arg_text = wx.TextCtrl( self.m_editor_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer15.Add( self.m_arg_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_add_arg_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_add_arg_button, 0, wx.ALL, 5 )
		
		m_arg_listChoices = []
		self.m_arg_list = wx.ListBox( self.m_editor_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_arg_listChoices, wx.LB_SINGLE )
		fgSizer15.Add( self.m_arg_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer23 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_remove_arg_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Del", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_remove_arg_button, 0, wx.ALL, 5 )
		
		self.m_edit_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_edit_button, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_editor_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer23.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_upp_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_upp_button, 0, wx.ALL, 5 )
		
		self.m_down_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_down_button, 0, wx.ALL, 5 )
		
		
		fgSizer15.Add( fgSizer23, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( fgSizer15, 1, wx.EXPAND, 5 )
		
		
		fgSizer14.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.AddGrowableCol( 3 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_apply_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_apply_button, 0, wx.ALL, 5 )
		
		self.m_cancel_button = wx.Button( self.m_editor_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_cancel_button, 0, wx.ALL, 5 )
		
		
		fgSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer14.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		
		self.m_editor_panel.SetSizer( fgSizer14 )
		self.m_editor_panel.Layout()
		fgSizer14.Fit( self.m_editor_panel )
		bSizer6.Add( self.m_editor_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_arg_text.Bind( wx.EVT_TEXT_ENTER, self.on_arg_enter )
		self.m_add_arg_button.Bind( wx.EVT_BUTTON, self.on_add )
		self.m_remove_arg_button.Bind( wx.EVT_BUTTON, self.on_remove )
		self.m_edit_button.Bind( wx.EVT_BUTTON, self.on_edit )
		self.m_upp_button.Bind( wx.EVT_BUTTON, self.on_up )
		self.m_down_button.Bind( wx.EVT_BUTTON, self.on_down )
		self.m_apply_button.Bind( wx.EVT_BUTTON, self.on_apply )
		self.m_cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_arg_enter( self, event ):
		event.Skip()
	
	def on_add( self, event ):
		event.Skip()
	
	def on_remove( self, event ):
		event.Skip()
	
	def on_edit( self, event ):
		event.Skip()
	
	def on_up( self, event ):
		event.Skip()
	
	def on_down( self, event ):
		event.Skip()
	
	def on_apply( self, event ):
		event.Skip()
	
	def on_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class RegexTestDialog
###########################################################################

class RegexTestDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Regex Tester", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_tester_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_tester_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer18 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer18.AddGrowableCol( 0 )
		fgSizer18.AddGrowableRow( 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_tester_panel, wx.ID_ANY, u"Test Text" ), wx.VERTICAL )
		
		self.m_test_text = wx.TextCtrl( self.m_tester_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH )
		sbSizer8.Add( self.m_test_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer18.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_tester_panel, wx.ID_ANY, u"Regex Input" ), wx.VERTICAL )
		
		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_case_checkbox = wx.CheckBox( self.m_tester_panel, wx.ID_ANY, u"Search case-sensitive", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_case_checkbox, 0, wx.ALL, 5 )
		
		self.m_dot_checkbox = wx.CheckBox( self.m_tester_panel, wx.ID_ANY, u"Dot matches newline", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_dot_checkbox, 0, wx.ALL, 5 )
		
		
		sbSizer9.Add( fgSizer19, 1, wx.EXPAND, 5 )
		
		self.m_regex_text = wx.TextCtrl( self.m_tester_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_regex_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer18.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		fgSizer20 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer20.AddGrowableCol( 0 )
		fgSizer20.AddGrowableCol( 3 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer20.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_use_regex_button = wx.Button( self.m_tester_panel, wx.ID_ANY, u"Use", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_use_regex_button, 0, wx.ALL, 5 )
		
		self.m_close_button = wx.Button( self.m_tester_panel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_close_button, 0, wx.ALL, 5 )
		
		
		fgSizer20.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer18.Add( fgSizer20, 1, wx.EXPAND, 5 )
		
		
		self.m_tester_panel.SetSizer( fgSizer18 )
		self.m_tester_panel.Layout()
		fgSizer18.Fit( self.m_tester_panel )
		bSizer8.Add( self.m_tester_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.Bind( wx.EVT_SIZE, self.on_size )
		self.m_test_text.Bind( wx.EVT_TEXT, self.on_test_changed )
		self.m_case_checkbox.Bind( wx.EVT_CHECKBOX, self.on_case_toggle )
		self.m_dot_checkbox.Bind( wx.EVT_CHECKBOX, self.on_dot_toggle )
		self.m_regex_text.Bind( wx.EVT_TEXT, self.on_regex_changed )
		self.m_use_regex_button.Bind( wx.EVT_BUTTON, self.on_use )
		self.m_close_button.Bind( wx.EVT_BUTTON, self.on_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()
	
	def on_size( self, event ):
		event.Skip()
	
	def on_test_changed( self, event ):
		event.Skip()
	
	def on_case_toggle( self, event ):
		event.Skip()
	
	def on_dot_toggle( self, event ):
		event.Skip()
	
	def on_regex_changed( self, event ):
		event.Skip()
	
	def on_use( self, event ):
		event.Skip()
	
	def on_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ArgDialog
###########################################################################

class ArgDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Argument", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_arg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_arg_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer24 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_arg_text = wx.TextCtrl( self.m_arg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.m_arg_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer25 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer25.AddGrowableCol( 0 )
		fgSizer25.AddGrowableCol( 3 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_apply_button = wx.Button( self.m_arg_panel, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.m_apply_button, 0, wx.ALL, 5 )
		
		self.m_cancel_button = wx.Button( self.m_arg_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.m_cancel_button, 0, wx.ALL, 5 )
		
		
		fgSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer24.Add( fgSizer25, 1, wx.EXPAND, 5 )
		
		
		self.m_arg_panel.SetSizer( fgSizer24 )
		self.m_arg_panel.Layout()
		fgSizer24.Fit( self.m_arg_panel )
		bSizer9.Add( self.m_arg_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		bSizer9.Fit( self )
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_apply_button.Bind( wx.EVT_BUTTON, self.on_apply )
		self.m_cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_apply( self, event ):
		event.Skip()
	
	def on_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class SaveSearchDialog
###########################################################################

class SaveSearchDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Search Name", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_save_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_save_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer24 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer34 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer34.AddGrowableCol( 1 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_name_label = wx.StaticText( self.m_save_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_name_label.Wrap( -1 )
		fgSizer34.Add( self.m_name_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_name_text = wx.TextCtrl( self.m_save_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer34.Add( self.m_name_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer24.Add( fgSizer34, 1, wx.EXPAND, 5 )
		
		fgSizer25 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer25.AddGrowableCol( 0 )
		fgSizer25.AddGrowableCol( 3 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_apply_button = wx.Button( self.m_save_panel, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.m_apply_button, 0, wx.ALL, 5 )
		
		self.m_cancel_button = wx.Button( self.m_save_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer25.Add( self.m_cancel_button, 0, wx.ALL, 5 )
		
		
		fgSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer24.Add( fgSizer25, 1, wx.EXPAND, 5 )
		
		
		self.m_save_panel.SetSizer( fgSizer24 )
		self.m_save_panel.Layout()
		fgSizer24.Fit( self.m_save_panel )
		bSizer9.Add( self.m_save_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		bSizer9.Fit( self )
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_apply_button.Bind( wx.EVT_BUTTON, self.on_apply )
		self.m_cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_apply( self, event ):
		event.Skip()
	
	def on_cancel( self, event ):
		event.Skip()
	