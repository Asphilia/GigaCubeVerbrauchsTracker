##################################################
#                                                #
# GigaCube Verbrauchs Tracker Einstellungen      #
#                                                #
# Liest und setzt die Einstellungen              #
#                                                #
# Letztes Update: 16.08.2026                     #
# Autoren: Asphilia                              #
##################################################

# IMPORTE
# yaml
import yaml

# VARS
# settings file
SETTINGS_FILE = "settings.yaml"

# CLASSES
class GCVT_Settings:
    def __init__(self):
        '''
        Manager für die Einstellungen.
        Einstellungen werden im app Ordner in 
        settings.yaml gesetzt.
        '''
        # Load settings.yaml
        with open(SETTINGS_FILE, "r") as file:
            self.settings: dict = yaml.full_load(file)

    def save_settings(self):
        with open(SETTINGS_FILE, "w") as file:
            yaml.dump(self.settings)

    def get_saving_directory(self) -> str:
        save_dir = (
            self.settings
            .get('backend', dict())
            .get('data', dict())
            .get('saving_directory', '~/.gvct/data')
        )
        return save_dir

    def set_saving_directory(self, save_dir: str) -> bool:
        try:
            backend = self.settings.setdefault('backend', {})
            data = backend.setdefault('data', {'refresh_minutes': 60})
            data['saving_directory'] = save_dir
            self.save_settings()
            return True
        except:
            return False

    def get_refresh_minutes(self) -> int:
        return (
            self.settings
            .get('backend', {})
            .get('data', {})
            .get('refresh_minutes', 60)
        )

    def set_refresh_minutes(self, refresh_min: int) -> bool:
        try:
            backend = self.settings.setdefault('backend', {})
            data = backend.setdefault('data', {'saving_directory': '~/.gcvt/data'})
            data['refresh_minutes'] = refresh_min
            self.save_settings()
            return True
        except:
            return False

    def get_theme(self) -> str:
        return (
            self.settings
            .get('frontend', {})
            .get('theme', 'default')
        )

    def set_theme(self, theme: str) -> bool:
        try:
            frontend = self.settings.setdefault('frontend', {})
            frontend['theme'] = theme
            self.save_settings()
            return True
        except:
            return False

    def get_username(self) -> str:
        return (
            self.settings
            .get('frontend', {})
            .get('username', 'None')
        )

    def set_username(self, name:str) -> bool:
        try:
            frontend = self.settings.setdefault('frontend', {})
            frontend['username'] = name
            self.save_settings()
            return True
        except:
            return False

    def get_analysis(self) -> bool:
        return (
            self.settings
            .get('frontend', {})
            .get('analysis', False)
        )

    def set_analysis(self, analysis:bool) -> bool:
        try:
            frontend = self.settings.setdefault('frontend', {})
            frontend['analysis'] = analysis
            self.save_settings()
            return True
        except:
            return False

    def get_prognonsis(self) -> str:
        return (
            self.settings
            .get('frontend', {})
            .get('prognosis', 'mean')
        )

    def set_prognosis(self, prognosis:str) -> bool:
        try:
            frontend = self.settings.setdefault('frontend', {})
            frontend['prognosis'] = prognosis
            self.save_settings()
            return True
        except:
            return False

    def get_mean_time(self) -> str:
        return (
            self.settings
            .get('frontend', {})
            .get('data', {})
            .get('mean_time', 'start')
        )

    def set_mean_time(self, mean:str) -> bool:
        if not mean in ['start', 'custom']:
            return False
        try:
            frontend = self.settings.setdefault('frontend', {})
            data = frontend.setdefault('data', {})
            data['mean_time'] = mean
            self.save_settings
            return True
        except:
            return False

    def get_delta(self) -> str:
        return (
            self.settings
            .get('frontend', {})
            .get('data', {})
            .get('delta', '1d')
        )

    def set_mean_time(self, delta:str) -> bool:
        try:
            frontend = self.settings.setdefault('frontend', {})
            data = frontend.setdefault('data', {})
            data['delta'] = delta
            self.save_settings
            return True
        except:
            return False
