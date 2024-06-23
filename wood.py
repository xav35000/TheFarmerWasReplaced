while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			plant(Entities.Bush)
			quick_print(get_water())
			if get_water() <= 0.3:
				use_item(Items.Water_Tank)
			move(North)
		move(East)	