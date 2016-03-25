r = 2**(1/12)
a = 440

scale_temp = [a / r**9, a / r**7, a / r**5, a / r**4, a / r**2,
              a, a * r**2, a * r**3]
scale_pure = [3/5 * a, 3/5 * a * 9/8, 3/5 * a * 5/4,  3/5 * a * 4/3,  3/5 * a * 3/2,
              a, 3/5 * a * 15/8, 3/5 * a * 2]

playTone(scale_temp, 1000)
playTone(scale_pure, 1000)

playTone(scale_temp, 1000, block = False)
playTone(scale_pure, 1000)