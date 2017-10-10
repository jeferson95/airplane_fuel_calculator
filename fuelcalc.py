def fuel_calc(fuelc, distance, speed):
	while True:
		try:
			fuelc = int(fuelc)
			distance = int(distance)
			speed = int(speed)

		except:
			return "Invalid arguments. Try again"

		else:
			cont = distance / speed
			cont = cont * 60
			print("travel time is " + "%.2f" % cont + " minutes")

			fuelc = fuelc / 60
			fueln = cont * fuelc
			print("now adding 30% reserved fuel...")
			fueln += (fueln / 100) * 30
			print ("%.2f" % fueln + " gallons consumed")
			return ("You need " + str("%.2f" % fueln) + " gallons for this trip")