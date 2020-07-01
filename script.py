import utils.main as m
'''
Adding new users
'''
# m.add_user("921010", "aly", 0, 0, 0)
# m.add_user("921010", "jake", 0, 0, 0)
# m.add_user("9211011", "sda", 0, 0, 0)
# m.add_user("92102343", "asw", 0, 0, 0)
# m.add_user("76565623", "wyh", 0, 0, 0)
'''
Retrieving user data
'''
# print(m.get_all_users())
# print(m.get_user_count())
'''
Update user information
'''
m.update_user("76565623", name="notjake")
m.update_user("76565623", lvl=2)
m.update_user("76565623", exp=200)
m.update_user("76565623", msg_count=40)
m.update_user("dfg", lvl=4, msg_count=430)
m.update_user("921010", lvl=16, msg_count=2345, exp=35789, name="notaly")
