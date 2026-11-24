
% Connected cities
connected(chennai, bangalore).
connected(chennai, hyderabad).
connected(bangalore, mumbai).
connected(hyderabad, delhi).
connected(mumbai, pune).
connected(delhi, jaipur).

% Find a path between two cities
path(Start, Goal) :-
    travel(Start, Goal, [Start]).

% Destination reached
travel(Goal, Goal, Visited) :-
    reverse(Visited, Path),
    write(Path).

% Search for the next connected city
travel(Current, Goal, Visited) :-
    connected(Current, Next),
    \+ member(Next, Visited),
    travel(Next, Goal, [Next|Visited]).
