import i3


workspaces = i3.get_workspaces()
for workspace in workspaces:
	if workspace['focused']:
		if workspace["name"] != "10":
			i3.command('move', 'container to workspace number ' + str(int(workspace["name"])+1))			
		else:
			i3.command('move', 'container to workspace number 1') 
