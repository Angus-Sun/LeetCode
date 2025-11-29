1int is_palindrome_len(const char *st, int len) {
2    int i = 0, j = len - 1;
3    while (i < j) {
4        if (st[i] != st[j]) return 0;
5        i++; j--;
6    }
7    return 1;
8}
9
10char* longestPalindrome(char* s) {
11    int longest = 0;
12    char *compare = malloc(sizeof(char) * strlen(s) + 1);
13    char *new_str = malloc(sizeof(char) * strlen(s) + 1);
14    int n = strlen(s);
15    for (size_t i = 0; i < n; i++) {
16        if ((int)(n - i) <= longest) break;
17        int index = 0;
18        for (size_t j = i; j < n; j++) {
19            compare[index++] = s[j];
20            if (index > longest && is_palindrome_len(compare, index)) {
21                longest = index;
22                compare[index] = '\0';
23                strcpy(new_str, compare);
24            }
25        }
26    }
27    free(compare);
28    return new_str;
29}