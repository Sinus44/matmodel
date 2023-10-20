from numpy import array

print("="*15 + " TASK 1 " + "="*15)

cargos = array([
	[37, 17, 52, 73, 72],
	[11, 39, 70, 20, 27],
	[12, 21, 25, 11, 30],
	[49, 35, 36, 35, 74],
	[40, 31, 78, 66, 79],
	[77, 14, 59, 67, 78]
]).T

minimum = float('inf')
minimum_data = []

# Бешенный перебор
for c1, cargo1 in enumerate(cargos[0]):
	for c2, cargo2 in enumerate(cargos[1]):
		if c2 == c1: continue
		for c3, cargo3 in enumerate(cargos[2]):
			if c3 == c2 or c3 == c1: continue
			for c4, cargo4 in enumerate(cargos[3]):
				if c4 == c1 or c4 == c2 or c4 == c3: continue
				for c5, cargo5 in enumerate(cargos[4]):
					if c5 == c1 or c5 == c2 or c5 == c3 or c5 == c4: continue

					s = cargo1 + cargo2 + cargo3 + cargo4 + cargo5 # Считаем сумму
					if s < minimum: # Проверяем, минимум ли это
						minimum = s
						minimum_data = [c1, c2, c3, c4, c5]

print(f"Сумма затрат: {minimum}")

for g, d in enumerate(minimum_data):
	print(f"Груз / Машина: {g+1} / {d+1}")


print("="*15 + " TASK 2 " + "="*15)
p = array([
	[3, 2, 1],
	[2, 3, 3],
	[1, 1, 2]
]).T


minimum = float('inf')
minimum_data = []

# Бешенный перебор
for c1, cargo1 in enumerate(p[0]):
	for c2, cargo2 in enumerate(p[1]):
		if c2 == c1: continue
		for c3, cargo3 in enumerate(p[2]):
			if c3 == c2 or c3 == c1: continue
			s = cargo1 + cargo2 + cargo3 # Считаем сумму
			if s < minimum: # Проверяем, максимум ли это
				minimum = s
				minimum_data = [c1, c2, c3]

print(f"Сумма предпочтений: {minimum}")

for g, d in enumerate(minimum_data):
	print(f"Группа {g+1} Предприятие {d+1}")

n = array([
	[7, 4, 8],
	[10, 8, 6],
	[5, 6, 7]
]).T

###
minimum = float('inf')
minimum_data = []

# Бешенный перебор
for c1, cargo1 in enumerate(n[0]):
	for c2, cargo2 in enumerate(n[1]):
		if c2 == c1: continue
		for c3, cargo3 in enumerate(n[2]):
			if c3 == c2 or c3 == c1: continue
			s = cargo1 + cargo2 + cargo3 # Считаем сумму
			if s < minimum: # Проверяем, максимум ли это
				minimum = s
				minimum_data = [c1, c2, c3]

print(f"Сумма НИИ: {minimum}")
print("")
for g, d in enumerate(minimum_data):
	print(f"Группа {g+1} НИИ {d+1}")