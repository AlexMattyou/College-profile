ORG 0000H

; ADDITION
MOV A, #20H
ADD A, #21H
MOV 40H, A      ; Store result in memory location 40H

; SUBTRACTION
MOV A, #20H
CLR C
SUBB A, #18H
MOV 41H, A      ; Store result in memory location 41H

; MULTIPLICATION
MOV A, #03H
MOV B, #04H
MUL AB
MOV 42H, A      ; Result lower byte
MOV 43H, B      ; Result higher byte

; DIVISION
MOV A, #95H
MOV B, #10H
DIV AB
MOV 44H, A      ; Quotient
MOV 45H, B      ; Remainder

END
