// This file is part of the materials accompanying the book 
// "The Elements of Computing Systems" by Nisan and Schocken, 
// MIT Press. Book site: www.idc.ac.il/tecs
// File name: projects/08/FunctionCalls/FibonacciElement/FibonacciElement.tst

// FibonacciElement.asm is the result of translating both Main.vm and Sys.vm.
load FibonacciElement.asm,
output-file FibonacciElement.out,
compare-to FibonacciElement.cmp,
output-list RAM[0]%D1.6.1 RAM[261]%D1.6.1;

repeat 6000 {
  ticktock;
}

output;
