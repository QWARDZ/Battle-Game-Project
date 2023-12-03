import random
import time

villain_powers = ["Punch", "Kick", "Flying kick", "Elbows and Knees"]

hero_health = 100
villain_health = 100

print("Welcome to my battle game.")
time.sleep(2)

print("You are Ryan of the Intergalactic Police, Power Pop Girl.")
time.sleep(2)

print("Your mission is to defeat the evil John.")
time.sleep(2)

print("After searching for years you finally find John.")
time.sleep(2)

print("Now is your time to beat him.")
time.sleep(3)

while True:
		print("\n--------POWERS----------")
		print("1) Triangle choke: 15 damage")
		print("2) Punch: 6 damage")
		print("3) Kick: 5 damage")
		print("4) Intergalactic Smile: heals 10 damage\n")

		print("Your health: " + str(hero_health))
		print("John health: " + str(villain_health))
		attack = input("\nWhich attack do you want to use powers 1-4? ")

		if attack in ['1', '2', '3', '4']:
				if attack == '1':
						print("\nYour attack is: Triangle choke")
						villain_health -= 15
				elif attack == '2':
						print("\nYour attack is: Punch")
						villain_health -= 6
				elif attack == '3':
						print("\nYour attack is: Kick")
						villain_health -= 5
				elif attack == '4':
						print("\nYour attack is: Intergalactic Smile")
						hero_health += 10

				time.sleep(1)
				print("John health is now: " + str(villain_health))
		else:
				print("Please choose 1, 2, 3, or 4.")
				time.sleep(1)
				continue

		time.sleep(1)
		attack2 = random.choice(villain_powers)
		print("John attack is: " + attack2)

		if attack2 == 'Flying kick':
				hero_health -= 15
		elif attack2 == 'Punch':
				hero_health -= 6
		elif attack2 == 'Kick':
				hero_health -= 5
		elif attack2 == 'Elbows and Knees':
				villain_health += 10

		time.sleep(1)
		print("Your health is now: " + str(hero_health))

		if villain_health <= 0:
				print("\nYou win! Congratulations, you defeated John")
				break
		if hero_health <= 0:
				print("\nYou lose! John defeated you!")
				break