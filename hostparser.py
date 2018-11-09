import re


with open ('cab_lists.txt','rb' ) as cab_list:
  for cab in cab_list:
    print(cab)
    cab = cab.strip().lower()
    
    with open('switch_location2.txt', 'rb') as switches:
      for line in switches:
        line = line.strip()
        if cab in line:
          print(line)
