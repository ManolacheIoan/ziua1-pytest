#include <stdio.h>

int main() {
    int numar = 10;
    int *pointer_catre_numar = &numar;
    
    printf("Valoarea lui numar: %d\n", numar);
    printf("Adresa lui numar: %p\n", &numar);
    printf("Valoarea din pointer: %d\n", *pointer_catre_numar);
    
    *pointer_catre_numar = 20;
    printf("Valoarea lui numar dupa modificare: %d\n", numar);
    
    return 0;
}
