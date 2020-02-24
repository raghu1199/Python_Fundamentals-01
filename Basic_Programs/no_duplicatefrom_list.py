speed={'jan':44,'feb':45,'march':44,'april':34,'may':67,'june':23,'july':34,'aug':70}
speed_list=list()
for item in speed.values():
    if item not in speed_list:
        speed_list.append(item)

print(speed_list)