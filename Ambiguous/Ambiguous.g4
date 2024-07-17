grammar Ambiguous;

exp
    : exp '+' exp
    | exp '*' exp
    | '(' exp ')'
    | 'L'
    | 'I'
    ;

WS: [ \n\t\r]+ -> skip;