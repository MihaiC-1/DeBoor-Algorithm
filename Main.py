def citire_noduri(t):
    # Aici se citesc cele 9 noduri t0, t1, ... t8.
    for i in range(0, 9):
        print("Nodul ", i, " = ")
        d = int(input())
        t.append(d)


def citire_puncte_control(d_x, d_y):
    # Aici se citesc cordonatele punctelor de control iar cordonatele x se salveaza intr-o lisa iar cordonatele y se
    # salveaza in cealalta lista, in aceeasi ordine pentru a se extrage cum trebuie.
    for i in range(0, 5):
        print("Pentru punctul ", i + 1, " de control : ")
        x = int(input(" x = "))
        y = int(input(" y = "))
        d_x.append(x)
        d_y.append(y)


def functie_B_Spline_grad_0(t, i, a):
    # Calculul unei functii B-Spline de grad 0, unde a este acel t din t[i-1] <= t < t[i].
    if t[i - 1] <= a < t[i]:
        return 1
    else:
        return 0


def functie_B_Spline_grad_r(t, a, r, i):
    # Rezolvarea unei funtii B-Spline de grad r ce se rezolva recursiv. Deoarece gada r este 3 vom avea nevoie si de
    # functiile B-Spline de grad 2, 1 si 0. Formula este extrasa din cursul 8-10, pagina 21.
    if r - 1 == 0:
        return ((a - t[i - 1]) / (t[i + r - 1] - t[i - 1])) * functie_B_Spline_grad_0(t, i, a) + (
                    (t[i + r] - a) / (t[i + r] - t[i])) * \
               functie_B_Spline_grad_0(t, i, a)
    else:
        return ((a - t[i - 1]) / (t[i + r - 1] - t[i - 1])) * functie_B_Spline_grad_r(t, a, r - 1, i) + (
                    (t[i + r] - a) / (t[i + r] - t[i])) * \
               functie_B_Spline_grad_r(t, a, r - 1, i + 1)


def main():
    t = []
    d_x = []
    d_y = []
    citire_noduri(t)
    citire_puncte_control(d_x, d_y)

    suma = (0, 0)
    index_t = t[3]

    # Determinarea fiecarui r(t) pentr t intre t[3] si t[5]. t este index_t.
    # Pentru acestea voi avea nevoie de functiile B-Spline e grad 3, deoarece am 5 puncte de control si 9 noduri.
    # Iar i = 1 .. 5, la fel de mult ca si numarul de puncte de control.

    while index_t <= t[5]:
        for i in range(1, 6):
            suma = (functie_B_Spline_grad_r(t, index_t, 3, i)*d_x[i-1] + suma[0],
                    functie_B_Spline_grad_r(t, index_t, 3, i)*d_y[i-1] + suma[1])
        print("Pentru t = ", index_t, "avem r(t) = ", suma)
        index_t += 1


main()
