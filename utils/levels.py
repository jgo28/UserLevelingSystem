import utils.database.methods as methods
import utils.database.config as config

metadata = config.get_metadata()
engine = config.get_engine()
connection = config.get_connection()
db = methods.Methods(engine, metadata, connection)

exp_mod = 1   # experience point modifier; progession speed through the system
exp_gain = 15   # experience points gained per message

# Defines the message requirements for each level. Each element is the number of
# messages for that level. Each level is represented by an element in the array.
# 10 levels in each row of the list.
msg_list = [
        5, 5, 10, 10, 10, 20, 20, 20, 20, 20,
        30, 30, 30, 30, 30, 30, 30, 30, 40, 40,
        40, 40, 40, 40, 40, 50, 50, 50, 50, 50,
        50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
        60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
        70, 70, 70, 80, 80, 80, 80, 90, 90, 90,
        100, 100, 100, 100, 100, 100, 100, 100, 200, 200,
        200, 200, 200, 200, 200, 200, 250, 250, 250, 500,
        500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
        1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000, 5000
    ]

# Generates the experience requirements for each level. Takes the exp_gain
# per message and the exp_mod and multiples it by each element in the message
# requirements list.
exp_list = [i * exp_gain for i in msg_list]

# Generates the experience requirements to achieve a level at that point
# in time.
exp_req = []
for i in range(len(exp_list)):
    if i == 0:
        exp_req.append(exp_list[i])
    else:
        exp_req.append(exp_list[i] + exp_req[i-1])

# Maximum level in the system
max_level = len(msg_list)


def msg_sent(user):
    '''
    Each time a user sends a message, reward them with experience points.
    If the user reaches a certain threshold of points, their level increases.
    '''
    d_id = user.get("discord_id")
    exp = user.get("experience")
    lvl = user.get("level")
    msgs = user.get("message_count")
    add_msg_count(d_id, msgs)
    if not is_max_exp(d_id):
        add_experience(d_id, exp)
    if ready_to_level(lvl, exp) and not is_max_lvl(d_id):
        add_level(d_id, lvl)


def add_experience(discord_id, exp):
    '''Update user experience value in database.'''
    max_exp = get_max_exp()
    if exp < max_exp:
        exp = exp + exp_gain * exp_mod
    elif exp > max_exp:
        exp = max_exp
    elif exp == max_exp:
        return
    db.update_user(discord_id, exp = exp)


def add_level(discord_id, level):
    '''Increases the user's level by 1 in the database.'''
    if level < max_level: 
        level = level + 1
        db.update_user(discord_id, lvl = level)


def add_msg_count(discord_id, msgs):
    '''Increments the user's message count by 1 in the database.'''
    msgs = msgs + 1
    db.update_user(discord_id, msg_count = msgs)


def ready_to_level(level, exp):
    '''
    Checks if the user has met the experience requirements for the next level.
    '''
    print(exp)
    print(exp_req[level-1])
    if exp >= exp_req[level-1]:
        return True
    return False


def get_user_exp(discord_id):
    user = db.get_user(discord_id)
    return int(user.get("experience"))


def get_user_lvl(discord_id):
    user = db.get_user(discord_id)
    return user.get("level")


def get_user_msgs(discord_id):
    user = db.get_user(discord_id)
    return user.get("message_count")


def get_max_exp():
    '''Returns maxiumum experience required to hit level 100.'''
    exp = sum(exp_list)
    return exp


def get_max_msgs():
    '''Returns maximum messages required to hit level 100.'''
    msgs = sum(msg_list)
    return msgs


def is_max_lvl(discord_id):
    '''Checks to see if user has hit max level.'''
    cur_lvl = get_user_lvl(discord_id)
    if cur_lvl == max_level:
        return True
    return False


def is_max_exp(discord_id):
    '''Checks to see if user has hit max experience.'''
    cur_exp = get_user_exp(discord_id)
    if cur_exp == get_max_exp():
        return True
    return False


def is_max_msgs(discord_id):
    '''Checks to see if user has hit the max amount of messages.'''
    cur_msgs = get_user_msgs(discord_id)
    if cur_msgs == get_max_msgs():
        return True
    return False


def reset_stats(discord_id):
    db.update_user(discord_id, lvl = 1, exp = 0, msg_count = 0)
    print(f"Reset user: {discord_id} stats.")


def set_exp(discord_id, xp):
    '''Sets a user's experience points.'''
    db.update_user(discord_id, exp = xp)


def set_level(discord_id, level):
    '''Set a user's level.'''
    db.update_user(discord_id, lvl = level)


def set_msg_count(discord_id, msgs):
    db.update_user(discord_id, msg_count = msgs)
