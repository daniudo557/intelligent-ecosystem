import random
from mesa import Model
from config.settings import *    

def get_neighborhood(self, pos=False):
    if not pos:
        pos = self.pos    
    neighborhood = self.model.grid.get_neighborhood(
        pos,
        moore=True,
        include_center=True)
    return neighborhood

def get_object(self, choice):
    if choice == "neighborhood":
        content = get_neighborhood(self)
    elif choice == "self":
        content = [self.pos]
    else:
        content = choice
    return self.model.grid.get_cell_list_contents(content)

def generate_random_gender(self):
    gender = random.randint(1,2)
    if (gender == 1):
        return "male"
    if (gender == 2):
        return "female"

def agent_counter(agent_specie, born_or_die):
    if (born_or_die == "die"):
        agent_counter_dict["{specie}".format(specie = agent_specie)] -= 1 
    else:
        agent_counter_dict["{specie}".format(specie = agent_specie)] += 1 

    