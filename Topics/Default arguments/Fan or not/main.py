def add_viewer(name, fan_list=None):
    if fan_list != None:
        fan_list.append(name)
        return fan_list
    else:
        return [name]
