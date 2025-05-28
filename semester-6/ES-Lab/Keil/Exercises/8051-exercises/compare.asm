ORG 0000H       ; Starting address

MOV A, #25H     ; Load A with 0x25
MOV B, #30H     ; Load B with 0x30

CLR C           ; Clear carry flag before subtraction
SUBB A, B       ; A = A - B (A = 0x25 - 0x30)

JZ EQUAL        ; If result is zero, A == B
JC LESS_THAN    ; If carry is set, A < B
SJMP GREATER_THAN ; If no carry and not zero, A > B

EQUAL:
    MOV R0, #01H   ; Set R0 = 1 (equal)
    SJMP DONE

LESS_THAN:
    MOV R0, #02H   ; Set R0 = 2 (less than)
    SJMP DONE

GREATER_THAN:
    MOV R0, #03H   ; Set R0 = 3 (greater than)

DONE:
    END
