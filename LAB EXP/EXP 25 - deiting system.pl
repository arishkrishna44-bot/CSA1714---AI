% Facts
avoid(diabetes, sugar).
avoid(diabetes, sweets).
avoid(blood_pressure, salt).
avoid(blood_pressure, pickle).
avoid(obesity, junk_food).
avoid(obesity, oily_food).

recommend(diabetes, vegetables).
recommend(diabetes, whole_grains).
recommend(blood_pressure, fruits).
recommend(blood_pressure, vegetables).
recommend(obesity, fruits).
recommend(obesity, vegetables).

% Rules
diet(Disease, Food) :-
    recommend(Disease, Food).

avoid_food(Disease, Food) :-
    avoid(Disease, Food).