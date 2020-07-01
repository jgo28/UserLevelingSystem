
class UserDB:
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
