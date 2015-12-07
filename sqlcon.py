import sqlite3 as lite
import sys


class Conexion(object):

    def __init__(self,origen,destino):
        self.strOrigen = origen
        self.strDestino = destino
        self.pSectorO= ''
        self.pSectorD=''
        self.pSubsectorO=''
        self.pSubsectorD=''
        self.strsectorO=''
        self.strsectorD=''
        self.strsubsectorO=''
        self.strsubsectorD=''
        self.strTarifa=''

    def ubicacion(self):
        #self.strOrigen= strOrigen
        #self.strDestino= strDestino
        con = lite.connect('db/DBt.db')

        with con:
            cur = con.cursor()
            cur.execute("SELECT SECTOR,SUBSECTOR FROM tUbicaciones where UBICACION=:UBICACION",
                        {"UBICACION": str(self.strOrigen)})

            rows = cur.fetchone()
            self.pSectorO = rows[0]
            self.pSubsectorO = rows[1]
            #print(str(pSectorO))

        with con:
            cur = con.cursor()
            cur.execute("SELECT SECTOR,SUBSECTOR FROM tUbicaciones where UBICACION=:UBICACION",
                        {"UBICACION": str(self.strDestino)})

            rows = cur.fetchone()
            self.pSectorD = rows[0]
            self.pSubsectorD = rows[1]
            #print(str(self.pSectorD))

        #self.tarifa(pSectorO,pSectorD,pSubsectorO)

    def tarifa(self):
        self.strsectorO = self.pSectorO
        self.strsectorD = self.pSectorD
        self.strsubsectorO = self.pSubsectorO
        #self.strSector = str(self.tmp_a1)
        #print(str(self.strArea))
        #db = dbcon.Conexion
        con = lite.connect('db/DBt.db')

        if self.strsubsectorO =='N':
            with con:
                cur = con.cursor()
                cur.execute("SELECT Tarifa FROM tAreaNorte where sOrigen=:sOrigen and sDestino=:sDestino",
                            {"sOrigen": str(self.strsectorO), "sDestino": str(self.strsectorD)})

                rows = cur.fetchall()
                #for row in rows:
                #print(row)
                self.strTarifa= rows[0]

        if self.strsubsectorO =='S':
            with con:
                cur = con.cursor()
                cur.execute("SELECT Tarifa FROM tAreaSur where sOrigen=:sOrigen and sDestino=:sDestino",
                            {"sOrigen": str(self.strsectorO), "sDestino": str(self.strsectorD)})

                rows = cur.fetchall()
                #for row in rows:
                #print(str(rows[0]))
                self.strTarifa= rows[0]