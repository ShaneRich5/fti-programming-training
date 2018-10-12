# Read from the file you created in the previous lab and print it out
# Write the last song you listened to on a new line in the same file
# Read from the file again, this time printing "The last movie I watched is: " before the movie
# and "My the last song I listened to is: " before the song
filename = '/Users/jdcarter/Documents/Programming Training 2018/programming-training-2018/solutions/labs/lab7.0/last_movie.txt'
pout = open(filename, 'r')
for line in pout:
    print(line)
pout.close()
pout = open(filename, 'a')
pout.write('\nShake it Off - Taylor Swift')
pout.close()
pout = open(filename, 'r')
print("The last movie I watched is: " + pout.readline())
print("The last song I listened to is: " + pout.readline())
pout.close()
