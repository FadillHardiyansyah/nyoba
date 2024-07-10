import pandas as pd

class MCG:
    def __init__(self, seed, a, m):
        self.seed = seed
        self.a = a
        self.m = m
        self.state = seed

    def next(self):
        self.state = (self.a * self.state) % self.m
        return self.state

# Meminta input dari pengguna
seed = int(input("Masukkan nilai seed: "))
a = int(input("Masukkan nilai a: "))
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan jumlah angka acak yang diinginkan: "))

# Buat instance dari MCG
mcg = MCG(seed, a, m)

# Generate angka acak dan simpan dalam daftar
data = []
previous_state = seed

for i in range(1, n + 1):
    zi = mcg.next()
    ui = zi / m
    X100 = round(100 * ui)
    data.append([i, previous_state, zi, ui, X100])
    previous_state = zi

# Membuat tabel dengan pandas
df = pd.DataFrame(data, columns=["i", "zi-1", "zi", "ui", "X100"])
print(df)
