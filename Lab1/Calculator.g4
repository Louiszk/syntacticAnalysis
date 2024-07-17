grammar Calculator;

exp : term exp_ ;
term : factor term_ ;
factor : literal | '(' exp ')' ;
literal : NUMBER ;
exp_ : '+' exp | ;
term_ : '*' term | ;
NUMBER : DIGIT+ ;
WS : [ \t\r\n]+ -> skip ;
fragment DIGIT : [0-9] ;