
class UserInfo:
    def __init__(self, name, id, level, exp, msg_count):
        self.user = name
        self.id = id
        self.level = level
        self.exp = exp
        self.msg_count = msg_count

    def get_username(self):
        return self.user

    def get_discord_id(self):
        return self.discord_id

    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp

    def get_msg_count(self):
        return self.msg_count

    def set_username(self, name):
        self.user = name

    def set_discord_id(self, id):
        self.id = id

    def set_level(self, level):
        self.level = level

    def set_exp(self, exp):
        self.exp = exp

    def set_msg_count(self, msgs):
        self.msg_count = msgs

    def calc_exp(self):
        pass
