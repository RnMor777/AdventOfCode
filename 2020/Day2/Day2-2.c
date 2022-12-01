#include <stdio.h>

int main () {
    //variables
    FILE *fp = fopen("Day2.txt", "r");
    int count=0;
    int count2=0;
    char arr[100];
    char let;
    int i, j, max, min;

    for (i=0; i<1000; i++) {
        for (j=0; j<100; j++)
            arr[j] = '\0';
        fscanf(fp, "%d-%d %c: %s", &min, &max, &let, arr);
        count2 = 0;
        if (arr[min-1] == let) 
            count2 += 1;
        if (arr[max-1] == let)
            count2 += 1;
        if (count2 == 1)
            count += 1;
    }
    printf ("%d\n", count);
    return 0;
}
