def can_i_get_off_work(boss_mood):
    print("Checking if I can get off work")
    return boss_mood == "good"

def can_i_get_someone_to_watch_the_ranch(are_animals_sick):
    print("Checking if I can get someone to watch the ranch")
    return not are_animals_sick

def can_i_get_resonable_tickets(are_tickets_expensive):
    print("Checking if I can get reasonable tickets")
    return not are_tickets_expensive

def can_i_go_to_san_fran(boss_mood, are_animals_sick, are_tickets_expensive):
    if can_i_get_off_work(boss_mood) and can_i_get_someone_to_watch_the_ranch(are_animals_sick) and can_i_get_resonable_tickets(are_tickets_expensive):
        print("I'm going to San Fran next week")
        print()
    else:
        print("I'm not going to San Fran next week")
        print()

can_i_go_to_san_fran("bad", True, True)
can_i_go_to_san_fran("good", True, False)
can_i_go_to_san_fran("good", False, True)
can_i_go_to_san_fran("good", False, False)

