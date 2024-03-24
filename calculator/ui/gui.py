from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from calculator import Calculator
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


BUTTONS_NAMES = [
    ['C','7', '8', '9', '/'],
    ['History','4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+'],
]


class CalculatorApp(App):
    def build(self):
        self._calc = Calculator()
        
        main_layout = BoxLayout(orientation='vertical')

        self._display = Label(text="0", font_size=24, size_hint=(1, 0.75))
        main_layout.add_widget(self._display)

        for button_names_row in BUTTONS_NAMES:
            grid_row = BoxLayout()
            for button_name in button_names_row:
                button = Button(text=button_name, font_size=24, on_press=self.on_button_press)
                grid_row.add_widget(button)
            main_layout.add_widget(grid_row)

        # Assuming you add a ScrollView for history at the top or bottom
        self._history_scroll = ScrollView(size_hint=(1, 0.2), do_scroll_x=False, do_scroll_y=True)
        self._history_label = Label(size_hint_y=None, markup=True)


        self._history_scroll.add_widget(self._history_label)


        main_layout.add_widget(self._history_scroll)  # Add wherever appropriate in the layout

        
    

        return main_layout
    


    def on_button_press(self, button):
        match button.text:
            case "C":
                self._calc.clear_expression()
                self._display.text = "0"
            case "=":
                try:
                    result = self._calc.compute_result()
                    self._display.text = str(result)
                    #self.update_history_display()
                except ValueError as e:
                    self._display.text = "Error"
            
            case "History":
                self._display.text = ""  
                self._history_label.text = '\n'.join(self._calc.history)
            
            case "+":
                self._calc.plus()
                self._display.text = self._calc.expression
            case "-":
                self._calc.minus()
                self._display.text = self._calc.expression
            case "*":
                self._calc.multiply()
                self._display.text = self._calc.expression
            case "/":
                self._calc.divide()
                self._display.text = self._calc.expression
            case ".":
                self._calc.dot()
                self._display.text = self._calc.expression
            case "Clear History":
                self._calc.clear_history()  
                self.update_history_display()  
            case _:
                self._calc.digit(button.text)
                self._display.text = self._calc.expression
            
    

if __name__ == '__main__':
    CalculatorApp().run()
