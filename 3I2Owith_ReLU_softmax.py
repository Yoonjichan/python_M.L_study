from math import exp

i1, i2 =.05, .10
t1, t2=.01, .99

w1, w3=.15, .25
w2, w4=.20, .30
b1, b2=.35, .35

w5, w7=.40, .50
w6, w8=.45, .55
b3, b4=.60, .60

a, b=int(input("Test N:")), float(input("LearningRate:"))


for epoch in range(a):
  print('------------------')
  print('epoch=%d' %epoch)
  print('------------------')

  h1=i1*w1+i2*w2+1*b1
  h2=i1*w3+i2*w4+1*b2
  h1=(h1>0)*h1
  h2=(h2>0)*h2
  o1=h1*w5+h2*w6+1*b3
  o2=h1*w7+h2*w8+1*b4
  o1m=o1-max(o1, o2)
  o2m=o2-max(o1, o2)
  o1=exp(o1m)/(exp(o1m)+exp(o2m))
  o2=exp(o2m)/(exp(o1m)+exp(o2m))

  print('h1, h2=%6.3f, %6.3f' %(h1, h2))
  print('o1, o2=%6.3f, %6.3f' %(o1, o2))

  E=(o1-t1)**2/2+(o2-t2)**2/2
  print('E=%.7f' %E)
  if E<0.0000001:
    break
  
  o1b, o2b=o1-t1, o2-t2
 
  
  h1b, h2b=o1b*w5+o2b*w7, o1b*w6+o2b*w8
  h1b, h2b=h1b*(h1>0)*1, h2b*(h2>0)*1

  w1b, w3b=i1*h1b, i1*h2b
  w2b, w4b=i2*h1b, i2*h2b
  b1b, b2b=1*h1b, 1*h2b
  w5b, w7b=h1*o1b, h1*o2b
  w6b, w8b= h2*o1b, h2*o2b
  b3b, b4b=1*o1b, 1*o2b

  lr=b
  w1, w3=w1-lr*w1b, w3-lr*w3b
  w2, w4=w2-lr*w2b, w4-lr*w4b
  b1, b2=b1-lr*b1b, b2-lr*b2b
  w5, w7=w5-lr-w5b, w7-lr*w7b
  w6, w8=w6-lr*w6b, w8-lr*w8b
  b3, b4=b3-lr*b3b, b4-lr*b4b