% Forward Chaining Program

fact(sunny).
fact(warm).

rule(go_outside) :-
    fact(sunny),
    fact(warm).

rule(ice_cream) :-
    fact(sunny).

rule(swimming) :-
    fact(sunny),
    fact(warm).

% Forward Chaining

forward_chaining(X) :-
    fact(X).

forward_chaining(X) :-
    rule(X).