// from FibonacciSeries.vm
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
// pop off the stack onto 3 + 1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push 0 onto the stack
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto THAT[0]
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push 1 onto the stack
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto THAT[1]
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
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
// push 2 onto the stack
@2
D=A
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
// pop off the stack onto ARG[0]
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// label Sys.init$MAIN_LOOP_START
(Sys.init$MAIN_LOOP_START)
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
// if-goto Sys.init$COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@Sys.init$COMPUTE_ELEMENT
D;JNE
// goto
@Sys.init$END_PROGRAM
0;JMP
// label Sys.init$COMPUTE_ELEMENT
(Sys.init$COMPUTE_ELEMENT)
// push THAT[0] onto the stack
@THAT
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT[1] onto the stack
@THAT
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
// pop off the stack onto THAT[2]
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push 3[1] onto the stack
@3
D=A
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push 1 onto the stack
@1
D=A
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
// pop off the stack onto 3 + 1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
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
// push 1 onto the stack
@1
D=A
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
// pop off the stack onto ARG[0]
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// goto
@Sys.init$MAIN_LOOP_START
0;JMP
// label Sys.init$END_PROGRAM
(Sys.init$END_PROGRAM)
