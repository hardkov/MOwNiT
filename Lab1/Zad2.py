from numpy import float32
import time

start_time = time.time()

val64 = 0.53125
val32 = float32(0.53125)
sum = float32(0)
err = float32(0)
y = float32(0)
tmp = float32(0)
list = [val32] * 10 ** 7

for i in range(len(list)):
    y = list[i] - err
    tmp = sum + y
    err = (tmp - sum) - y
    sum = tmp

print(time.time() - start_time)
sum64 = val64 * (10 ** 7)
print(sum64 - sum)

# błąd względny oraz bezwzględny wynosi 0 dla val32 = 0.53125
# błąd w sumowaniu wynika z tego, ze sum jest dużo większe w porównaniu do y
# zmienna err zawiera poprawke na niskie bity utracone podczas sumowania
# z racji takiej że tracona wartość liczby jest mała to 32bitowe err nie będzie miało problemu z przechowaniem go
# czas działania dla val32 = 0.53125 wynosi 11.154638290405273
