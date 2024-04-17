from solver import *
from pwn import *

HOST = "165.232.161.196"
PORT = 4020
TOKEN = b"pk76xiPbP4"
N = 30


def main():
    conn = remote(HOST, PORT)
    conn.recvuntil(b"Masukkan token terlebih dahulu!")
    conn.sendline(TOKEN)

    for _ in range(N):
        conn.recvuntil(b"Tahap-")
        tahap = (conn.recvline().decode()).replace("-", "").strip()

        conn.recvuntil(b"paket_soal = ")
        type = conn.recv(1).decode().lower()
        conn.recvuntil(b"n = ")
        n = int(conn.recvline().decode())
        conn.recvuntil(b"e = ")
        e = int(conn.recvline().decode())
        conn.recvuntil(b"c = ")
        c = int(conn.recvline().decode())

        print("Tahap", tahap)
        print("Type:", type)
        print("n:", n)
        print("e:", e)
        print("c:", c)

        conn.recvuntil(b"Jawaban =")

        if type == "a":
            m = solve_a(n, e, c)
        elif type == "b":
            m = solve_b(n, e, c)
        elif type == "c":
            m = solve_c(n, e, c)
        elif type == "d":
            m = solve_d(n, e, c)
        elif type == "e":
            m = solve_e(n, e, c)
        else:
            raise Exception("[ERROR] Invalid type:", type)

        conn.sendline(bytes(m))
        result = conn.recvline().decode().strip()

        if not result.startswith("Uwaw keren"):
            raise Exception("[ERROR] Wrong Answer")

        print("Result:", m)
        print()

    conn.interactive()


main()
