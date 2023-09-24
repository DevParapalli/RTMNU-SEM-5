#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ARR_LEN 20

char * lcsAlgo(char * S1, char * S2) {
    int s1_len = strlen(S1);
    int s2_len = strlen(S2);

    int LCS_table[MAX_ARR_LEN][MAX_ARR_LEN];

    for (int i = 0; i <= s1_len; i++) {
        LCS_table[i][0] = 0;
    }
    for (int i = 0; i <= s2_len; i++) {
        LCS_table[0][i] = 0;
    }

    for (int i = 1; i <= s1_len; i++) {
        for (int j = 1; j <= s2_len; j++) {
            if (S1[i - 1] == S2[j - 1]) {
                LCS_table[i][j] = LCS_table[i - 1][j - 1] + 1;
            } else if (LCS_table[i - 1][j] >= LCS_table[i][j - 1]) {
                LCS_table[i][j] = LCS_table[i - 1][j];
            } else {
                LCS_table[i][j] = LCS_table[i][j - 1];
            }
        }
    }

    int index = LCS_table[s1_len][s2_len];
    char * lcsOutput;
    lcsOutput = (char*)malloc((index + 1) * sizeof(char));
    lcsOutput[index] = '\0';

    int i = s1_len, j = s2_len;
    while (i > 0 && j > 0) {
        if (S1[i - 1] == S2[j - 1]) {
            lcsOutput[index - 1] = S1[i - 1];
            i--;
            j--;
            index--;
        }

        else if (LCS_table[i - 1][j] > LCS_table[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }

    return lcsOutput;
}

int main() {
    char *S1 = "Sunflower", *S2 = "Rainbow";
    char* output = lcsAlgo(S1, S2);
    printf("S1 : %s \nS2 : %s \nLCS: %s\n", S1, S2, output);
}