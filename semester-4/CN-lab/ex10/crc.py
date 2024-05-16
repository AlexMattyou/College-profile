def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    initial_padding = initial_filler * (len(polynomial_bitstring) - 1)
    input_padded = input_bitstring + initial_padding
    while len(input_padded) >= len(polynomial_bitstring):
        current_chunk = input_padded[0 : len(polynomial_bitstring)]
        input_padded = input_padded[len(polynomial_bitstring) : ]
        current_chunk = bin(int(current_chunk, 2) ^ int(polynomial_bitstring, 2))[2 : ].zfill(len(current_chunk))
        input_padded = current_chunk + input_padded
    return input_padded

def crc_check(input_bitstring, polynomial_bitstring, crc_check_bitstring):
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    crc_check_bitstring = crc_check_bitstring.lstrip('0')
    initial_padding = crc_check_bitstring + (len(polynomial_bitstring) - 1) * '0'
    return (crc_remainder(input_bitstring, polynomial_bitstring, '0') == initial_padding)

def main():
    input_bitstring = "1011101"
    polynomial_bitstring = "1101"
    crc = crc_remainder(input_bitstring, polynomial_bitstring, '0')
    print("CRC: ", crc)
    received_crc = "100"
    print("Error detected: ", crc_check(input_bitstring, polynomial_bitstring, received_crc))

if __name__ == "__main__":
    main()


'''
OUTPUT:

Enter data to be transmitted: 1001101
Enter the Generating polynomial: 1011
----------------------------------------
Data padded with n-1 zeros : 1001101000
----------------------------------------
CRC or Check value is : 101
----------------------------------------
Final data to be sent : 1001101101
----------------------------------------
Enter the received data: 1001101101
-----------------------------
Data received: 1001101101
No error detected



'''