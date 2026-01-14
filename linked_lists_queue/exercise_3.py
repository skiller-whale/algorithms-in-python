import random

VECTOR_DIM = 20

class User:
    def __init__(self):
        self.profile_vector = [random.random() for _ in range(VECTOR_DIM)]
        self.queue = []

    def add_to_queue(self, posts):
        self.queue.extend(posts)

    def has_requested_content(self):
        return random.random() < 0.1

    def show_top_posts(self, num_posts):
        for i in range(num_posts):
            post = self.queue.pop()
            print(f"Post content: {post.content}")


class Post:
    def __init__(self):
        self.content_vector = [random.random() for _ in range(VECTOR_DIM)]
        self.content = ["cat", "dog", "politics"][random.randint(0, 2)]

def get_new_posts():
    return [Post() for i in range(20)]

def get_priority(user, post):
    return sum([i * j for i, j in zip(user.profile_vector, post.content_vector)])

def serve_content(user):
    while True:
        new_posts = get_new_posts()
        user.add_to_queue(new_posts)

        if user.has_requested_content():
            user.show_top_posts(5)

user = User()
serve_content(user)