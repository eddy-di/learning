class Human:
    physical = "appearance" # this part is a class attribute the general class is defined here
    def __init__(self, height, hair_color, eye_color): # instance atributes are defined here,
        self.height = int(height)
        self.hair_color = hair_color
        self.eye_color = eye_color


human1 = Human(166, "dark", "brown")
print(human1.eye_color)
human2 = Human(178, "blonde", "blue")
print(human2.height)