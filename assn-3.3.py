score = raw_input("Enter score between 0.0 and 1.0:")
sc = float(score)
if sc < 0: exit("invalid score, score is too low")
if sc > 1: exit("invalid score, score is too high")
if sc >= 0.9: 
	print("A")
elif sc >= 0.8: 
	print("B")
elif sc >= 0.7: 
	print("C")
elif sc >= 0.6: 
	print("D")
elif sc < 0.6: 
	print("F")

