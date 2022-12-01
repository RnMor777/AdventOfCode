#include <stdio.h>

int main () {
    //variables
    FILE *fp = fopen("Day1.txt", "r");
    int arr[200];
    int i, j, k;
    
    //take in input
    for (i=0; i<200; i++) {
        fscanf(fp, "%d", &arr[i]);
    }

    //calculate answer
    for (i=0; i<200; i++) {
        for (j=i+1; j<200; j++) {
            for (k=j+1; k<200; k++) {
                if (arr[i]+arr[j]+arr[k]==2020) {
                    printf ("%d\n", arr[i]*arr[j]*arr[k]);
                    break;
                }
            }
        }
    }
    return 0;
}
