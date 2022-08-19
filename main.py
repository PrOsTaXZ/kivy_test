from turtledemo.__main__ import font_sizes

from kivy.app import App
from kivy.uix.button import Button

import requests
response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
data = response.json()
btc_prt = f"BTC:{round(data.get('btc_usd').get('last'), 2)}$\n"

class MyApp(App):
    def build(self):
        return Button(text='test',
                      font_size=30,
                      on_press=self.btn_pres,
                      on_release=self.btn_rele)
    def btn_rele(self, instance):
        instance.text = 'Нажми на меня'

    def btn_pres(self, instance):
        instance.text = btc_prt

if __name__ == "__main__":
    MyApp().run()