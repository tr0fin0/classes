# ----------
# Palindrome
# ----------
# 
# int Palindrome(char *s)
#   char *s, pointer to string
# 
# receives a string ended in \0 
# return 1 if the string is     palindrome
#        0 if the string is not palindrome
# 
# assuming that the Maiuscula 
# is implemented
# 
#     .TEXT:
#         .word 0x61605E5C
#         .word 0x796E6462
#         .word 0x00007B7A

Palindrome:
    addi sp, sp, -4
    sw   ra, 0(sp)

    call Maiuscula

    addi t0, a0, 0          # *s[0]

    loop0:
        lbu t1, 0(a0)       #    char = s[i]
        beq t1, zero, end0  # if char == \0 then end0

        addi a0, a0, 1      # a0++
        j loop0

    end0:
        addi t1, a0, -1     # *s[n-1]

    addi a0, zero, 1; # a0 = 1

    loop1:
        lbu t2, 0(t0)       # s[i]
        lbu t3, 0(t1)       # s[n-i-1]
        beq t0, zero, end   # if s[i] == zero then end

        addi t0, t0,  1     # t0++
        addi t1, t1, -1     # t1--

        bne t2, t3, end1;   # if s[i] != s[n-i-1] then end1
        j loop1

    end1:
        addi a0, zero, 0; # a0 = 0
        j end

    end:
        lw   ra, 0(sp)
        addi sp, sp,4
        jr ra