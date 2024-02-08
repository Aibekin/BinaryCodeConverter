from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.5, 0.8, 0.2, 1)

class Calculate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.formula = ''
        self.result_text = ''
        
    def update_label(self):
        self.ids.text_calc.text = self.formula
        
    def add_number(self, instance):
        self.formula += str(instance.text)
        self.update_label()
        
    def remove_number(self):
        self.formula = self.formula[:-1]
        self.update_label()
        
    def get_the_binary_code(self):
        result = self.find_all_values()
        result.reverse()
        self.result_text = ''.join(map(str, result))
        print(result)
        app = App.get_running_app()
        app.result_text = self.result_text

    def find_all_values(self):
        binary_code = []
        new_value = int(self.formula)
        while new_value // 2 != 0:
            res = new_value % 2
            new_value = new_value // 2
            binary_code.append(res)
        binary_code.append(1)
        return binary_code
        
class Results(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self, *args):
        app = App.get_running_app()
        result_text = app.result_text
        self.ids.results_text.text = result_text
    
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Calculate(name='main'))
        sm.add_widget(Results(name='results'))
        return sm
    
if __name__ == "__main__":
    MyApp().run()   