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
			quick_print(get_water())
			if get_water() <= 0.3:
				use_item(Items.Water_Tank)
			move(North)
		move(East)
	for loop in range(5):
		trade(Items.Empty_Tank)