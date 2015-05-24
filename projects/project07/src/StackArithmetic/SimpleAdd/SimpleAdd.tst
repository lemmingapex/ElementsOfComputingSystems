// This file is part of the materials accompanying the book 
// "The Elements of Computing Systems" by Nisan and Schocken, 
// MIT Press. Book site: www.idc.ac.il/tecs
// File name: projects/07/StackArithmetic/SimpleAdd/SimpleAdd.tst

load SimpleAdd.asm,
output-file SimpleAdd.out,
compare-to SimpleAdd.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,

repeat 60 {
  ticktock;
}

output;
