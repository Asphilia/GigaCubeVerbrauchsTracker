##################################################
#                                                #
# GigaCube Verbrauchs Tracker UI Graph           #
#                                                #
# Der Visualisierungsbildschirm                  #
#                                                #
# Letztes Update: 16.08.2026                     #
# Autoren: Asphilia                              #
##################################################

# IMPORTS
# ctk
import customtkinter as ctk
# Graph
import matplotlib.figure as figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# CLASSES
class GCVT_GraphFrame(ctk.CTkFrame):
    def __init__(self, master, gcvt_data):
        super().__init__(master=master)
        self.gcvt_data = gcvt_data
        # 3 Buttons: Monat zurück, Monat vor, Neu laden
        self.button_back = ctk.CTkButton(self, text='Monat zurück', command=self.month_back)
        self.button_back.grid(column=0, row=0, padx=20, pady=20, sticky='w')
        self.button_up = ctk.CTkButton(self, text='Monat vor', command=self.month_up)
        self.button_up.grid(column=4, row=0, padx=20, pady=20, sticky="e")
        self.button_refresh = ctk.CTkButton(self, text='Neu Laden', command=self.refresh)
        self.button_refresh.grid(column=2, row=0, padx=20, pady=20)
        self.fig = figure.Figure((15,10,'in'))
        self.ax1 = self.fig.add_subplot(2,1,1)
        self.ax2 = self.fig.add_subplot(2,1,2)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0, row=1, columnspan=5, sticky='nsew')
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.grid(column=0, row=2, columnspan=5, sticky='news')

    def plot(self):
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.plot(self.gcvt_data.data['datum'], self.gcvt_data.data['verbrauch'], label="Gesamt Verbrauch in GB")
        self.ax2.plot(self.gcvt_data.data['datum'], self.gcvt_data.data['acc_mean'], label='Tages Verbrauch an GB/Tag (Durchschnitt)')
        self.ax2.plot(self.gcvt_data.data['datum'], self.gcvt_data.data['recommended_daily_usage'], label='Täglicher Tagesverbrauch für restliche GB in GB/Tag')
        self.ax1.legend()
        self.ax2.legend()
        self.canvas.draw()

    def month_back(self):
        self.gcvt_data.set_ago(-1)
        self.plot()

    def month_up(self):
        self.gcvt_data.set_ago(1)
        self.plot()

    def refresh(self):
        self.plot()

if __name__ == "__main__":
    from data import GCVT_Data
    gcvt_master = GCVT_Data()
    root = ctk.CTk()
    root.title("Dynamic Scatterplot")
    gcvt_graph = GCVT_GraphFrame(master=root, gcvt_data=gcvt_master)
    gcvt_graph.grid(row=0, column=0, sticky="snew")
    root.mainloop()