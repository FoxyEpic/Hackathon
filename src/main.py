import random,time
score = 0
while True:
	difficulty = 1
	num1 = random.randint(1,50)
	operator = "/","-","+","*"
	op = random.choice(operator)
	num2 = random.randint(1,50)
	if score == 5:
		difficulty = 2
		print("Score 5 reached, changing difficulty to 2")
		time.sleep(2)
	if score == 10:
		difficulty = 3
		print("Score 10 reached, changing difficulty to max(3)")
		time.sleep(2.4)
	if op == "+":
		if difficulty == 3:
			num1 = random.randint(20,100)
			num2 = random.randint(20,100)
			print(num1,"+",num2)
			inp = int(input("Enter Answer: "))
			add_ans = num1 + num2
			if inp == add_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",add_ans)
				print("Your score was:",score)
				break
		
		if difficulty == 2:
			num1 = random.randint(10,70)
			num2 = random.randint(10,70)
			print(num1,"+",num2)
			inp = int(input("Enter Answer: "))
			add_ans = num1 + num2
			if inp == add_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",add_ans)
				print("Your score was:",score)
				break
		
		if difficulty == 1:	
			print(num1,"+",num2)
			inp = int(input("Enter Answer: "))
			add_ans = num1 + num2
			if inp == add_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",add_ans)
				print("Your score was:",score)
				break
		
	if op == "-":
		if difficulty == 1:
			print(num1,"-",num2)
			inp = int(input("Enter Answer: "))
			sub_ans = num1 - num2
			if inp == sub_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",sub_ans)
				print("Your score was:",score)
				break
			
		if difficulty == 2:
			num1 = random.randint(10,70)
			num2 = random.randint(10,70)
			print(num1,"-",num2)
			inp = int(input("Enter Answer: "))
			sub_ans = num1 - num2
			if inp == sub_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",sub_ans)
				print("Your score was:",score)
				break
			
		if difficulty == 3:
			num1 = random.randint(20,100)
			num2 = random.randint(20,100)
			print(num1,"-",num2)
			inp = int(input("Enter Answer: "))
			sub_ans = num1 - num2
			if inp == sub_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",sub_ans)
				print("Your score was:",score)
				break
			
	if op == "*":
		if difficulty == 1:
			num1 = random.randint(1,20)
			num2 = random.randint(1,10)
			print(num1,"×",num2)
			inp = int(input("Enter Answer: "))
			mul_ans = num1*num2
			if inp == mul_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",mul_ans)
				print("Your score was:",score)
				break
				
		if difficulty == 2:
			num1 = random.randint(10,30)
			num2 = random.randint(1,10)
			print(num1,"×",num2)
			inp = int(input("Enter Answer: "))
			mul_ans = num1*num2
			if inp == mul_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",mul_ans)
				print("Your score was:",score)
				break
			
		if difficulty == 3:
			num1 = random.randint(10,40)
			num2 = random.randint(1,10)
			print(num1,"×",num2)
			inp = int(input("Enter Answer: "))
			mul_ans = num1*num2
			if inp == mul_ans:
				print("Correct!")
				score += 1
				print("Now your score is:",score)
				time.sleep(1)
			else:
				print("Wrong answer, the answer was:",mul_ans)
				print("Your score was:",score)
				break
			
	if op == "/":
		if difficulty == 1:
			if num2 > num1:
				print(num2,"÷",num1)
				inp = int(input("Enter Answer: "))
				div_ans = num2//num1
				if inp == div_ans:
					print("Correct!")
					score += 1
					print("Now your score is:",score)
					time.sleep(1)
				else:
					print("Wrong answer, the answer was:",div_ans)
					print("Your score was:",score)
					break
			else:
				print(num1,"÷",num2)
				inp = float(input("Enter Answer: "))
				div_ans = num1//num2
				if inp == div_ans:
					print("Correct!")
					score += 1
					print("Now your score is:",score)
					time.sleep(1)
				else:
					print("Wrong answer, the answer was:",div_ans)
					print("Your score was:",score)
					break
			
		if difficulty == 2:
			num1 = random.randint(15,60)
			num2 = random.randint(15,60)
			if num2 > num1:
				print(num2,"÷",num1)
				inp = int(input("Enter Answer: "))
				div_ans = num2//num1
				if inp == div_ans:
					print("Correct!")
					score += 1
					print("Now your score is:",score)
					time.sleep(1)
				else:
					print("Wrong answer, the answer was:",div_ans)
					print("Your score was:",score)
					break
			else:
				print(num1,"÷",num2)
				inp = float(input("Enter Answer: "))
				div_ans = num1//num2
				if inp == div_ans:
					print("Correct!")
					score += 1
					print("Now your score is:",score)
					time.sleep(1)
				else:
					print("Wrong answer, the answer was:",div_ans)
					print("Your score was:",score)
					break
			
		if difficulty == 3:
			num1 = random.randint(30,70)
			num2 = random.randint(10,20)
			if num2 > num1:
				print(num2,"÷",num1)
				inp = int(input("Enter Answer: "))
				div_ans = num2//num1
				if inp == div_ans:
					print("Correct!")
					score += 1
					print("Now your score is:",score)
					time.sleep(1)
				else:
					print("Wrong answer, the answer was:",div_ans)
					print("Your score was:",score)
					break
			else:
				print(num1,"÷",num2)
				inp = float(input("Enter Answer: "))
				div_ans = num1//num2
				if inp == div_ans:
					print("Correct!")
					score += 1
					print("Now your score is:",score)
					time.sleep(1)
				else:
					print("Wrong answer, the answer was:",div_ans)
					print("Your score was:",score)
					break
			
