from agents.import_agents import *
from mesa import Model
import random

def generate_water(self):   
    i = 1000

    for pos in water_list:
        water = WaterAgent(i,self, "water", "ground")
        self.schedule.add(water)
        self.grid.place_agent(water,pos)
        i=i+1

def generate_jungle(self, width, height):
    k = 2000
    for i in range(height):        
        for j in range(width):
            is_ground = True
            x=i
            y=j
            pos=(x,y)
            agents_list = self.grid.iter_cell_list_contents(pos)
            for item in agents_list:
                is_ground = False
                if (item.type != "ground"):
                    is_ground = True
            if (is_ground == True):
                jungle = JungleAgent(k,self, "jungle", "ground")
                self.schedule.add(jungle)
                self.grid.place_agent(jungle, (x, y))
                k=k+1

def generate_desert(self):
    desert = DesertAgent(999999,self, "desert", "ground")
    self.schedule.add(desert)
    self.grid.place_agent(desert, (12, 19))
    self.grid.place_agent(desert, (13, 19))
    self.grid.place_agent(desert, (14, 19))
    self.grid.place_agent(desert, (15, 19))
    self.grid.place_agent(desert, (16, 19))
    self.grid.place_agent(desert, (17, 19))
    self.grid.place_agent(desert, (18, 19))
    self.grid.place_agent(desert, (19, 19))
    self.grid.place_agent(desert, (13, 18))
    self.grid.place_agent(desert, (14, 18))
    self.grid.place_agent(desert, (15, 18))
    self.grid.place_agent(desert, (16, 18))
    self.grid.place_agent(desert, (17, 18))
    self.grid.place_agent(desert, (18, 18))
    self.grid.place_agent(desert, (19, 18))
    self.grid.place_agent(desert, (13, 17))
    self.grid.place_agent(desert, (14, 17))
    self.grid.place_agent(desert, (15, 17))
    self.grid.place_agent(desert, (16, 17))
    self.grid.place_agent(desert, (17, 17))
    self.grid.place_agent(desert, (18, 17))
    self.grid.place_agent(desert, (19, 17))
    self.grid.place_agent(desert, (14, 16))
    self.grid.place_agent(desert, (15, 16))
    self.grid.place_agent(desert, (16, 16))
    self.grid.place_agent(desert, (17, 16))
    self.grid.place_agent(desert, (18, 16))
    self.grid.place_agent(desert, (19, 16))
    self.grid.place_agent(desert, (15, 15))
    self.grid.place_agent(desert, (16, 15))
    self.grid.place_agent(desert, (17, 15))
    self.grid.place_agent(desert, (18, 15))
    self.grid.place_agent(desert, (19, 15))
    self.grid.place_agent(desert, (15, 14))
    self.grid.place_agent(desert, (16, 14))
    self.grid.place_agent(desert, (17, 14))
    self.grid.place_agent(desert, (18, 14))
    self.grid.place_agent(desert, (19, 14))
    self.grid.place_agent(desert, (16, 13))
    self.grid.place_agent(desert, (17, 13))
    self.grid.place_agent(desert, (18, 13))
    self.grid.place_agent(desert, (19, 13))
    self.grid.place_agent(desert, (18, 12))
    self.grid.place_agent(desert, (19, 12))
    
    
def generate_lion(self, lion_num):
    i=0
    while(i!=lion_num):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        pos=(x,y)
        if (self.grid.is_cell_empty((x,y))):
            lion = LionAgent(i, self, "lion", "animal")
            id_list[i]=ALIVE
            self.schedule.add(lion)
            self.grid.place_agent(lion, (x, y))
            i=i+1

def generate_antelope(self, antelope_num):
    for i in range(RANGE, RANGE+antelope_num):
        antelope = AntelopeAgent(i, self, "antelope", "animal")
        id_list[i]=ALIVE
        self.schedule.add(antelope)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(antelope, (x, y))

def generate_bird(self, bird_num):
    for i in range(RANGE*2, RANGE*2+bird_num):
        bird = BirdAgent(i, self, "bird", "animal")
        id_list[i]=ALIVE
        self.schedule.add(bird)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(bird, (x, y))

def generate_snake(self, snake_num):
    for i in range(RANGE*3, RANGE*3+snake_num):
        snake = SnakeAgent(i, self, "snake", "animal")
        id_list[i]=ALIVE
        self.schedule.add(snake)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(snake, (x, y))


def generate_crocodile(self, crocodile_num):
    for i in range(RANGE*4, RANGE*4+crocodile_num):
        crocodile = CrocodileAgent(i, self, "crocodile", "animal")
        id_list[i]=ALIVE
        self.schedule.add(crocodile)
        pos = random.choice(water_list)
        self.grid.place_agent(crocodile, pos)

def generate_bush(self, bush_num):
    i=RANGE*5
    while (i!=RANGE*5+bush_num):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        # Verifica se o bush será renderizado na agua
        if (self.grid.is_cell_empty((x,y))):
            bush = BushAgent(i,self, "bush", "plant")
            id_list[i]=ALIVE
            self.schedule.add(bush)
            self.grid.place_agent(bush, (x, y))
            i=i+1
