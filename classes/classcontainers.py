# video 9 from class it is basically shows how with the help of magic methods it is possible to create your own containers
class TagCloud:
    def __init__(self): # this part of code creates an empty dictionary that is named tags 
        self.tags = {}
    def add(self, tag): # this part allows to add tags and convert them into lowercase letters
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    def __getitem__(self, tag): # allows to look at the tgs and its ammount
        return self.tags.get(tag.lower(), 0)
    def __setitem__(self, tag, count): # allows to set specific limit to tags
        self.tags[tag.lower()] = count
    def __len__(self): # gives the numbers of different tags, for 5 python tags and 2 c# tags the result will be 2 (types of tags are given)
        return len(self.tags)
    def __iter__(self): # allows to iterate over each tag in dictionary
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
cloud["python"] = 2
for i in cloud.tags:
    if i == "c#":
        print("Yes")
print(len(cloud))
print(cloud.tags)