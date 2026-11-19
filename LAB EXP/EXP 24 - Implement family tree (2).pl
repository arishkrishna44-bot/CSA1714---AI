
% Family Tree Program

% Facts
male(ram).
male(raj).
male(kumar).
male(arun).

female(sita).
female(gita).
female(priya).

% Parent Relationships
parent(ram, raj).
parent(sita, raj).

parent(ram, gita).
parent(sita, gita).

parent(raj, kumar).
parent(priya, kumar).

parent(raj, arun).
parent(priya, arun).

% Rules
father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandfather(X, Y) :-
    father(X, Z),
    parent(Z, Y).
