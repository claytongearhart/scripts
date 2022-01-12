# Inputs wavelengths and calculates frequency and energy

wv = input("Input wavelength in nm ")

wv = int(wv) * (10**-9)

freq = (3 * 10^8)/(wv)
print("{:e}".format(freq))

nrg = (6.6262 * 10**-34) * freq

print(str(nrg))