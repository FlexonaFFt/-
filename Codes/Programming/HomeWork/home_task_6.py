class Pie():
  def __init__(self, topping, testo, size):
    self.topping = topping
    self.testo = testo
    self.size = size
    self.baked = False

  def bake(self):
    self.baked = True
    print(f"{self.topping} пирог размера ({self.size}) был испечён!")
  
  def add_topping(self, additional_topping):
        self.topping += f", {additional_topping}"
        print(f"К пирогу добавлены дополнительные атрибуты в виде: ({additional_topping})")

  def description(self):
    if self.baked == True:
      print(f"Этот {self.size} пирог {self.testo} с начинкой ({self.topping}) уже испечен.")
    else:
      print(f"Этот {self.size} пирог {self.testo} с начинкой ({self.topping}) ещё не испечен.")

apple_pie = Pie("яблочный", "на лёгком тесте", "средний")
apple_pie.description()
apple_pie.bake()
apple_pie.add_topping("взбитые сливки")