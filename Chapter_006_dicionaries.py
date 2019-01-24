# # alien_0 = {"color":"Green","points":5}
# alien_0 = {}
# alien_0["color"] = "yellow"
# alien_0["points"] = 5
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# alien_0["speed"] = "medium"
# print(alien_0)
# # print(alien_0["color"])
# # print(alien_0["points"])
# #
# # new_points = alien_0["points"]
# # print("You just earned "+ str(new_points)+" points!")
# #
# print("Original x-position: "+ str(alien_0["x_position"]))
#
# # move alien to right
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# if alien_0["speed"] == "fast":
#     x_increment = 3
#
# alien_0["x_position"] = alien_0["x_position"] + x_increment
# print("New x-position: " + str(alien_0["x_position"]))
#
# del alien_0["points"]
#
# print(alien_0)

fav_lang = {
    "jen": "python",
    'sarah':"c",
    'edward':'ruby',
    'phil':'python',
}
# print("Sarah's favorite language is "+fav_lang['sarah'].title()+'.')

# user_0={
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }
#
# for key, value in user_0.items():
#     print('\nkey: '+key)
#     print("value: "+value)
#
# for k,v in user_0.items():
#     print("\nKey: "+k)
#     print("Value: "+v)


# for name,language in fav_lang.items():
#     print(name.title()+ "'s favorite language is "+language.title()+'. \n')

for name in fav_lang.keys():
    print(name.title())

for name in fav_lang:
    print(name.title())