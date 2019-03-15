
freq = int(input('Enter the frequency\n'))
samples = int(input('Enter the samples\n'))
bin_n = float(input("Enter nth bin: "))
while(bin_n != 0):
    bin_freq = (float)(bin_n)*(freq/samples)
    print("Frequency is: ",bin_freq,"\n")
    bin_n = float(input("Enter nth bin: "))
print("End")
