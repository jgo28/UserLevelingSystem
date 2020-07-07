import utils.database.methods as methods
import utils.database.config as config
import utils.levels as levels

metadata = config.get_metadata()
engine = config.get_engine()
connection = config.get_connection()
data = methods.Methods(engine, metadata, connection)

'''
Adding new users
'''
data.add_user("921010", "aly", 1, 0, 0)
data.add_user("9210310", "jake", 1, 0, 0)
data.add_user("9211011", "sda", 1, 0, 0)
data.add_user("92102343", "asw", 1, 0, 0)
data.add_user("76565623", "wyh", 1, 0, 0)

'''
Retrieving user data
'''
print(data.get_all_users())
print(data.get_user_count())
print(data.user_exists("921010"))
user = data.get_user("921010")
print(user)

'''
Update user information
'''
data.update_user("76565623", name="notjake")
data.update_user("76565623", lvl=2)
data.update_user("76565623", exp=200)
data.update_user("76565623", msg_count=40)
data.update_user("dfg", lvl=4, msg_count=430)
data.update_user("921010", lvl=16, msg_count=2345, exp=35789, name="notaly")

'''
Leveling System
'''
print(levels.get_max_exp())
print(levels.get_max_msgs())
print(levels.max_level)
levels.msg_sent(data.get_user("921010"))

'''
Delete user data
'''
data.delete_user("921010")
data.delete_all()
print(data.get_user_count())
data.delete_all()
