print("======================================")
print("    TRANSFORMER EFFICIENCY CALCULATOR")
print("======================================")

input_power = float(input("Enter input power (W): "))
output_power = float(input("Enter output power (W): "))

if input_power <= 0 or output_power < 0:
    print("\nPlease enter valid power values.")
elif output_power > input_power:
    print("\nOutput power cannot be greater than input power.")
else:
    efficiency = (output_power / input_power) * 100
    power_loss = input_power - output_power

    print("\n------------- RESULTS -------------")
    print(f"Input Power       : {input_power:.2f} W")
    print(f"Output Power      : {output_power:.2f} W")
    print(f"Power Loss        : {power_loss:.2f} W")
    print(f"Transformer Efficiency : {efficiency:.2f}%")
    print("-----------------------------------")
