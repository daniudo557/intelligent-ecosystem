from models.wild_model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from config.variables import *


def agent_portrayal(agent):
    if (agent.health <= 0):
    	health_points = 0
    else:	 
    	health_points = agent.health/100.0
    
    portrayal = {"Shape": "",
                "scale": health_points,
                "Heath": agent.health,
                "specie": agent.specie,
                "ID": agent.unique_id,
                "gender" : agent.gender,
                "Layer": 1}
    if (agent.specie == "lion"):
        portrayal["Shape"]= "img/lion.png"
        portrayal["Layer"] = 0.1
    elif (agent.specie == "antelope"):
        portrayal["Shape"]= "img/antelope.png"
        portrayal["Layer"] = 0.1
    elif (agent.specie == "bird"):
        portrayal["Shape"]= "img/bird.png"
        portrayal["Layer"] = 0.1
    elif (agent.specie == "crocodile"):
        portrayal["Shape"]= "img/crocodile.png"
        portrayal["Layer"] = 0.1
    elif (agent.specie == "snake"):
        portrayal["Shape"]= "img/snake.png"
        portrayal["Layer"] = 0.1
    elif (agent.specie == "bush"):
        portrayal["Shape"]= "img/bush.png"
        portrayal["Layer"] = 0.1 
    elif(agent.specie == "jungle"):
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1
    elif(agent.specie == "water"):
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
        portrayal["w"] = 1
        portrayal["h"] = 1
    return portrayal

grid = CanvasGrid(agent_portrayal, 25, 25, 1000, 1000)
model_params = dict(width=25, 
                    height=25,
                    lion_num=lion_variables["lion_num"],
                    antelope_num=antelope_variables["antelope_num"],
                    bird_num=bird_variables["bird_num"],
                    snake_num=snake_variables["snake_num"],
                    crocodile_num=crocodile_variables["crocodile_num"],
                    bush_num=bush_variables["bush_num"])


chart = ChartModule([
                    {"Label": "Lion",
                        "Color": "Orange"},
                    {"Label": "Snake",
                        "Color": "Green"},
                    {"Label": "Antelope",
                        "Color": "Red"},
                    {"Label": "Bird",
                        "Color": "Blue"},
                    {"Label": "Crocodile",
                        "Color": "Brown"},                        
                    ],
                    data_collector_name='datacollector')

server = ModularServer(WildModel,
                       [chart,grid ],
                       "Wild Model",
                       model_params)
server.port = 8521
server.launch()

