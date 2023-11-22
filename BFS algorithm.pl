
edge(a, b, 5).
edge(a, c, 2).
edge(b, d, 4).
edge(b, e, 10).
edge(c, f, 8).
edge(d, goal, 7).
edge(e, goal, 3).
edge(f, goal, 6).
heuristic(Node, Cost) :-
    goal(goal),
    edge(Node, goal, Cost).
best_first_search(Node, Path, Cost) :-
    best_first_search_helper([Node-Cost], [], Path, Cost).
best_first_search_helper([Node-Cost|_], _, [Node], Cost) :-
    goal(Node).
best_first_search_helper([Node-Cost|Rest], Visited, Path, TotalCost) :-
    findall(Child-NewCost,
            (edge(Node, Child, EdgeCost),
             \+ member(Child-_, Visited),
             NewCost is Cost + EdgeCost + heuristic(Child, H),
             asserta(visited(Child, NewCost)),
             asserta(queue(Child, NewCost)),
             retract(visited(Child, _))),
            Children),
    append(Children, Rest, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    best_first_search_helper(SortedQueue, [Node-Cost|Visited], Path, TotalCost).
sort_queue(Queue, SortedQueue) :-
    keysort(Queue, SortedQueue).
