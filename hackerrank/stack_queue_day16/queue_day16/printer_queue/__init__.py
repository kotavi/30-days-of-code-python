from hackerrank.stack_queue_day16.queue_day16.printer_queue import Job
from hackerrank.stack_queue_day16.queue_day16.printer_queue import PrintQueue
from hackerrank.stack_queue_day16.queue_day16.printer_queue import Printer

if __name__ == '__main__':

    print_queue = PrintQueue()
    job1 = Job()
    print_queue.enqueue(job1)
    job2 = Job()
    print_queue.enqueue(job2)
    job3 = Job()
    print_queue.enqueue(job3)
    print(print_queue)

    printer = Printer()
    # printing the first job
    printer.get_job(print_queue)
    printer.print_job(printer.current_job)
    print(print_queue)
    # printing the second job
    printer.get_job(print_queue)
    printer.print_job(printer.current_job)
    print(print_queue)
    # printing the third job
    printer.get_job(print_queue)
    printer.print_job(printer.current_job)
    print(print_queue)
