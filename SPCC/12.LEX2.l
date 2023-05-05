%{
#include <stdio.h>
%}

%%

[0-9]+      printf("%s is a number.\n", yytext);
[a-zA-Z]+   printf("%s is a word.\n", yytext);
[0-9a-zA-Z]+    printf("%s is a combination of word and number.\n", yytext);
.           printf("%s is not a valid input.\n", yytext);

%%

int main()
{
    yylex();
    return 0;
}