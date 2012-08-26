// from StaticTest.vm
// push 111 onto the stack
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 333 onto the stack
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 888 onto the stack
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop off the stack onto static
@SP
AM=M-1
D=M
@StaticTest.8
M=D
// pop off the stack onto static
@SP
AM=M-1
D=M
@StaticTest.3
M=D
// pop off the stack onto static
@SP
AM=M-1
D=M
@StaticTest.1
M=D
// push static StaticTest.3 onto the stack
@StaticTest.3
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static StaticTest.1 onto the stack
@StaticTest.1
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
// push static StaticTest.8 onto the stack
@StaticTest.8
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
