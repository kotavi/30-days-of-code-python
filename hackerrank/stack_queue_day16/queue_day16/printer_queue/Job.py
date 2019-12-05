import random
class Job:

    def __init__(self):
        self.pages = random.randrange(1, 11)

    def __repr__(self):
        return "Job object({} pages)".format(self.pages)

    def print_pages(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        return self.pages == 0

