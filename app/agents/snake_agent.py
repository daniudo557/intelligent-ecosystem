from mesa import Agent
from agents.import_agents import *
from config.variables import snake_variables as s

class SnakeAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.gender = generate_random_gender(self)
        self.specie = specie
        self.health = s["initial_health"]

    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts()
            self.damage()

    def percepts(self):
        self.breeding()
        self.set_move()
    
    def breeding(self):
        cellmates = get_object(self, "self")
        for other in cellmates:
            if(other.specie == "snake" and self.unique_id != other.unique_id):
                if(self.gender == "female" and other.gender == "male"):
                    self.born()

    def born(self):
        born_chance = random.randint(1,10)
        if (born_chance > s["born_chance"] and self.health>s["min_health_breeding"]):
            for i in range(RANGE):
                if (id_list[i] == DEAD):
                    possible_positions = get_neighborhood(self)
                    position_choose = self.random.choice(possible_positions)
                    born_position = self.avoid("snake", position_choose, possible_positions, 0)
                    if (born_position != None):
                        id_list[i]=ALIVE
                        agent_counter(self.specie, "born")
                        snake = SnakeAgent(i, self.model, "snake", "animal")
                        self.model.schedule.add(snake)
                        self.model.grid.place_agent(snake, self.pos)
                        break
                    break

    def set_move(self):
        possible_steps = get_neighborhood(self)
        possible_position = self.random.choice(possible_steps)
        agent_target = self.target() 
        
        if(agent_target!=False):
            new_possible_position = self.fight(agent_target, possible_position)
        else:
            new_possible_position = possible_position
        
        new_position = self.avoid(["crocodile", "lion"], new_possible_position, possible_steps, 0)
        
        if (new_position != None):
            self.move(new_position)

    def target(self):
        agents_list = get_object(self, "neighborhood")
        for item in agents_list:
            if (item.specie == "bird"):
                return item

        for item in agents_list:
            if (item.specie == "water"):
                self.drink()
                break
        return False

    def fight(self, other, possible_position):          
        if(self.health<=150):
            if(self.pos == other.pos):
                self.health = self.health+s["food_refill"]
                other.health = DEAD
                id_list[other.unique_id] = DEAD
                agent_counter(other.specie, "die")
                self.model.grid._remove_agent(other.pos, other)

            else:
                possible_position = other.pos

        return possible_position

    def avoid(self, avoid, possible_position, possible_steps, times):
        have_avoid = False
        agents_list = get_object(self, possible_position)
        for item in agents_list:
            if (item.specie in avoid):
                have_avoid = True
        if (have_avoid == True):
            if (times < 18):
                new_random_position = self.random.choice(possible_steps)
                times = times+1
                return self.avoid(avoid, new_random_position, possible_steps, times)
            else:
                return None
        else:
            return item.pos

    def drink(self):
        if(self.health<150):
            self.health = self.health+s["water_refill"]

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)
    
    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > s["damage_chance"]:
            self.health = self.health - s["damage_points"]
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                agent_counter(self.specie, "die")
                self.model.grid._remove_agent(self.pos, self)