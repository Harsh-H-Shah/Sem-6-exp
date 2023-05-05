%{
#include <stdio.h>
%}

%%

[aeiouAEIOU]    printf("%c is a vowel.\n", yytext[0]);
[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]   printf("%c is a consonant.\n", yytext[0]);
.   printf("%c is not a valid letter.\n", yytext[0]);

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();
    return 0;
}
