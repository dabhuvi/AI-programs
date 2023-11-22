
on_floor(monkey).
on_ceiling(banana).
at(door, monkey).
at(chair, room_left).
can_reach(monkey, banana) :- on_floor(monkey), at(chair, room_left), at(door, monkey).

can_reach(chair, banana) :- at(chair, room_left), at(door, monkey).

can_reach(monkey, banana) :- at(chair, room_left), at(door, room_left).
on_chair(monkey) :- can_reach(monkey, banana).

at(chair, room_right) :- can_reach(chair, banana).

at(chair, room_right) :- can_reach(monkey, banana).


goal_state :- on_chair(monkey), at(chair, room_right), can_reach(monkey, banana).
search(State) :- goal_state, write('Monkey got the banana!'), nl.
search(State) :-
    can_reach(Agent, Object),
    apply_action(Agent, Object, NewState),
    write('Executing action: '), write(Agent), write(' moves '), write(Object), nl,
    search(NewState).
apply_action(monkey, banana, NewState) :-
    on_chair(monkey),
    at(chair, room_right),
    write('Monkey climbs onto the chair and reaches the banana.'), nl,
    NewState = goal_state.
apply_action(monkey, chair, NewState) :-
    at(chair, room_left),
    write('Monkey pushes the chair to the right.'), nl,
    NewState = on_chair(monkey).
apply_action(monkey, banana, NewState) :-
    at(chair, room_left),
    write('Monkey moves the chair to the right.'), nl,
    NewState = at(chair, room_right).
