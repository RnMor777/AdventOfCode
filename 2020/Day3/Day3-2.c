#include <stdio.h>

int main () {
    //variables
    FILE *fp = fopen("Day3.txt", "r");
    char arr[500][32];
    int lines=0;
    int left1=0, left3=0, left5=0, left7=0, lefthalf=0;
    int k=0;
    long c1=0, c3=0, c5=0, c7=0, chalf=0;
    
    //take in input
    while (lines<323 && fscanf(fp, "%s", arr[lines])) {
        lines += 1;
    }

    //calculate answer
    for (k=0; k<lines; k++) {
        if (arr[k][left1]=='#') 
            c1+=1;;
        left1+=1;
        left1%=31;

        if (arr[k][left3]=='#') 
            c3+=1;;
        left3+=3;
        left3%=31;

        if (arr[k][left5]=='#') 
            c5+=1;;
        left5+=5;
        left5%=31;

        if (arr[k][left7]=='#') 
            c7+=1;;
        left7+=7;
        left7%=31;
    }
    for (k=0; k<lines; k+=2) {
        if (arr[k][lefthalf]=='#')
            chalf+=1;
        lefthalf+=1;
        lefthalf%=31;
    }
    printf("%ld\n", c1*c3*c5*c7*chalf); 
    return 0;
}
