#shift operations

number = int(input("Enter a number: "))
left_result = number << 2
right_result = number >> 2
print("Original number: ",number)
print("Left shift by 2: ", left_result)
print("Right shift by 2: ", right_result)
predict = int(input("Predict the left-shift result: "))
if predict == left_result:
    print("Correct prediction")
else:
    print("Incorrect prediction")
    print("The correct result is: ",left_result)