ORG 0000H

MOV R0, #95H     ; Load R0 with 0x95
MOV R1, #6FH     ; Load R1 with 0x6F

MOV A, R0        ; Move R0 to A
MOV 30H, A       ; Store R0’s value in memory 30H

MOV A, R1        ; Move R1 to A
MOV 31H, A       ; Store R1’s value in memory 31H

END
