from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import randint


class AppLayout(BoxLayout):

    def roll_dice(self):
        self.ids.dice.text = str(randint(1, 6))


class DiceRollingApp(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    DiceRollingApp().run()
