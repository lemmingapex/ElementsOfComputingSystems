// from PointerTest.vm
// push 3030 onto the stack
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto 3 + 0
@3
D=A
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
// push 3040 onto the stack
@3040
D=A
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
// push 32 onto the stack
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto THIS[2]
@THIS
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
// push 46 onto the stack
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto THAT[6]
@THAT
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
// push 3[0] onto the stack
@3
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
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
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// push THIS[2] onto the stack
@THIS
D=M
@2
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
// push THAT[6] onto the stack
@THAT
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
