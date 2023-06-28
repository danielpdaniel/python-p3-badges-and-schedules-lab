def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    names_list = [badge_maker(name) for name in names]
    # for name in names:
    #     badge_text = badge_maker(name)
    #     names_list.append(badge_text)
    return names_list


def assign_rooms(names):
    rooms_list = [f"Hello, {names[n -1]}! You'll be assigned to room {n}!" for n in range(1,9)]
    # for n in range(1,9):
    #     rooms_list.append(f"Hello, {names[n -1]}! You'll be assigned to room {n}!")
    return rooms_list


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
    
