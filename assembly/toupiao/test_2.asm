        ORG 0000H
        AJMP START
        ORG 0003H;      INT0中断
        LJMP KEY_INT
        ORG 0100H
START:  MOV SP, #60H
        CRL IT0;   INT0低电平
        MOV IP, #01H;   INT0高优先级
        SETB EA;        总中断允许
        SETB EX0;       INT0中断允许
        MOV P1, 0FFH;   设置P1口为输入状态
        MOV R1, #80H;   当前打分位数
        MOV R0, #05H;    完全打完分数之后的数字等数量
        MOV R4, #00H

LOOP:   CJNE R1, #04H, LOOP
LOOP1:  MOV A, R4
        DA A

        MOV R5, #00H
        SWAP A
        XCHD A, R5
        MOV R3, A;  暂存A
        MOV A, #08H
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, R5
        MOVC A, @A+DPTR
        MOV P0, A
        MOV A, R3

        MOV R5, #00H
        SWAP A
        XCHD A, R5
        MOV A, #08H
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, R5
        MOVC A, @A+DPTR
        MOV P0, A
        AJMP LOOP1

        ORG 0300H
KEY_INT:MOV A, P1
        CPL A
        JZ RETURN;  A中内容为0，无键闭合，返回
        LCALL D10ms;    软件去抖
        MOV A, P1
        CPL A
        JZ RETURN
        JB ACC.0, Pkey0
        JB ACC.1, Pkey1
        JB ACC.2, Pkey2
        JB ACC.3, Pkey3
        JB ACC.4, Pkey4
        JB ACC.5, Pkey5
        JB ACC.6, Pkey6
        JB ACC.7, Pkey7
        LJMP RETURN
Pkey0:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #01H
        ADD A, R4
        MOV R4, A
        MOV A, #00H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey1:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #01H
        ADD A, R4
        MOV R4, A
        MOV A, #02H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey2:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #03H
        ADD A, R4
        MOV R4, A
        MOV A, #02H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey3:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #04H
        ADD A, R4
        MOV R4, A
        MOV A, #03H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey4:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #05H
        ADD A, R4
        MOV R4, A
        MOV A, #04H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey5:  MOV A, R1
        RL A
        MOV R1, A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #06H
        ADD A, R4
        MOV R4, A
        MOV A, #05H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey6:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #07H
        ADD A, R4
        MOV R4, A
        MOV A, #06H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN
Pkey7:  MOV A, R1
        RL A
        MOV R1, A
        MOV P2, A
        MOV DPTR, #TAB
        MOV A, #08H
        ADD A, R4
        MOV R4, A
        MOV A, #07H
        MOVC A, @A+DPTR
        MOV P0, A
        LJMP RETURN

RETURN: RETI

D10ms:  MOV R7, #25
D1:     MOV R6, #200
        DJNZ R6, $
        DJNZ R7, D1
        RET

TAB:    DB 0F9H, 0A4H, 0B0H, 99H, 92H, 82H, 0F8H, 80H, 90H
        END
