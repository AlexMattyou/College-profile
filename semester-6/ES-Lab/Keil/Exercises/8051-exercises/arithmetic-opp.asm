ORG 0000H

; ADDITION
MOV A, #20H
ADD A, #21H
MOV P0, A      ; Store result in memory location 40H

; SUBTRACTION
MOV A, #20H
CLR C
SUBB A, #18H
MOV P0, A      ; Store result in memory location 41H

; MULTIPLICATION
MOV A, #03H
MOV B, #04H
MUL AB
MOV P0, A      ; Result lower byte
MOV P1, B      ; Result higher byte

; DIVISION
MOV A, #95H
MOV B, #10H
DIV AB
MOV P0, A      ; Quotient
MOV P1, B      ; Remainder

END
