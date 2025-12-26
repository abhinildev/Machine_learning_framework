#All the loss functions

#here y is the actual class value y_n is the predicted class value and n is the no of values in y
def mean_squared_error(y,y_n):
    print("The mean squared error is: ")
    m=len(y)
    for i in range(m):
        loss+=(y[i]-y_n)*(y[i]-y_n)
    cost=(1/(2*m))*loss
    return cost

