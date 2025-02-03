//Vienna LaRose, Expressions Notes C
#include <stdio.h>
// integers int when we set the variable and %d when we print
// floats float when we set the variable and %f when we print
// strings (words) char when we set the variable and %s when we print
int mynum;
float percent;

int main(void){
    printf("Type a number: \n");
    scanf("%d", &mynum);
    printf("You inputed %d\n", mynum);
    printf("Give me a percent as a decimal: \n");
    scanf("%f", &percent);
    printf("Your percent is %f\n", percent);
    return 0;
}