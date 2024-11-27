#Function to Sort a List of Tuples by the Second Element

def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])
