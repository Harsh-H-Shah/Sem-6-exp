%{
#include <stdio.h>
%}

%%

[a-zA-Z]+    printf("Hello %s\n", yytext);

%%

int main()
{
    printf("Enter your name: ");
    yylex();
    return 0;
}
