from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import sqlcon as dbcon

Window.size = (400, 500)


class MainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def showTarifa(self, origen, destino):

        try:
            self.db = dbcon.Conexion(origen,destino)
            self.db.ubicacion()
            sOrigen = self.db.pSectorO
            sDestino= self.db.pSectorD
            self.db.tarifa()
            sTarifa = self.db.strTarifa
            #print(sTarifa)
            self.box = GridLayout(cols=1)
            self.box.add_widget(Label(text='Desde: '+origen+ '\nHasta: '+destino))
            self.box.add_widget(Label(text=str(sTarifa)))

            self.popup = Popup(title='Tarifa aproximada', content=self.box, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        except Exception:
            self.box = GridLayout(cols=1)
            self.box.add_widget(Label(text='Datos incorrectos, favor \n'
                                           'verificar origen y destino'))

            self.popup = Popup(title='Tarifa', content=self.box, size_hint=(None, None), size=(250, 200))
            self.popup.open()

class TaxiApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    TaxiApp().run()
