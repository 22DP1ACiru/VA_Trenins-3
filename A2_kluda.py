# ----------------------------------------------------------------------
# A2. Salīdzinājums
# ----------------------------------------------------------------------

# Jāatrod lielākais skaitlis. Izvadās nulle.
#
# Salabo vienu rindu, lai programma strādātu pareizi. Tad palaid ar F5.

skaitli = [3, 9, 7]
lielakais = 0

for s in skaitli:
    if s < lielakais:
        lielakais = s

print(lielakais)
