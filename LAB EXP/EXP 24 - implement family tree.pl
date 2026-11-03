% Facts
male(john).
male(peter).
male(sam).

female(mary).
female(lisa).

parent(john, peter).
parent(mary, peter).
parent(john, sam).
parent(mary, sam).
parent(peter, lisa).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.