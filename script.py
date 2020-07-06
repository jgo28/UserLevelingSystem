import utils.database.methods as methods
import utils.database.config as config
import utils.levels as levels

metadata = config.get_metadata()
engine = config.get_engine()
connection = config.get_connection()
db = methods.Methods(engine, metadata, connection)

'''
Adding new users
'''
db.add_user("921010", "aly", 0, 0, 0)
db.add_user("921010", "jake", 0, 0, 0)
db.add_user("9211011", "sda", 0, 0, 0)
db.add_user("92102343", "asw", 0, 0, 0)
db.add_user("76565623", "wyh", 0, 0, 0)

'''
Retrieving user data
'''
print(db.get_all_users())
print(db.get_user_count())
user = db.get_user("9211011")
print(user)

'''
Update user information
'''
db.update_user("76565623", name="notjake")
db.update_user("76565623", lvl=2)
db.update_user("76565623", exp=200)
db.update_user("76565623", msg_count=40)
db.update_user("dfg", lvl=4, msg_count=430)
db.update_user("921010", lvl=16, msg_count=2345, exp=35789, name="notaly")

'''
Delete user data
'''
db.delete_user("921010")
db.delete_all()
print(db.get_user_count())
db.delete_all()

'''
Leveling System
'''
print(levels.max_exp())
print(levels.max_msgs())
print(levels.max_level)