#include <stdio.h>

int main(){
    int t; // 테스트 케이스
    int n; // 국가 수
    int m; // 비행기 수

    int a, b; // 비행기가 왕복하는 국가 쌍

    scanf("%d", &t);

    while(t--){
        scanf("%d %d", &n, &m);
        for (int i=0; i < m; i++){
            scanf("%d %d", &a, &b);
        }
        printf("%d\n", n-1);
    }
}