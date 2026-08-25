# Ziua 8 - HiL Testing concepte

## Ce e HiL
Hardware-in-the-Loop: un ECU real este conectat la un simulator
care imita restul masinii (senzori, motor, roti), fara sa fie
nevoie de masina completa asamblata.

## Niveluri de testare in auto
1. Unit testing - functii izolate de cod
2. SiL (Software-in-the-Loop) - tot simulat, fara hardware
3. HiL (Hardware-in-the-Loop) - ECU real, restul simulat
4. Vehicle testing - masina completa, reala

## Termeni cheie
- ECU: Electronic Control Unit
- dSPACE / Vector CANoe: unelte comerciale pentru HiL
- Test bench: ansamblul fizic simulator + ECU
- Real-time simulation: simulatorul trebuie sa raspunda la fel
  de rapid ca hardware-ul real

## Legatura cu ce am invatat deja
HiL foloseste tot CAN bus pentru comunicare intre simulator si ECU,
similar cu python-can, doar ca un capat e hardware real, nu VirtualBus.
