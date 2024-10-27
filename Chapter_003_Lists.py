bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[2])
print(bicycles[2].title())
print(bicycles[-1])
print(bicycles[-2])

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('Honda')
print(motorcycles)

motorcycles.insert(2, 'BMW')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)

print(motorcycles)
motorcycles.append('BMW')
print(motorcycles)

motorcycles.remove('BMW')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.sort()

print(popped_motocycle)