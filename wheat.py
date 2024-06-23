while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				till()
			harvest()
			move(North)
		move(East)	