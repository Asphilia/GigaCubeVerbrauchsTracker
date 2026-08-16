##################################################
#                                                #
# GigaCube Verbrauchs Tracker User Interface     #
#                                                #
# Verarbeitet und Visualisiert die Daten aus     #
# dem Backend                                    #
#                                                #
# Letztes Update: 16.08.2026                     #
# Autoren: Asphilia                              #
##################################################

# IMPORTE
# ui system
import customtkinter as ctk
# UI Elemente
from ui_graph import GCVT_GraphFrame
# GCVT Data
from data import GCVT_Data

class GCVT_Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GigaCube Verbrauchs Tracker")
        self.gcvt_data = GCVT_Data()
        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(row=0, column=0, padx=20, pady=20)
        self.graphtab = self.tabs.add('Visualisierung')
        self.graphframe = GCVT_GraphFrame(self.graphtab, self.gcvt_data)
        self.graphframe.grid(row=0, column=0, sticky='news')
        self.bar = ctk.CTkProgressBar(self)
        self.bar.grid(row=1, column=0, sticky='we')
        self.bar.set(self.gcvt_data.percentage_used)




app = GCVT_Main()
app.mainloop()
