% Backward Chaining Program

fact(sunny).
fact(warm).
fact(holiday).

% Rules

can_go_outside :-
    fact(sunny),
    fact(warm).

can_play :-
    can_go_outside,
    fact(holiday).

can_swim :-
    fact(sunny),
    fact(warm).

% Backward Chaining Queries

backward_chaining(X) :-
    fact(X).

backward_chaining(X) :-
    call(X).