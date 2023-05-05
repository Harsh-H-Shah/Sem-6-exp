%{
#include <stdio.h>
int line_count = 0, word_count = 0, char_count = 0;
%}

%%

\n  line_count++;
[a-zA-Z]+   { word_count++; char_count += strlen(yytext); }
.   char_count++;

%%

int main()
{
    yylex();
    printf("Number of lines: %d\n", line_count);
    printf("Number of words: %d\n", word_count);
    printf("Number of characters: %d\n", char_count);
    return 0;
}
