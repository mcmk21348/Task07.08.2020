class House:
    def __init__(self, household_type, total_area, mebel_list):
        self.household_type = household_type
        self.total_area = total_area
        self.remaing_area = 0
        self.mebel_list = mebel_list


    def furniture(self, name, name1, name2, area, area1, area2):
        self.name = name
        self.name1 = name1
        self.name2 = name2
        self.area = area
        self.area1 = area1
        self.area2 = area2
        


    def add_area(self):
        area3 = self.area + self.area1 + self.area2
        print('Участок для мебели', area3,'кв. метра')
        rob = self.total_area - area3
        print('Свободного места', rob,'кв. метра')
        return self.remaing_area + rob

    def __str__(self):
        return f'{self.household_type}, {self.total_area}, {self.add_area()}, {self.mebel_list}'
    
    
house = House('Частный', 50, ['Кровать: 4 квадратных метра', 'Стол: 2 квадратных метра', 'Шкаф: 15 квадратных метра'])
house.furniture('Кровать', 'Стол', 'Шкаф', 4, 2, 15)
print(house)






