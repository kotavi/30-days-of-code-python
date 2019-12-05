class Printer:

    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No more jobs to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_pages()
        if job.check_complete():
            return "Printing complete"
        else:
            return "An error occured"
