// from SimpleFunction.vm
// function
(SimpleFunction.test)

@2
D=A
@R13
M=D

(SimpleFunction.testLOOP)
@R13
D=M
@SimpleFunction.testEND
D;JEQ

@0
D=A
@SP
A=M
M=D
@SP
M=M+1

@R13
M=M-1

@SimpleFunction.testLOOP
0;JMP
(SimpleFunction.testEND)
// push LCL[0] onto the stack
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push LCL[1] onto the stack
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// not
@SP
A=M-1
M=!M
// push ARG[0] onto the stack
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// push ARG[1] onto the stack
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
@SP
A=M-1
M=M-D
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
