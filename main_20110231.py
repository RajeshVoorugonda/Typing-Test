import time

#preparing my lists of easy, medium and hard words for typing

easy_list=['duffles','animal','learning','diddle','mammals','sorry','wagon','funny']
medium_list=['excellent','abcedfgh','battle','henna','dazzler','xmas','fammag','xrolex']
hard_list=['zaqqum','zaqazip','pazazzes','dummy','queppem','yaddle','silliest','taimur']

#printing the instructions
print()
print("PLEASE READ THE FOLLOWING INSTRUCTIONS  :")
print("YOU NEED TO TYPE THE WORD DISPLAYED ON THE SCREEN AS FAST AS YOU CAN.")
print("EACH TIME YOU SUBMIT THE WORD BY PRESSING ENTER, A NEW WORD IS DISPLAYED UNTIL ALL THE WORDS(8 words) ALL COMPLETED")
print()
difficulty_level=input('Enter the difficulty level of words (E for easy, M for medium, H for hard)  : ')
print()
print("YOUR TIME STARTS IMMEDIATELY AFTER YOU PRESS ENTER. PRESS ENTER TO BEGIN")
input()


#defining a function to check errors in user input
def word_check(my_list):
    global correctly_typed
    for word in my_list:
        print("")
        print(word)
        user_input=input()
        if user_input==word:
            correctly_typed=correctly_typed+1
        else:
            if len(user_input)==len(word):
                for index in range(len(user_input)):
                    if user_input[index]!=word[index]:
                        wrongly_typed[word[index]]=wrongly_typed.get(word[index],0)+1
            else:
                for letter in word:
                    if word.count(letter)!=user_input.count(letter):
                        wrongly_typed[letter]=wrongly_typed.get(letter,0)+1


#defining dictionary to append wrongly typed words
wrongly_typed={}
#flag for number of correct words
correctly_typed=0

#recording the starting time
start_time=time.time()

#checking the words entered using the function word_check
if difficulty_level=="E":
    word_check(easy_list)
    selected_list = easy_list

elif difficulty_level=="M":
    word_check(medium_list)
    selected_list=medium_list

elif difficulty_level=="H":
    word_check(hard_list)
    selected_list=hard_list

else:
    print("You need enter the difficulty level as mentioned(either E or M or H)")
    print('Try again')
    exit()

#recording the end time
end_time=time.time()
print()

for_next_event=input("You're done. Press enter to check your results...")

time_taken = (end_time - start_time)

speed =int((len(selected_list)/time_taken)*60)
#rounding off the speed as words per minute must be an integer
if (speed - int(speed))>0.5:
    speed = int(speed+1)
else:
    speed = int(speed)

accuracy = correctly_typed/len(selected_list)

#counting the actual number of letters in all words given by computer
actual_number={}
for word in selected_list:
    for letter in word:
        actual_number[letter]=actual_number.get(letter,0)+1

#checking the % difficulty in wrongly typed letters
display_list=[]
for letter,value in wrongly_typed.items():
    total_number=actual_number[letter]
    if value!=0:
        display_list.append(((value/total_number)*100,letter))
    else:
        break

#printing the result in form of strings
print()
print("------------------------------------------------------------------------")
print("RESULT  :")
print()
print("Speed :  " + str(speed) + " words per minute")
print()
print("Accuracy :  " + str(int(accuracy* 100)) + "%")
print()
print("Level of 'difficulty' in typing:".upper())
if len(display_list)==0:
    print("Seems like you have no problem in typing any letter")
else:
    display_list.sort()
    display_list.reverse()
    for result in display_list:
        print("-->>   "+result[1]+" : "+str(result[0])[:4] + "%")
    print()
    print("You are fine with the other letters".upper())
print()
print()
for_exit=input("Press enter to continue ")
