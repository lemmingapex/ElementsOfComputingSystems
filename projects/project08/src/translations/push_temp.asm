// push %%SEGMENT%%[%%INDEX%%] onto the stack
@%%SEGMENT%%
D=A
@%%INDEX%%
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
