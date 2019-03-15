freq = 8000
samples = 4046
bin_n = float(input("Enter nth bin: "))
while(bin_n != 0):
    bin_freq = (float)(bin_n)*(freq/samples)
    print("Frequency is: ",bin_freq,"\n")
    bin_n = float(input("Enter nth bin: "))
print("End")
