class Human:
    physical = "appearance" # this part is a class attribute the general class is defined here
    def __init__(self, height, hair_color, eye_color): # instance atributes are defined here,
        self.height = int(height)
        self.hair_color = hair_color
        self.eye_color = eye_color
    def who(self):
        print(f"This human has {self.height} cm height, {self.hair_color} hairs, and {self.eye_color} eyes.")


human1 = Human(166, "dark", "brown")
human1.who()
human2 = Human(178, "blonde", "blue")
