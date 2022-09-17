#STUDENT 340
from queue import PriorityQueue

def add_value(dict_obj, key, value):
        ''' Adds a key-value pair to the dictionary.
        If the key already exists in the dictionary,
        it will associate multiple values with that
        key instead of overwritting its value'''
        if key not in dict_obj:
            q = PriorityQueue()
            dict_obj[key] = q
            dict_obj[key].put((-value[1],value[0]))
        else:
            dict_obj[key].put((-value[1],value[0]))
        

# get maximum for specific day
def get_max(dic, date):
    """

    :param dic: Dictionary from function above
    :param date: Date (string format: 'yyyy-mm-dd')
    :return: Sensory ID and value of the maximum measurement
    """
    value, id_ = dic[date].get()
    return "{0},{1}".format(id_, -value)
    
    

if __name__ == "__main__":
    input = input()
    input = input.split(";")
    requested_date = input[0]
    input.pop(0)
    data = []
    for d in input:
        date, id, value = d.split(',', 2)
        instance = (date, (int(id), int(value)))
        data.append(instance)

    # TODO: create empty dictionary and fill it.
    dic = {}
    for date, tup in data:
        add_value(dic, date, tup)

    print(get_max(dic, requested_date))
