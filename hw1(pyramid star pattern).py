def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


# Satır sayısını belirlemek için bir değişken oluşturun
rows = 5
print_pyramid(rows)
