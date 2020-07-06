import utils.database.methods as methods
import utils.database.config as config

metadata = config.get_metadata()
engine = config.get_engine()
connection = config.get_connection()
db = methods.Methods(engine, metadata, connection)

exp_mod = 1   # experience point modifier; progession speed through the system
exp_gain = 10   # experience points gained per message

# Defines the message requirements for each level. Each level is represented
# by an element in the array. 10 levels in each row of the list.
msg_list = [
        5, 5, 10, 10, 10, 20, 20, 20, 20, 20,
        20, 20, 20, 30, 30, 30, 30, 30, 30, 30,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
        50, 50, 50, 60, 60, 60, 60, 60, 60, 60,
        70, 70, 70, 80, 80, 80, 80, 90, 90, 90,
        100, 100, 100, 100, 200, 200, 200, 200, 200, 200,
        250, 250, 250, 250, 250, 250, 250, 250, 250, 250,
        500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
        1000, 1000, 1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000
    ]

# Generates the experience requirements for each level. Takes the exp_gain
# per message and the exp_mod and multiples it by each element in the message
# requirements list.
exp_list = [i * exp_gain * exp_mod for i in msg_list]

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


def add_experience(discord_id, exp):
    '''Update user experience value in database.'''
    if exp < max_exp:
        exp = exp + exp_gain * exp_mod
    elif exp > max_exp:
        exp = max_exp
    elif exp == max_exp:
        return
    db.update_user(discord_id, exp = exp)


def level_up(level):
    if level < max_level: 
        level = level + 1
        db.update_user(discord_id, lvl = level)


def ready_to_level(level, exp):
    '''
    Checks if the user has met the experience requirements for the next level.
    '''
    if exp >= exp_req[level-1]:
        return True
    return False


def reset_stats():
    pass


def reset_exp():
    '''Resets experience back to 0.'''
    db.update_user(discord_id, exp = 0)


def reset_level():
    '''Resets level back to 0.'''
    db.update_user(discord_id, lvl = 0)


def max_exp():
    '''Returns maxiumum experience required to hit level 100.'''
    exp = sum(exp_list)
    return exp


def max_msgs():
    '''Returns maximum messages required to hit level 100.'''
    msgs = sum(msg_list)
    return msgs
