        ORG 0000H
        AJMP MAIN
        ORG 0100H
MAIN:   MOV A, #11H
        MOV P1, A
        LCALL D3s
        MOV A, #21H
        MOV P1, A
        MOV R1, #01H;   R1是数码管选择位数
        MOV A, R1
        LCALL D30s

        MOV A, #0AH
        MOV P1, A
        LCALL D3s
        MOV A, #0CH
        MOV P1, A
        MOV R1, #04H
        MOV A, R1
        LCALL D30s
        AJMP MAIN

        ORG 0200H
D3s:    MOV R5, #20
DEL30:  MOV R6, #100
DEL31:  MOV R7, #100
        DJNZ R7, $
        DJNZ R6, DEL31
        DJNZ R5, DEL30
        RET
        ORG 0300H
D30s:   MOV R0, #01FH;   TAB选择
NEXT:   MOV R4, #100
INPUT:  MOV A, #0FFH
        MOV P0, A
        MOV A, R0
        ADD A, R0
        MOV R3, A
        MOV A, R1
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, R3
        DEC R3
        MOVC A, @A+DPTR
        MOV P0, A
DELAY0: MOV R5, #10
DEL0:   MOV R6, #20
DEL1:   MOV R7, #20
DEL2:   DJNZ R7, DEL2
        DJNZ R6, DEL1
        DJNZ R5, DEL0
		MOV A, #0FFH
        MOV P0, A
        MOV A, R1
        RL A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, R3
        DEC R3
        MOVC A, @A+DPTR
        MOV P0, A
DELAY1: MOV R5, #10
DEL10:  MOV R6, #20
DEL11:  MOV R7, #20
DEL12:  DJNZ R7, DEL12
        DJNZ R6, DEL11
        DJNZ R5, DEL10

        DJNZ R4, INPUT
        DJNZ R0, NEXT
        RET

TAB:    DB 	 0C0H,0C0H,0C0H,0F9H,0C0H,0A4H,0C0H,0B0H,0C0H,099H,0C0H,092H,0C0H,082H,0C0H,0F8H,0C0H,080H,0C0H,090H,0C0H,0C0H,0F9H,0F9H,0F9H,0A4H,0F9H,0B0H,0F9H,099H,0F9H,092H,0F9H,082H,0F9H,0F8H,0F9H,080H,0F9H,090H,0F9H,0C0H,0A4H,0F9H,0A4H,0A4H,0A4H,0B0H,0A4H,099H,0A4H,092H,0A4H,082H,0A4H,0F8H,0A4H,080H,0A4H,090H,0A4H,0C0H,0B0H

        END
