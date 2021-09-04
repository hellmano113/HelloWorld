import numpy 


def initial_para(nums_feature):
    w = np.zero((1,nums_feature))
    b = 0 
    return w,b

def activation(w,x,b):
    '''
    x_ = w*x+b , y = 1/(1+exp(-x_))
    '''

    x_ = np.dot(w,x.T)+b
    sigmoid = 1 / (1+np.exp(-x_))

    return sigmoid

def SGD(w,x,b,label,learning_rate):
    #batch_size
    n = len(label)
    #激活函数
    sigmoid = activation(w,x,b)
    #损失函数g
    loss = -np.sum(label.T*np.log(sigmoid)+(1-label).T*np.log(1-sigmoid)) / n

    g_w = np.dot(x.T,(sigmoid - lable.T).T) /n
    g_b = np.sum((sigmoid-label.T)) / n

    w = w -learning_rate * g_w.T
    b = b - learning_rate * g_b

    return w,b,loss