with open("stripped") as f:
	lines = f.read().splitlines()

with open("filtered", "w+") as f:
	for line in lines:
		# Ignore comments
		if not line.startswith("#"):
			# Remove A-number and omit final comma
			f.write(line.split(" ,", 1)[1][:-1]+"\n")
