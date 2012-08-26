// push static %%FILENAME%%.%%STATICADDRESS%% onto the stack
@%%FILENAME%%.%%STATICADDRESS%%
D=M
@SP
A=M
M=D
@SP
M=M+1
