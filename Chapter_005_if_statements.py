# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())
#
# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
#
# age = 18
#
# answer = 42
#
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
# else:
#     print("Thats right")
#
# age = 3
#
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
# •  Write an if statement to test whether the alien’s color is green If it is, print
# a message that the player just earned 5 points
# •  Write one version of this program that passes the if test and another that
# fails (The version that fails will have no output )
alien_color = ['green', 'yellow', 'red']

alien_killed = "blue"

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

print(alien_1['color'])
print(alien_1['points'])

if alien_killed == 'green':
    print("you earned () points".format(alien_0['points']))
elif alien_killed == 'red':
    print("Your earned () points".format(alien_1['points']))
elif alien_killed == 'yellow':
    print("Your earned () points".format(alien_2['points']))

new_points = alien_0['points']

print("You just earned " + str(new_points) + " points!")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise
#
#
# 5-3, and
# write an if-else chain
# •  If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien
# •  If the alien’s color isn’t green, print a statement that the player just earned
# 10 points
# •  Write one version of this program that runs the if block and another that
# runs the else block