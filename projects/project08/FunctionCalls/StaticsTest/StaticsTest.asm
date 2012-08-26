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
// from Class2.vm
// function
(Class2.set)

@0
D=A
@R13
M=D

(Class2.setLOOP)
@R13
D=M
@Class2.setEND
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

@Class2.setLOOP
0;JMP
(Class2.setEND)
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
// pop off the stack onto static
@SP
AM=M-1
D=M
@Class2.0
M=D
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
// pop off the stack onto static
@SP
AM=M-1
D=M
@Class2.1
M=D
// push 0 onto the stack
@0
D=A
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
// function
(Class2.get)

@0
D=A
@R13
M=D

(Class2.getLOOP)
@R13
D=M
@Class2.getEND
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

@Class2.getLOOP
0;JMP
(Class2.getEND)
// push static Class2.0 onto the stack
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static Class2.1 onto the stack
@Class2.1
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
// push 6 onto the stack
@6
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
// call
// push return-Class1.set-0
@return-Class1.set-0
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
@2
D=D-A
@5
D=D-A
@ARG
M=D

// goto Class1.set
@Class1.set
0;JMP

(return-Class1.set-0)
// pop off the stack onto 5 + 0
@5
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
// push 23 onto the stack
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// push 15 onto the stack
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call
// push return-Class2.set-1
@return-Class2.set-1
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
@2
D=D-A
@5
D=D-A
@ARG
M=D

// goto Class2.set
@Class2.set
0;JMP

(return-Class2.set-1)
// pop off the stack onto 5 + 0
@5
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
// call
// push return-Class1.get-2
@return-Class1.get-2
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

// goto Class1.get
@Class1.get
0;JMP

(return-Class1.get-2)
// call
// push return-Class2.get-3
@return-Class2.get-3
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

// goto Class2.get
@Class2.get
0;JMP

(return-Class2.get-3)
// label Sys.init$WHILE
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
// from Class1.vm
// function
(Class1.set)

@0
D=A
@R13
M=D

(Class1.setLOOP)
@R13
D=M
@Class1.setEND
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

@Class1.setLOOP
0;JMP
(Class1.setEND)
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
// pop off the stack onto static
@SP
AM=M-1
D=M
@Class1.0
M=D
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
// pop off the stack onto static
@SP
AM=M-1
D=M
@Class1.1
M=D
// push 0 onto the stack
@0
D=A
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
// function
(Class1.get)

@0
D=A
@R13
M=D

(Class1.getLOOP)
@R13
D=M
@Class1.getEND
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

@Class1.getLOOP
0;JMP
(Class1.getEND)
// push static Class1.0 onto the stack
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static Class1.1 onto the stack
@Class1.1
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
