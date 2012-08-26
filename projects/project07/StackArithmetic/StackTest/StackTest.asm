// from StackTest.vm
// push 17 onto the stack
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 17 onto the stack
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
@SP
A=M-1
A=M
D=D-A
@TRUE0
D;JEQ
(FALSE0)
@SP
A=M-1
M=0
@EXIT0
0;JMP
(TRUE0)
@SP
A=M-1
M=-1
(EXIT0)
// push 892 onto the stack
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 891 onto the stack
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
AM=M-1
D=M
@SP
A=M-1
A=M
D=D-A
@TRUE1
D;JGE
(FALSE1)
@SP
A=M-1
M=0
@EXIT1
0;JMP
(TRUE1)
@SP
A=M-1
M=-1
(EXIT1)
// push 32767 onto the stack
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 32766 onto the stack
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
@SP
A=M-1
A=M
D=D-A
@TRUE2
D;JLE
(FALSE2)
@SP
A=M-1
M=0
@EXIT2
0;JMP
(TRUE2)
@SP
A=M-1
M=-1
(EXIT2)
// push 56 onto the stack
@56
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 31 onto the stack
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 53 onto the stack
@53
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
// push 112 onto the stack
@112
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
// neg
@SP
A=M-1
M=-M
// and
@SP
AM=M-1
D=M
@SP
A=M-1
M=D&M
// push 82 onto the stack
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
AM=M-1
D=M
@SP
A=M-1
M=D|M
