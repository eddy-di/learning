# video 9 from class it is basically shows how with the help of magic methods it is possible to create your own containers
class TagCloud:
    def __init__(self): # this part of code creates 
        self.tags = {}
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    def __len__(self):
        return len(self.tags)
    def __iter__(self):
        iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("C#")
cloud.add("C#")
cloud.add("C#")
print(cloud.tags)