#include <stdio.h>

struct Masina {
    char model[50];
    int an;
    float pret;
};

int main() {
    struct Masina masina1;
    
    snprintf(masina1.model, sizeof(masina1.model), "%s", "BMW Seria 3");
    masina1.an = 2022;
    masina1.pret = 35000.50;
    
    printf("Model: %s\n", masina1.model);
    printf("An: %d\n", masina1.an);
    printf("Pret: %.2f\n", masina1.pret);
    
    return 0;
}
