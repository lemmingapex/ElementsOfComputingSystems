// call
// push return-%%F%%-%%ID%%
@return-%%F%%-%%ID%%
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
@%%N%%
D=D-A
@5
D=D-A
@ARG
M=D

// goto %%F%%
@%%F%%
0;JMP

(return-%%F%%-%%ID%%)
