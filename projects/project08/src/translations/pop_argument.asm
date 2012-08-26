// pop off the stack onto %%SEGMENT%%[%%INDEX%%]
@%%SEGMENT%%
D=M
@%%INDEX%%
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
