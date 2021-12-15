class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        self.following += 1


user1 = User("001", "angela")
user2 = User("002", "jack")

user2.follow(user1)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
