// bootstrap
@256
D=A
@SP
M=D
// Sys.init 
// call
// push return-Sys.init-0
@return-Sys.init-0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// repostion LCL
@SP
D=M
@LCL
M=D

// repostion ARG
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D

// goto Sys.init
@Sys.init
0;JMP

(return-Sys.init-0)
// end Sys.init
// from Main.vm
// function
(Main.fibonacci)

@0
D=A
@R13
M=D

(Main.fibonacciLOOP)
@R13
D=M
@Main.fibonacciEND
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

@Main.fibonacciLOOP
0;JMP
(Main.fibonacciEND)
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
// lt
@SP
AM=M-1
D=M
@SP
A=M-1
A=M
D=D-A
@TRUE0
D;JGT
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
// if-goto Main.fibonacci$IF_TRUE
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE
// goto
@Main.fibonacci$IF_FALSE
0;JMP
// label Main.fibonacci$IF_TRUE
(Main.fibonacci$IF_TRUE)
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
// label Main.fibonacci$IF_FALSE
(Main.fibonacci$IF_FALSE)
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
// call
// push return-Main.fibonacci-1
@return-Main.fibonacci-1
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// repostion LCL
@SP
D=M
@LCL
M=D

// repostion ARG
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D

// goto Main.fibonacci
@Main.fibonacci
0;JMP

(return-Main.fibonacci-1)
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
// call
// push return-Main.fibonacci-2
@return-Main.fibonacci-2
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// repostion LCL
@SP
D=M
@LCL
M=D

// repostion ARG
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D

// goto Main.fibonacci
@Main.fibonacci
0;JMP

(return-Main.fibonacci-2)
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
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
// from Sys.vm
// function
(Sys.init)

@0
D=A
@R13
M=D

(Sys.initLOOP)
@R13
D=M
@Sys.initEND
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

@Sys.initLOOP
0;JMP
(Sys.initEND)
// push 4 onto the stack
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call
// push return-Main.fibonacci-3
@return-Main.fibonacci-3
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// repostion LCL
@SP
D=M
@LCL
M=D

// repostion ARG
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D

// goto Main.fibonacci
@Main.fibonacci
0;JMP

(return-Main.fibonacci-3)
// label Sys.init$WHILE
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
