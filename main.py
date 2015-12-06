from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import sqlite3 as lite
import sys


class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.strOrigen=''
        self.strDestino=''

    def ubicacion(self,origen,destino):
        print(str(origen + destino))
        self.strOrigen = origen
        self.strDestino = destino
        con = lite.connect('db/DBt.db')

        with con:
            cur = con.cursor()
            cur.execute("SELECT SECTOR,SUBSECTOR FROM tUbicaciones where UBICACION=:UBICACION",
                        {"UBICACION": str(self.strOrigen)})

            rows = cur.fetchone()
            pSectorO = rows[0]
            pSubsectorO = rows[1]
            print(str(pSectorO))

        with con:
            cur = con.cursor()
            cur.execute("SELECT SECTOR,SUBSECTOR FROM tUbicaciones where UBICACION=:UBICACION",
                        {"UBICACION": str(self.strDestino)})

            rows = cur.fetchone()
            pSectorD = rows[0]
            pSubsectorD = rows[1]
            print(str(pSectorD))


        self.tarifa(pSectorO,pSectorD,pSubsectorO)

    def tarifa(self,sectorO,sectorD,subsectorO):
        self.strsectorO = sectorO
        self.strsectorD = sectorD
        self.strsubsectorO = subsectorO
        #self.strSector = str(self.tmp_a1)
        #print(str(self.strArea))
        con = lite.connect('db/DBt.db')

        if self.strsubsectorO =='N':
            with con:
                cur = con.cursor()
                cur.execute("SELECT Tarifa FROM tAreaNorte where sOrigen=:sOrigen and sDestino=:sDestino",
                            {"sOrigen": str(self.strsectorO), "sDestino": str(self.strsectorD)})

                rows = cur.fetchall()
                for row in rows:
                        print(row)

        if self.strsubsectorO =='S':
            with con:
                cur = con.cursor()
                cur.execute("SELECT Tarifa FROM tAreaSur where sOrigen=:sOrigen and sDestino=:sDestino",
                            {"sOrigen": str(self.strsectorO), "sDestino": str(self.strsectorD)})

                rows = cur.fetchall()
                for row in rows:
                        print(row)

class TaxiApp(App):
    def build(self):

        return MainScreen()

if __name__ == '__main__':
    TaxiApp().run()
