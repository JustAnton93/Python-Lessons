import sys


def salary(hours, stavka, reward):
    try:
        return (hours * stavka) + reward
    except TypeError:
        return


try:
    file, hours, stavka, reward = sys.argv
except:
    print("invalid")
    exit()
print(salary(int(hours), int(stavka), int(reward)))
