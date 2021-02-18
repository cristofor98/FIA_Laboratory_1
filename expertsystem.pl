
go :- hypothesize(Tourist),
      write('I guess that the tourist is: '),
      write(Tourist),
      nl,
      undo.

/* hypotheses to be tested */
hypothesize(loonie)   :- loonie, !.
hypothesize(saturnian)     :- saturnian, !.
hypothesize(humane)   :- humane, !.
hypothesize(marsian)     :- marsian, !.
hypothesize(neptunian)   :- neptunian, !.
hypothesize(venusian)   :- venusian, !.
hypothesize(unknown).             

/* tourist identification rules */
loonie :- big body, 
          big head, 
           verify(has_tawny_color),
           verify(has_dark_spots).
saturnian :- big head,  
         long legs.
marsian :- normal body,
         big eyes.
neptunian :- ultrasonic ability,
           small nose  
           verify(has_long_neck).
venusian :- small nose, 
           antenna.

/* classification rules */
big body    :- verify(has purple skin), !.
big body    :- verify(has orange hair).
big head   :- verify(has long ears), !.
big head   :- verify(has four ears), 
long legs :- verify(has big shoes), !.
long legs :- verify(has jeans), 
normal body :- verify(has white skin), 
            verify(has two legs), !.
big eyes :- verify(has big fingers), !.
big eyes  :- verify(has red eyes), 
small nose :- verify(has blue eyes), !.
small nose  :- verify(has four hands), 
ultrasonic ability :- verify(has blue skin), !.
ultrasonic ability  :- verify(has blue eyes), 
antenna :- verify(has a long neck), !.
antenna :- verify(has four hands), 

/* how to ask questions */
ask(Question) :-
    write('Does the animal have the following attribute: '),
    write(Question),
    write('? '),
    read(Response),
    nl,
    ( (Response == yes ; Response == y)
      ->
       assert(yes(Question)) ;
       assert(no(Question)), fail).

:- dynamic yes/1,no/1.

/* How to verify something */
verify(S) :-
   (yes(S) 
    ->
    true ;
    (no(S)
     ->
     fail ;
     ask(S))).

/* undo all yes/no assertions */
undo :- retract(yes(_)),fail. 
undo :- retract(no(_)),fail.
undo.
