#include <stdio.h>

int aduna(int a, int b) {
    return a + b;
}

void afiseaza_mesaj(char mesaj[]) {
    printf("%s\n", mesaj);
}

int main() {
    int rezultat = aduna(5, 3);
    printf("Rezultat: %d\n", rezultat);
    
    afiseaza_mesaj("Salut din C!");
    
    return 0;
}
