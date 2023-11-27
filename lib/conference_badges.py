def badge_maker(name):
    return f"Hello, my name is {name}."

speaker_name = "Elijah"
badge_message = badge_maker(speaker_name)
print(badge_message)  


def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(f"Hello, my name is {name}.")
    return badge_messages

speakers = ["John Doe", "Jane Smith", "Michael Jackson"]
badge_messages = batch_badge_creator(speakers)
for message in badge_messages:
    print(message)


def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names):
        room_number = index + 1  
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
    return room_assignments

speakers = ["John Doe", "Jane Smith", "Michael Jackson"]
room_assignments = assign_rooms(speakers)
for assignment in room_assignments:
    print(assignment)


def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge_message in badge_messages:
        print(badge_message)
    
    for room_assignment in room_assignments:
        print(room_assignment)

speakers = ["John Doe", "Jane Smith", "Michael Jackson"]
printer(speakers)