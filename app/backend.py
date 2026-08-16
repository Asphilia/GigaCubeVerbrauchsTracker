##################################################
#                                                #
# GigaCube Verbrauchs Tracker Backend            #
#                                                #
# Übernimmt Verbrauchsabfragen und Speicherung   #
#                                                #
# Letztes Update: 16.08.2026                     #
# Autoren: Asphilia                              #
##################################################

# IMPORTE
# Um den aktuellen Verbrauch abzufragen
import requests 
# Für FehlerLogs
import time
# Einstellungen
from settings import GCVT_Settings

# VARIABLEN
# URL für die Verbrauchsabfrage
URL = "https://center.vodafone.de"
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0'}

# CLASSES
class GCVT_Backend:
    def __init__(self):
        self.settings = GCVT_Settings()

    def extract(self):
        return self._extract_usage(
            self._get_html()
        )

    def _extract_usage(self, html_file: str) -> dict:
        '''
        Extrahiert die Verbrauchsdaten aus dem HTML
        Gibt die Verbrauchsdaten als Dictionary zurück
        '''
        _, relevant = html_file.split('Meine verbrauchten GB:</div>\n<div class=\"fr\">', 1)
        verbrauch, rest = relevant.split('GB', 1)
        _, relevant = rest.split('Meine Bandbreite wird begrenzt bei:</div>\n<div class=\"fr\">', 1)
        volumen, rest = relevant.split('GB', 1)
        _, relevant = rest.split('Rechnungszeitraum:</div>\n<div class=\"fr\">', 1)
        zeitraum, _ = relevant.split('</div>', 1)
        return {
            "verbrauch": float(".".join(verbrauch.split(","))),
            "volumen_gesamt": float(".".join(volumen.split(","))),
            "zeitraum": zeitraum
        }

    def _get_html(self) -> str:
        '''
        Ruft die center.vodafone.de Seite auf, um die Verbrauchsdaten zu erhalten
        '''
        r = requests.get(URL, headers=HEADERS)
        if not r.status_code == 200:
            error_file = f"GigaCubeVerbrauchsTracker_Error_{time.time()}.txt"
            with open(error_file, "x") as err_file:
                err_file.write(r.text)
            raise Exception(f"Status Code ist {r.status_code}. Text liegt in Error File {err_file}")
        return r.text

    def _test(self):
        with open('../test/test-verbrauchsdaten.html', 'r') as test_file:
            test_html = test_file.read()
        print('Beginning test of GCVT_Backend')
        expected = {
            "verbrauch": 16.7,
            "volumen_gesamt": 26,
            "zeitraum": "13.08.-12.09.2026"
        }
        extraction_result = 'SUCCESS' if self._extract_usage(test_html) == expected else "FAILED"
        print('Extraction Test: ' + extraction_result)
        connection_result = 'SUCCESS' if 'Meine verbrauchten GB:' in self._get_html() else 'FAILED'
        print('Connection Test: ' + connection_result)

if __name__ == "__main__":
    gcvt = GCVT_Backend()
    gcvt._test()