import utils.database.methods as methods
import utils.database.config as config

metadata = config.get_metadata()
engine = config.get_engine()
connection = config.get_connection()
db = methods.Methods(engine, metadata, connection)

max_level = 100
exp_mod = 1   # experience point modifier
exp_req = [500]     # experience required for each level tier
exp_gain = 10   # experience points gained per message
max_exp = None


def gain_experience(exp)
    if exp < max_exp:
        exp = exp + exp_gain*exp_mod


def level_up(level):
    if level < max_level: 
        level = level + 1
    return level


def reset_stats():
    pass

def reset_exp():
    exp = 0
    return exp

def reset_level():
    level = 0
    return level