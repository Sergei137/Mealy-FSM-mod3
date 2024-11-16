# 2024-11-15
# Sergei Mochalov
# Mealy finite state machine to determine if a binary number is divisible by 3


# Mealy FSM implementation
def mealy_fsm_mod3(bin_val):
    state = 0
    for i in bin_val:
        if state == 0:
            if i == 0:
                state = 0
            elif i == 1:
                state = 1
        elif state == 1:
            if i == 0:
                state = 2
            elif i == 1:
                state = 0
        elif state == 2:
            if i == 0:
                state = 1
            elif i == 1:
                state = 2
    return state






# Convert binary number into decimal (there is probably a more efficient way to do this)
def bin_to_dec(bin_val):
    decimal_total = 0
    loop_count = 0
    for i in bin_val:
        if int(i) == 1:
            decimal_total +=  2 ** (loop_count)
        loop_count += 1
    return decimal_total




# input binary number (no error checking)
binary_input1 = input("Enter a binary number: ")
print(f"binary input: {binary_input1}")
bin_val = [int(digit) for digit in str(binary_input1)]

# print decimal value of binary number
decimal_val = bin_to_dec(binary_input1)
print("binary to decimal: " + str(decimal_val))

output = mealy_fsm_mod3(bin_val)
if output == 0:
    print("The binary number is divisible by 3")
else:
    print("The binary number is not divisible by 3")







