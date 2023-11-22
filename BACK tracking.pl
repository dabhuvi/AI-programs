
color(apple, red).
color(banana, yellow).
color(grape, purple).
color(orange, orange).
color(lemon, yellow).
fruit_color(Fruit, Color) :-
    color(Fruit, Color).
fruits_of_color(Color, Fruits) :-
    findall(Fruit, color(Fruit, Color), Fruits).
all_fruits(Fruits) :-
    findall(Fruit-Color, color(Fruit, Color), Fruits).


