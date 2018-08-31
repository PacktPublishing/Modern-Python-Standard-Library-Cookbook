import multiprocessing

manager = multiprocessing.Manager()
namespace = manager.Namespace()
def set_first_variable():
    namespace.first = 42
p = multiprocessing.Process(target=set_first_variable)
p.start()
p.join()


def set_second_variable():
    namespace.second = dict(value=42)
p = multiprocessing.Process(target=set_second_variable)
p.start()
p.join()


import datetime
def set_custom_variable():
    namespace.last = datetime.datetime.utcnow()
p = multiprocessing.Process(target=set_custom_variable)
p.start()
p.join()



def print_variables():
   print(namespace.first, namespace.second, namespace.last)
p = multiprocessing.Process(target=print_variables)
p.start()
p.join()
