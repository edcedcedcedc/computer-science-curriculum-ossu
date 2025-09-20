
//prologue and metadata of the function
	.file	"3.2.2.c"
	.text
	.globl	multstore
	.type	multstore, @function
multstore: //function name 
.LFB0:
	.cfi_startproc
	endbr64 //indirect branch tracking ??
	pushq	%rbx //stack frame setup
	.cfi_def_cfa_offset 16 //directive for debugger 
	.cfi_offset 3, -16
	movq	%rdx, %rbx //argument handling 
	call	mult2@PLT //call helper 
	movq	%rax, (%rbx) // result from mult2, (memory address of %rbs) this write t to *dest
	popq	%rbx //restore the callee-saved %rbx 
	.cfi_def_cfa_offset 8
	ret //return to caller
	.cfi_endproc //mark end of debugging 
.LFE0: //extra metadata 
	.size	multstore, .-multstore
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:

/////////////////////////////
53               push %rbx
48 89 d3         mov %rdx, %rbx
e8 00 00 00 00   call mult2
48 89 03         mov %rax, (%rbx)
5b               pop %rbx
c3               ret
