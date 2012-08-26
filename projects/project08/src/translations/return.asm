// return
@LCL
D=M
@R13
M=D // R13 = FRAME = *LCL

@R13
D=M
@5
A=D-A
D=M
@R14
M=D // store return address in R14

@SP
A=M-1
D=M

@ARG
A=M
M=D // *ARG = pop()

@ARG
D=M
@SP
M=D+1 // SP = ARG + 1

@R13
AM=M-1
D=M
@THAT
M=D // THAT = FRAME - 1

@R13
AM=M-1
D=M
@THIS
M=D // THIS = FRAME - 2

@R13
AM=M-1
D=M
@ARG
M=D // ARG = FRAME - 3

@R13
AM=M-1
D=M
@LCL
M=D // LCL = FRAME - 4

@R14
A=M // A = RET = R14

// GOTO RET
0;JMP
