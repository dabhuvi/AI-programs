
diet_suggestion(high_blood_pressure, 'Low-sodium diet').
diet_suggestion(diabetes, 'Low-carbohydrate diet').
diet_suggestion(high_cholesterol, 'Low-fat diet').

suggest_diet(Person, Disease, Diet) :-
    has_disease(Person, Disease),
    diet_suggestion(Disease, Diet).


has_disease(john, high_blood_pressure).
has_disease(susan, diabetes).
has_disease(mike, high_cholesterol).
has_disease(lisa, high_blood_pressure).
has_disease(lisa, diabetes).

