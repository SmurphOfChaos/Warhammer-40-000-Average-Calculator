#To Make It Wait Before Printing Each Line
import os, sys
from time import sleep

#Clear Screen Command
def screen_clear():
    # for mac and linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

#To Make It Appear To Be Typing Across Like A Typewriter At The Start
def typingCredits(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.03)
    value=print()
    return value
def typingSpeed(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.03)
    value=input()
    return value

#To Clear The Screen
screen_clear()

#Credits
typingCredits("Here is the Warhammer 40k Average Calculator, brought to you by the SMURPH_OF_CHAOS\n")
sleep(0.5)

#Speed Of Text- As Defined By The User
typingChoice=typingSpeed("How fast would you like the type to be; fast(f), medium(m), or slow(s)? (Currently the speed is set to medium)\n")
if typingChoice == "f":
    typeSpeed = 0.01
elif typingChoice == "s":
    typeSpeed = 0.05
else:
    typeSpeed = 0.03

#To Make It Appear To Be Typing Across Like A Typewriter, Using The User's Preferred Speed
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(typeSpeed)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(typeSpeed)
    value=input()
    return value

#CHOOSING OPTION
def choosingOption():
    choice = int(input("Choose an option between 1 and 18\n"))
    #Attack With Torrent; i.e Has No Hit Roll
    if choice == int("9"):
        strength=float(typingInput("What is the Strength of the attacking weapon?\n"))
    elif choice == int("12"):
        strength=float(typingInput("What is the Strength of the attacking weapon?\n"))
    #Attack Without Torrent; i.e Has A Hit Roll
    elif 0 < choice < 19:
        hitRoll=float(typingInput("What is the Hit Roll of the attacking weapon? (Enter a number between 2 and 6)\n"))
        strength=float(typingInput("What is the Strength of the attacking weapon?\n"))
        #Undefined Attack
    else:
        typingPrint("Sorry, there is no program available for this number")
        screen_clear()
        choosingOption()

    armourPiercing=float(typingInput("What is the AP characteristic of the attacking weapon?(Enter a positive integer, the number after the '-' sign)\n"))
    toughness=float(typingInput("What is the Toughness of the defending unit?\n"))
    savingThrow=float(typingInput("What is the Saving Throw of the defending unit?\n"))
    isavingThrow=float(typingInput("What is the Invulnerable Saving Throw of the defending unit? (if none, type 100)\n"))
    attackNumber=float(typingInput("How many Attacks are there in total?(If a D6 value, enter the average of that)\n"))
    damage=float(typingInput("What is the Damage characteristic of each attack?\n"))

    if strength >= 2*toughness:
        woundRoll=2
    elif strength > toughness:
        woundRoll=3
    elif strength == toughness:
        woundRoll=4
    elif strength < toughness:
        woundRoll=5
    else:
        woundRoll=6

    #1- 'NORMAL ATTACK'
    if choice == int("1"):
        stepOne=(7-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepOne*stepTwo*stepThreeB*attackNumber)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7 < 7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)
        else:
            finalAnswerA =(stepOne*stepTwo)
            
    #2- 'RE-ROLLING ONES'
    elif choice == int("2"):
        stepOne=(7-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = stepOne*stepTwo*stepThreeA*attackNumber*7/6
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =stepOne*stepTwo*stepThreeB*attackNumber*7/6
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA = stepOne*stepTwo*stepThreeA*attackNumber*7/6
        else:
            finalAnswerA = stepOne*stepTwo*7/6
        
    #3- 'DEVASTATING WOUNDS'
    elif choice == int("3"):
        stepOne=(7-hitRoll)/6
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = (stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)
        else:
            finalAnswerA = (stepOne*stepTwo)+(stepOne*1/6*attackNumber)
        
    #4- 'DEVASTATING WOUNDS'&'RE-ROLLING ONES'
    elif choice == int("4"):
        stepOne=(7-hitRoll)/6
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = ((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber))*7/6
        elif isavingThrow < (savingThrow-armourPiercing):
             finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber))*7/6
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber))*7/6
        else:
            finalAnswerA =((stepOne*stepTwo)+(stepOne*1/6*attackNumber))*7/6
        
    #5- 'LETHAL HITS'
    elif choice == int("5"):
        stepOne=(6-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepOne*stepTwo*stepThreeB*attackNumber)+(1/6*stepThreeB)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA)
        else:
            finalAnswerA =(stepOne*stepTwo)+(1/6)
        
    #6- 'LETHAL HITS'&'RE-ROLLING ONES'
    elif choice == int("6"):
        stepOne=(6-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA))*7/6
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(1/6*stepThreeB))*7/6
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA))*7/6
        else:
            finalAnswerA =((stepOne*stepTwo)+(1/6))*7/6
        
    #7- 'SUSTAINED HITS 1'
    elif choice == int("7"):
        stepOne=(7-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)+((8-hitRoll)/(7-hitRoll))
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepOne*stepTwo*stepThreeB*attackNumber)+((8-hitRoll)/(7-hitRoll))
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)+((8-hitRoll)/(7-hitRoll))
        else:
            finalAnswerA =(stepOne*stepTwo)+((8-hitRoll)/(7-hitRoll))

    #8- 'SUSTAINED HITS 1'&'RE-ROLLING ONES'
    elif choice == int("8"):
        stepOne=(7-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+((8-hitRoll)/(7-hitRoll)))
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+((8-hitRoll)/(7-hitRoll)))
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+((8-hitRoll)/(7-hitRoll)))
        else:
            finalAnswerA =((stepOne*stepTwo)+((8-hitRoll)/(7-hitRoll)))
        
    #9- 'TORRENT'
    elif choice == int("9"):
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =(stepTwo*stepThreeA*attackNumber)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepTwo*stepThreeB*attackNumber)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(stepTwo*stepThreeA*attackNumber)
        else:
            finalAnswerA =(stepTwo)
        
    #10- 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'
    elif choice == int("10"):
        stepOne=(7-hitRoll)/6
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = ((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))
        else:
            finalAnswerA = ((stepOne*stepTwo)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))

    #11- 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES'
    elif choice == int("11"):
        stepOne=(7-hitRoll)/6
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = ((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll))
        else:
            finalAnswerA = ((stepOne*stepTwo)+(stepOne*1/6*attackNumber))*((8-hitRoll)/(7-hitRoll)) 

    #12- 'TORRENT'&'DEVASTATING WOUNDS'
    elif choice == int("12"):
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = (stepTwo*stepThreeA*attackNumber)+(1/6*attackNumber)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepTwo*stepThreeB*attackNumber)+(1/6*attackNumber)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(stepTwo*stepThreeA*attackNumber)+(1/6*attackNumber)
        else:
            finalAnswerA = (stepTwo)+(1/6*attackNumber)
        
    #13- 'LETHAL HITS'&'SUSTAINED HITS 1'
    elif choice == int("13"):
        stepOne=(6-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(1/6*stepThreeB))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA))*((8-hitRoll)/(7-hitRoll))
        else:
            finalAnswerA =((stepOne*stepTwo)+(1/6))*((8-hitRoll)/(7-hitRoll))
        
    #14- 'LETHAL HITS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES'
    elif choice == int("14"):
        stepOne=(6-hitRoll)/6
        stepTwo=(7-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA =(((stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA))*((8-hitRoll)/(7-hitRoll)))*7/6
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(((stepOne*stepTwo*stepThreeB*attackNumber)+(1/6*stepThreeB))*((8-hitRoll)/(7-hitRoll)))*7/6
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(((stepOne*stepTwo*stepThreeA*attackNumber)+(1/6*stepThreeA))*((8-hitRoll)/(7-hitRoll)))*7/6
        else:
            finalAnswerA =(((stepOne*stepTwo)+(1/6))*((8-hitRoll)/(7-hitRoll)))*7/6
        
    #15- 'LETHAL HITS'&'DEVASTATING WOUNDS'
    elif choice == int("15"):
        stepOne=(6-hitRoll)/6
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = (stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =(stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =(stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber)
        else:
            finalAnswerA = (stepOne*stepTwo)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber)
        
    #16- 'LETHAL HITS'&'DEVASTATING WOUNDS'&'RE-ROLLING ONES'
    elif choice == int("16"):
        stepOne=(6-hitRoll)/6
        stepTwo=(6-woundRoll)/6
        stepThreeA=(savingThrow+armourPiercing-1)/6
        stepThreeB=(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = ((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*(7/6)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*(7/6)
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*(7/6)
        else:
            finalAnswerA = ((stepOne*stepTwo)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*(7/6)

    #17- 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'
    elif choice == int("17"):
        stepOne (6-hitRoll)/6
        stepTwo =(6-woundRoll)/6
        stepThreeA =(savingThrow+armourPiercing-1)/6
        stepThreeB =(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = ((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA =((stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll))
        elif isavingThrow == (savingThrow-armourPiercing) < 7 < 7:
            finalAnswerA =((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll))
        else:
            finalAnswerA = ((stepOne*stepTwo)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll))
        
        

    #18- 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES'
    elif choice == int("18"):
        stepOne =(6-hitRoll)/6
        stepTwo =(6-woundRoll)/6
        stepThreeA =(savingThrow+armourPiercing-1)/6
        stepThreeB =(isavingThrow-1)/6
        if isavingThrow > (savingThrow-armourPiercing) <7:
            finalAnswerA = (((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll)))*(7/6)
        elif isavingThrow < (savingThrow-armourPiercing):
            finalAnswerA = (((stepOne*stepTwo*stepThreeB*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll)))*(7/6)
        elif isavingThrow == (savingThrow-armourPiercing) < 7:
            finalAnswerA =(((stepOne*stepTwo*stepThreeA*attackNumber)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll)))*(7/6)
        else:
            finalAnswerA = (((stepOne*stepTwo)+(stepOne*1/6*attackNumber)+(1/6*stepTwo*attackNumber))*((8-hitRoll)/(7-hitRoll)))*(7/6)
    #Final Answers
    finalAnswerB = finalAnswerA*damage
    probability = 1/finalAnswerB
    typingPrint("The number of Attacks that would proceed to do damage is ")
    sleep(0.03)
    print(finalAnswerA)
    typingPrint("The number of Wounds that would be done to the defending unit is ")
    sleep(0.03)
    print(finalAnswerB)
    sleep(0.03)
    typingPrint("The probability of you doing any damage to the opposing unit is 1 in ")
    print(probability)

    if probability <= 0.25:
        typingPrint("You are very likely to do damage\n")
    elif probability <= 0.5:
         typingPrint("You are likely to do damage\n")
    elif probability == 1:
        typingPrint("You are neither likely or unlikely to do damage\n")
    elif probability >= 1.5:
        typingPrint("You are very unlikely to do damage\n")
    else:
        typingPrint("You are unlikely to do damage\n")

    sleep(3)

    #Loop
    loop = typingInput("Would you like to use again?(y/n)\n")
    if loop == "y":
        screen_clear()
        print("Your options are below:\n")
        print("1= 'NORMAL ATTACK'\n")
        print("2= 'RE-ROLLING ONES'\n")
        print("3= 'DEVASTATING WOUNDS'\n")
        print("4= 'DEVASTATING WOUNDS'&'RE-ROLLING ONES TO HIT'\n")
        print("5= 'LETHAL HITS'\n")
        print("6= 'LETHAL HITS'&'RE-ROLLING ONES TO HIT'\n")
        print("7= 'SUSTAINED HITS 1'\n")
        print("8= 'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        print("9= 'TORRENT'\n")
        print("10= 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'\n")
        print("11= 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        print("12= 'TORRENT'&'DEVASTATING WOUNDS'\n")
        print("13= 'LETHAL HITS'&'SUSTAINED HITS 1'\n")
        print("14= 'LETHAL HITS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        print("15= 'LETHAL HITS'&'DEVASTATING WOUNDS'\n")
        print("16= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'RE-ROLLING ONES TO HIT'\n")
        print("17= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'\n")
        print("18= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        choosingOption()
    else:
        screen_clear()
        typingPrint("Goodbye!")
        sleep(2)
        quit()
#Start
def start():
    #Skip
    skip = typingInput("Would you like to skip the intro?(y or n)")
    #Options- Was Intro Skipped Or Not?
    if skip == 'n':
        typingPrint("Your options will appear below:\n")
        sleep(typeSpeed)
        typingPrint("1=  'NORMAL ATTACK'\n")
        sleep(typeSpeed)
        typingPrint("2=  'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("3=  'DEVASTATING WOUNDS'\n")
        sleep(typeSpeed)
        typingPrint("4=  'DEVASTATING WOUNDS'&'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("5=  'LETHAL HITS'\n")
        sleep(typeSpeed)
        typingPrint("6=  'LETHAL HITS'&'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("7=  'SUSTAINED HITS 1'\n")
        sleep(typeSpeed)
        typingPrint("8=  'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("9=  'TORRENT'\n")
        sleep(typeSpeed)
        typingPrint("10= 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'\n")
        sleep(typeSpeed)
        typingPrint("11= 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("12= 'TORRENT'&'DEVASTATING WOUNDS'\n")
        sleep(typeSpeed)
        typingPrint("13= 'LETHAL HITS'&'SUSTAINED HITS 1'\n")
        sleep(typeSpeed)
        typingPrint("14= 'LETHAL HITS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("15= 'LETHAL HITS'&'DEVASTATING WOUNDS'\n")
        sleep(typeSpeed)
        typingPrint("16= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'RE-ROLLING ONES TO HIT'\n")
        sleep(typeSpeed)
        typingPrint("17= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'\n")
        sleep(typeSpeed)
        typingPrint("18= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
    elif skip == 'y':
        print("Your options are below:\n")
        print("1= 'NORMAL ATTACK'\n")
        print("2= 'RE-ROLLING ONES TO HIT'\n")
        print("3= 'DEVASTATING WOUNDS'\n")
        print("4= 'DEVASTATING WOUNDS'&'RE-ROLLING ONES TO HIT'\n")
        print("5= 'LETHAL HITS'\n")
        print("6= 'LETHAL HITS'&'RE-ROLLING ONES TO HIT'\n")
        print("7= 'SUSTAINED HITS 1'\n")
        print("8= 'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        print("9= 'TORRENT'\n")
        print("10= 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'\n")
        print("11= 'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        print("12= 'TORRENT'&'DEVASTATING WOUNDS'\n")
        print("13= 'LETHAL HITS'&'SUSTAINED HITS 1'\n")
        print("14= 'LETHAL HITS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        print("15= 'LETHAL HITS'&'DEVASTATING WOUNDS'\n")
        print("16= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'RE-ROLLING ONES TO HIT'\n")
        print("17= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'\n")
        print("18= 'LETHAL HITS'&'DEVASTATING WOUNDS'&'SUSTAINED HITS 1'&'RE-ROLLING ONES TO HIT'\n")
        choosingOption()
start()
