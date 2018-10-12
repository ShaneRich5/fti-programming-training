response = raw_input("Please enter a number between 70 and 100: ")
iter_num = 0

response = int(response)
loop_continue = True

while loop_continue == True:
    if 70 <= int(response) <= 100:
        for num in range(10, response, response//5):
            iter_num += 1
            if num % 7 == 0:
                print("The number " + str(num) + " is evenly divisible by 7.")
                loop_continue = False
                break
        else:
            print("You have reached the maximum number in the range: " + str(num))
            loop_continue = False
    else:
        response = raw_input("Try again.  Please enter a number between 70 and 100: ")
        iter_num += 1

print(iter_num)
