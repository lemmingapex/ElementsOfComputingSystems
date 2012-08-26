// from BasicLoop.vm
// push 0 onto the stack
@0
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
// label Sys.init$LOOP_START
(Sys.init$LOOP_START)
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
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// pop off the stack onto LCL[0	]
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
// if-goto Sys.init$LOOP_START
@SP
AM=M-1
D=M
@Sys.init$LOOP_START
D;JNE
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
