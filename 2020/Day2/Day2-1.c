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
        for (j=0; j<100; j++) {
            if (arr[j]==let) {
                count2 += 1;
            }
        }
        if (min <= count2 && max >= count2)
            count += 1;
    }
    printf ("%d\n", count);
    return 0;
}
