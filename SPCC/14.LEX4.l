%{
#include <stdio.h>
%}

%%

"int"           printf("INT\n");
"float"         printf("FLOAT\n");
"double"        printf("DOUBLE\n");
"char"          printf("CHAR\n");
"if"            printf("IF\n");
"else"          printf("ELSE\n");
"while"         printf("WHILE\n");
"do"            printf("DO\n");
"for"           printf("FOR\n");
[0-9]+          printf("NUMBER(%s)\n", yytext);
[a-zA-Z_][a-zA-Z0-9_]*  printf("IDENTIFIER(%s)\n", yytext);
[ \t\n]         ; /* ignore whitespace */
.               printf("INVALID_CHARACTER(%c)\n", *yytext);

%%

int main()
{
    yylex();
    return 0;
}
