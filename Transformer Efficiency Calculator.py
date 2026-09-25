# Transformer Efficiency Calculator

output_power = float(input("Enter output power (W): "))
input_power = float(input("Enter input power (W): "))

if input_power <= 0:
    print("Input power must be greater than 0.")
elif output_power > input_power:
    print("Output power cannot be greater than input power.")
else:
    efficiency = (output_power / input_power) * 100

    print("\n--- Transformer Efficiency Calculator ---")
    print("Input Power:", input_power, "W")
    print("Output Power:", output_power, "W")
    print("Transformer Efficiency:", round(efficiency, 2), "%")
``