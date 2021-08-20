from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import randint


class AppLayout(BoxLayout):

    def roll_dice(self):
        print("Roll Dice")
        self.ids.dice.text = str(randint(1, 6))

    def select_sides(self, value):
        print(value)
        self.ids.dice.text = value


class DiceRollingApp(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    DiceRollingApp().run()
