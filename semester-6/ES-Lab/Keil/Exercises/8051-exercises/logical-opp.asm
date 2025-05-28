ORG 0000H

; AND Operation
MOV A, #25H       ; A = 0x25
MOV B, #12H       ; B = 0x12
ANL A, B          ; A = A AND B
MOV 30H, A        ; Store result in memory location 30H

; OR Operation
MOV A, #25H
MOV B, #15H
ORL A, B          ; A = A OR B
MOV 31H, A        ; Store result in memory location 31H

; XOR Operation
MOV A, #45H
MOV B, #67H
XRL A, B          ; A = A XOR B
MOV 32H, A        ; Store result in memory location 32H

; NOT Operation (Complement)
MOV A, #45H
CPL A             ; A = NOT A
MOV 33H, A        ; Store result in memory location 33H

END
