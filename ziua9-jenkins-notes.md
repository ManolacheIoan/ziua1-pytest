# Ziua 9 - CI/CD cu Jenkins

## Ce am facut
- Instalat Jenkins local prin Docker
- Creat un pipeline cu 3 etape: Checkout (din GitHub), Install
  dependencies (pip), Run tests (pytest)
- Debugat probleme reale de mediu:
  - Python lipsea din container -> instalat cu apt-get
  - pip blocat de "externally-managed-environment" -> rezolvat
    cu --break-system-packages
  - pytest instalat dar nu in PATH -> rulat cu calea completa

## Concepte cheie
- Pipeline: succesiune de etape (stages) definite in cod
- Fiecare etapa poate esua independent, oprind restul pipeline-ului
- Mediile izolate (containere) nu au acces automat la ce ai
  instalat pe laptopul propriu
