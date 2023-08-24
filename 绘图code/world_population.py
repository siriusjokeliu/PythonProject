import json
import pygal_maps_world.maps
from countries import  get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

filename = '../data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

world_pops_1, world_pops_2,world_pops_3 = {},{},{}
erro_counrty = []
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':

        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code and population <10000000:
            world_pops_1[code] = population
        elif code and population <100000000:
            world_pops_2[code] = population
        elif code and population >=100000000:
            world_pops_3[code] = population
        elif code == None:
            erro_counrty.append(country_name)

wm_style = RS('#556699',base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = '2010 Wolrd popuklation'
wm.add('<10 Million',world_pops_1)
wm.add('<100Million',world_pops_2)
wm.add('>100 Million',world_pops_3)
wm.render_to_file('2010.svg')
