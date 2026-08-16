##################################################
#                                                #
# GigaCube Verbrauchs Tracker Data               #
#                                                #
# Übernimmt Analyse und Prognose anhand der      #
# Daten                                          #
#                                                #
# Letztes Update: 16.08.2026                     #
# Autoren: Asphilia                              #
##################################################

# IMPORTE
# Datenmanipulation
import pandas as pd
# Eistellungen
from settings import GCVT_Settings
# Pfade finden
import os
# Berechnungen mit Zeiten
import datetime as dt
from dateutil.relativedelta import relativedelta

# CLASSES
class GCVT_Data:
    def __init__(self):
        self.settings = GCVT_Settings()
        self.data = pd.DataFrame()
        self.ago = 0
        self.load_data_files()
        self.load_data()

    def load_data_files(self):
        data_dir = self.settings.get_saving_directory()
        all_data_files = os.listdir(data_dir)
        self.data_files = {}
        today = dt.date.today()
        for file in all_data_files:
            if 'gcvt-data' in file and file.endswith('.csv'):
                month_ago = dt.datetime.strptime(file.split('-')[-1].rstrip('.csv'), '%d.%m.%Y').date()
                if today < month_ago:
                    self.data_files[0] = data_dir + "/" + file
                else:
                    months = (today.year - month_ago.year)*12 + (today.month - month_ago.month)
                    if today.day < month_ago.day:
                        months -= 1
                    self.data_files[months+1] = data_dir + "/" + file
        return

    def load_data(self):
        self.data = pd.read_csv(self.data_files[self.ago], header=0)
        self.data['datum'] = pd.to_datetime(self.data['timestamp'], unit='s')
        self.analyse()

    def set_ago(self, delta_ago:int):
        self.ago += delta_ago
        self.load_data()

    def analyse(self):
        date_range = self.data_files[self.ago].split('gcvt-data-')[-1].rstrip('.csv')
        date_end = dt.datetime.strptime(date_range.split('-')[-1], '%d.%m.%Y').date() + dt.timedelta(days=1)
        date_start = date_end - relativedelta(months=1)
        days_between = (date_end-date_start).days
        days_range = (self.data['datum'] - pd.Timestamp(date_start)).dt.days
        self.data['acc_mean'] = self.data['verbrauch'] / days_range
        self.monthly_mean_until_now = self.data['acc_mean'].mean()
        days_until_end = (pd.Timestamp(date_end) - self.data['datum']).dt.days
        self.data['remaining'] = self.data['volumen'] - self.data['verbrauch']
        self.data['recommended_daily_usage'] = self.data['remaining'] / days_until_end
        self.generally_recommended_daily_usage = self.data['volumen'][0] / days_between
        
# TEST
if __name__ == "__main__":
    gcvt_data = GCVT_Data()
    print(gcvt_data.data.head())
    print('Available_files: ')
    print(gcvt_data.data_files)
    print(f'Generally recommended daily usage: {gcvt_data.generally_recommended_daily_usage}')