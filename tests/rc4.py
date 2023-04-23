_SIZE = 256

g_key = ''.join([str(i % 10) for i in range(256)])


def create_table(key):
    table = []
    for i in range(_SIZE):
        table.append(i)
    
    n = len(key) // _SIZE
    key_list = [key[i:i+n] for i in range(0, len(key), n)]

    j = 0
    for i in range(_SIZE):
        j = (j + table[i] + int(key_list[i])) % _SIZE
        tmp = table[i]
        table[i] = table[j]
        table[j] = tmp

    return table


def rc4_run(steps, table):
    q1 = 0
    q2 = 0
    out = []

    for i in range(steps):
        q1 = (q1 + 1) % _SIZE
        q2 = (q2 + table[q1]) % _SIZE
        out.append((table[q1] + table[q2]) % _SIZE)
        tmp = table[q1]
        table[q1] = table[q2]
        table[q2] = tmp 

    return out



def rc4(data):
    table = create_table(g_key)
    out_key = rc4_run(_SIZE, table)
    coded_out = b''
    decoded_out = b''
    for i in range(len(data)):
        coded_out += (data[i] ^ out_key[i % len(out_key)]).to_bytes(1, 'big')

    print(f"coded: {coded_out}")

    for i in range(len(coded_out)):
        decoded_out += (coded_out[i] ^ out_key[i % len(out_key)]).to_bytes(1, 'big')

    print(f"decoded: {decoded_out}")


if __name__ == "__main__":
    rc4(b'hello world')
