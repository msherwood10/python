def computepay(h,r):
	if h <= 40:
    	return h*r
	elif h > 40:
    	over = h - 40
    	ot = float(over)
    	total = 40*r + 1.5*r*ot
        return total
hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter Rate:")
r = float(rph)
p = computepay(h,r)
print p