import kivy

kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.button import Button as buton
from kivy.uix.gridlayout import GridLayout as gridl



#дочерный клас Gridlaylout
class kanteinter(gridl):


    def toy(self):
        self.lable_widget.text = self.inpyt_widget.text







class myApp(App):
    def  build(self):

        return kanteinter()
if __name__=="__main__":
    myApp().run()


