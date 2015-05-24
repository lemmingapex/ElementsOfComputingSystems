// from SimpleAdd.vm
// push 7 onto the stack
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 8 onto the stack
@8
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
