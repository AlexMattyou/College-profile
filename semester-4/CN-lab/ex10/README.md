Algorithm:
CRC Generation:

Generate the CRC by performing polynomial division on the input bitstring using the specified polynomial.
Pad the input bitstring with zeros to match the length of the polynomial.

CRC Check:

Perform the same polynomial division on the received bitstring (including the CRC) to check for errors.
If the remainder is zero, no errors are detected. Otherwise, errors are present.

Main Function:

Define the input bitstring and polynomial.
Generate the CRC and print it.
Simulate error detection by checking the received CRC against the original CRC. 