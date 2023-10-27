from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

class HomeScreen(Screen):
    def calculation(self,formula):
        super(HomeScreen).__init__()

        if formula:
            try:
                self.ids.DisplayScreen.text = str(eval(formula))
            except:
                self.ids.DisplayScreen.text = 'Error'


class BoxLayoutExample():
    pass

class CalculatorApp(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    CalculatorApp().run()

Window.close()
