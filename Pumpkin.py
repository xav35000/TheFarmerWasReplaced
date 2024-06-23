while get_pos_y() != 0:
	move(South)
while get_pos_x() != 0:
	move(West)
while True:	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			n = get_pos_x() + get_pos_y()
			def is_even(n):
				return n % 2 == 0
			if is_even(n):
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			trade(Items.Carrot_Seed)
			till()
			plant(Entities.Carrots)
			quick_print(get_water())
			if get_water() <= 0.3:
				use_item(Items.Water_Tank)
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
			move(North)
		move(East)
	for loop in range(4):
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				quick_print(get_entity_type())
				if get_entity_type() == None:
					trade(Items.Pumpkin_Seed)
					plant(Entities.Pumpkin)
					move(North)
				else:
					move(North)
			move(East)
		