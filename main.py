from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.properties import ObjectProperty
import requests
import subprocess
import os
from database import Database
from kivy.core.window import Window

Builder.load_file('converter.kv')


class CurrencyConverterScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class MoneyCurrencyApp(MDApp):
    db = Database()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        self.screen = CurrencyConverterScreen()
        return self.screen

    def convert_currency(self):
        from_currency = self.screen.ids.currency1_field.text.upper()
        to_currency = self.screen.ids.currency2_field.text.upper()
        amount = self.screen.ids.amount_field.text

        try:
            response = requests.get(
                f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            )
            data = response.json()
            converted_amount = data['rates'][to_currency]
            result_text = f"{to_currency} {converted_amount} "
            self.screen.ids.output_label.text = result_text
           
        except Exception as e:
            self.screen.ids.output_label.text = "Error occurred: " + str(e)

    def logout_button(self):
        subprocess.Popen(["python", "login.py"])
        os._exit(0)

    def on_stop(self):
        self.db.close_db_connection()

class AboutApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.screen = AboutScreen()
        return self.screen

if __name__ == "__main__":
    Window.size = (368, 640)
    MoneyCurrencyApp().run()
