while get_pos_y() != 0:
	move(South)
while get_pos_x() != 0:
	move(West)
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		move(North)
	move(East)
