import names
import random
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def generate_full_name():
    return names.get_full_name()

def generate_first_name():
    return names.get_first_name()

def generate_last_name():
    return names.get_last_name()

with open('template.csv','w') as w:
    for line in range(100000):
        w.write("{},{},{},{}\n".format(line, generate_first_name(), generate_last_name() , generate_random_ip()))