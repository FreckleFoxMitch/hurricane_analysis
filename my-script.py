# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damages):
  """Convert damages data from string to float and return converted data as a list."""
  new_damages = []
  for damage in damages:
    if "M" in damage:
      new_damage = float(damage.strip("M")) * conversion["M"]
      new_damages.append(new_damage)
    elif "B" in damage:
      new_damage = float(damage.strip("B")) * conversion["B"]
      new_damages.append(new_damage)
    else:
      new_damages.append(damage)
  return new_damages

# update and view damages data
damages_updated = update_damages(damages)
# print(damages_updated)


# Create a Table
def create_hurricane_table(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
  hurricane_table = {}
  for i in range(len(names)):
    hurricane_table[names[i]] = {
      "Name": names[i], 
      "Month": months[i], 
      "Year": years[i], 
      "Max Sustained Wind": max_sustained_winds[i], 
      "Areas Affected": areas_affected[i], 
      "Damage": damages[i], 
      "Deaths": deaths[i]
      }
  return hurricane_table

# Create and view the hurricanes dictionary
hurricanes = create_hurricane_table(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)
# print(hurricanes)


# Organizing by Year
def create_hurricane_years(hurricanes):
  """Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""
  hurricanes_in_years = {}
  for cane in hurricanes.keys():
    current_cane = hurricanes[cane]
    current_year = hurricanes[cane]["Year"]
    if current_year not in hurricanes_in_years.keys():
      hurricanes_in_years[current_year] = [current_cane]
    else:
      hurricanes_in_years[current_year].append(current_cane)
  return hurricanes_in_years

# create and view new dictionary of hurricanes with year as key
hurricane_years = create_hurricane_years(hurricanes)
# print(hurricane_years)


# Counting Damaged Areas
def counting_damages(hurricanes):
  """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""
  damaged_areas = {}
  for cane in hurricanes.keys():
    current_areas = hurricanes[cane]["Areas Affected"]
    for area in current_areas:
      if area not in damaged_areas.keys():
        damaged_areas[area] = 1
      else:
        damaged_areas[area] += 1
  return damaged_areas

# create and view dictionary of areas to store the number of hurricanes involved in
areas_affected = counting_damages(hurricanes)
# print(areas_affected)


# Calculating Maximum Hurricane Count
def calculate_max_count(areas):
  """Find most affected area and the number of hurricanes it was involved in."""
  area_max_count = ""
  max_count = 0
  for area, count in areas.items():
    if count > max_count:
      max_count = count
      area_max_count = area
  print("Most frequently affected area is {area}. The number of hurricanes involved in is {count}.".format(area=area_max_count, count=max_count))
  return area_max_count, max_count

# find and view most frequently affected area and the number of hurricanes involved in
most_affected_area = calculate_max_count(areas_affected)
# print(most_affected_area)


# Calculating the Deadliest Hurricane
def calculate_max_deaths(hurricanes):
  """Find the highest mortality hurricane and the number of deaths it caused."""
  deadliest_cane = ""
  max_deaths = 0
  for cane in hurricanes.keys():
    current_name = cane
    current_deaths = hurricanes[cane]["Deaths"]
    if current_deaths > max_deaths:
      max_deaths = current_deaths
      deadliest_cane = current_name
  print("The highest mortality hurricane is {name} with number of deaths {num} people.".format(name=deadliest_cane, num=max_deaths))
  return deadliest_cane, max_deaths

# find and view highest mortality hurricane and the number of deaths
highest_mortality_hurricane = calculate_max_deaths(hurricanes)
# print(highest_mortality_hurricane)


# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def calculate_mortality_rating(hurricanes):
  """Categorize hurricanes by mortality and return a dictionary."""
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes.keys():
    current_cane = hurricanes[cane]
    current_deaths = hurricanes[cane]["Deaths"]
    if current_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(current_cane)
    elif current_deaths > mortality_scale[0] and current_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(current_cane)
    elif current_deaths > mortality_scale[1] and current_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(current_cane)
    elif current_deaths > mortality_scale[2] and current_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(current_cane)
    elif current_deaths > mortality_scale[3] and current_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(current_cane)
    elif current_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(current_cane)
  return hurricanes_by_mortality

# categorize and view hurricanes in new dictionary with mortality severity as key
hurricane_mortality_rating = calculate_mortality_rating(hurricanes)
# print(hurricane_mortality_rating)


# Calculating Hurricane Maximum Damage
def calculate_max_damage(hurricanes):
  """Find the highest damage inducing hurricane and its total cost."""
  max_damage_cane = ""
  max_damage = 0
  for cane in hurricanes.keys():
    current_name = cane
    current_damage = hurricanes[cane]["Damage"]
    if current_damage == "Damages not recorded":
      pass
    elif current_damage > max_damage:
      max_damage = current_damage
      max_damage_cane = current_name
  print("The hurricane that caused the greatest damage is {name}. Full damage cost was {num}$.".format(name=max_damage_cane, num=max_damage))
  return max_damage_cane, max_damage

# find and view highest damage inducing hurricane and its total cost
max_damage_hurricane = calculate_max_damage(hurricanes)
# print(max_damage_hurricane)


# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
                
def calculate_damage_rating(hurricanes):
  """Categorize hurricanes by damage and return a dictionary."""
  hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for cane in hurricanes.keys():
    current_cane = hurricanes[cane]
    current_damage = hurricanes[cane]["Damage"]
    if current_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(current_cane)
    elif current_damage > damage_scale[0] and current_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(current_cane)
    elif current_damage > damage_scale[1] and current_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(current_cane)
    elif current_damage > damage_scale[2] and current_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(current_cane)
    elif current_damage > damage_scale[3] and current_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(current_cane)
    elif current_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(current_cane)
  return hurricanes_by_damage

# categorize and view hurricanes in new dictionary with damage severity as key
hurricane_damage_rating = calculate_damage_rating(hurricanes)
# print(hurricane_damage_rating)