# -------------------------------
# multiplication with deslocation
# -------------------------------
# 
# s0 integer number >= 0
# s1 integer number >= 0
# a0 result of s0*s1
#
# operation done without multiplication instruction
# 
# example:
#     0 0 0 0 1 0 0 1: 09, a0
#     0 0 0 0 0 1 0 1: 05, a1
#     _______________
#     0 0 0 0 1 0 0 1: 09 a1
#   0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 1    : 36 a1
#     _______________
#     0 0 1 0 1 1 0 1: 45

#    a0 a1 t0 t1
# t0  9  5  0  0
# t1  9  5  0  0

multiply:
    add t0, zero, zero # t0 = zero + zero

    deslocation:
        andi t1, a1, 1 # t1 = a1 + 1
        srai a1, a1, 1 # right shift of a1 by 1
        # addi t1, a1, 0 # t1 = a1 + 1, store a1

        # # remove LSB
        # srai a1, a1, 1 # right shift of a1 by 1
        # slli a1, a1, 1 #  left shift of a1 by 1

        # # get LSB
        # sub t1, t1, a1 # t1 = t1 - a1
        # srai a1, a1, 1 # right shift of a1 by 1

        beq t1, zero, pass # if t1 == zero then pass
        add t0, t0, a0     # t0 = t0 + a0

    pass:
        slli a0, a0, 1             # left shift of a0 by 1
        bne  a1, zero, deslocation # if a1 != zero then deslocation
        add  a0, t0, zero          # a0 = t0 + zero
        jr ra                      # return

main:

    jal multiply

    jr ra