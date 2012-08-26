// from BasicTest.vm
// push 10 onto the stack
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto LCL[0]
@LCL
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
// push 21 onto the stack
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 22 onto the stack
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto ARG[2]
@ARG
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
// pop off the stack onto ARG[1]
@ARG
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
// push 36 onto the stack
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto THIS[6]
@THIS
D=M
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push 42 onto the stack
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 45 onto the stack
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto THAT[5]
@THAT
D=M
@5
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
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
// push 510 onto the stack
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto 5 + 6
@5
D=A
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
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
// push THAT[5] onto the stack
@THAT
D=M
@5
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
// push THIS[6] onto the stack
@THIS
D=M
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS[6] onto the stack
@THIS
D=M
@6
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
// sub
@SP
AM=M-1
D=M
@SP
A=M-1
M=M-D
// push 5[6] onto the stack
@5
D=A
@6
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
