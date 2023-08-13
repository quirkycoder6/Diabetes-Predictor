from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from diabetes import DP


Builder.load_file('DiseasePredictor.kv')

class MainLayout(Widget):
    pass

class DiseasePredictorAPP(App):
    data = []
    pregnancies, glucose, blood_pressure, skin_thickness, insulin, age = 0, 0, 0, 0, 0, 0
    bmi, diabetes_pedigree_function = 0.0, 0.0

    def build(self):
        return MainLayout()

    def process(self, key):
        if key == 'f1':
            self.pregnancies = self.root.ids.f1.text
        elif key == 'f2':
            self.glucose = self.root.ids.f2.text
        elif key == 'f3':
            self.blood_pressure = self.root.ids.f3.text
        elif key == 'f4':
            self.skin_thickness = self.root.ids.f4.text
        elif key == 'f5':
            self.insulin = self.root.ids.f5.text
        elif key == 'f6':
            self.bmi = self.root.ids.f6.text
        elif key == 'f7':
            self.diabetes_pedigree_function = self.root.ids.f7.text
        elif key == 'f8':
            self.age = self.root.ids.f8.text

    def calculate(self):
        self.data = [int(self.pregnancies), int(self.glucose), int(self.blood_pressure), int(self.skin_thickness),
                     int(self.insulin), float(self.bmi), float(self.diabetes_pedigree_function), int(self.age)]
        results = DP(self.data).model()

        if (results == 0):
            self.root.ids.result.color = (45/255, 227/255, 189/255, 1)
            self.root.ids.result.text = 'Not Diabetic !'
        else:
            self.root.ids.result.color = (245/255, 0/255, 19/255, 1)
            self.root.ids.result.text = 'Diabetic !!'

if __name__ == "__main__":
    DiseasePredictorAPP().run()