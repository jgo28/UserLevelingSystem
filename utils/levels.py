import utils.database.methods as methods
import utils.database.config as config

metadata = config.get_metadata()
engine = config.get_engine()
connection = config.get_connection()
db = methods.Methods(engine, metadata, connection)

max_level = 100
exp_mod = 1   # experience point modifier
exp_gain = 10   # experience points gained per message

# Defines the message requirements for each level. Each level is represented
# by an element in the array.
msg_list = [
        5, 5, 10, 10, 10, 20, 20, 20, 20, 20,
        20, 20, 20, 30, 30, 30, 30, 30, 30, 30,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
        50, 50, 50, 60, 60, 60, 60, 60, 60, 60,
        70, 70, 70, 80, 80, 80, 80, 90, 90, 90,
        90, 90, 100, 100, 100, 100, 200, 200, 200, 200,
        250, 250, 250, 250, 250, 250, 250, 250, 250, 250,
        500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
        1000, 1000, 1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000
    ]

# Generates the experience requirements for each level. Takes the exp_gain
# per message and the exp_mod and multiples it by each element in the message
# requirements list.
exp_list = [i * exp_gain * exp_mod for i in msg_list]


def add_experience(discord_id, exp):
    if exp < max_exp:
        exp = exp + exp_gain*exp_mod
        
        # db.update_user(discord_id, )


def level_up(level):
    if level < max_level: 
        level = level + 1
    return level


def reset_stats():
    pass


def reset_exp():
    '''
    Resets experience back to 0.
    '''
    exp = 0
    return exp


def reset_level():
    '''
    Resets level back to 0.
    '''
    level = 0
    return level


def max_exp():
    '''
    Returns maxiumum experience required to hit level 100
    '''
    exp = sum(exp_list)
    return exp


def max_msgs():
    '''
    Returns maximum messages required to hit level 100
    '''
    msgs = sum(msg_list)
    return msgs
