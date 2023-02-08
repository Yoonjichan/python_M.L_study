xs=[-1., 0., 1., 2., 3., 4.]
ys=[-2., 1., 4., 7., 10., 13.]

w=-10.
b=10.
a=int(input("학습횟수:"))
c=a/10

for epoch in range(a):
    for n in range(6):

        y=xs[n]*w+1*b

        t=ys[n]
        E=(y-t)**2/2

        yb=y-t
        wb=yb*xs[n]
        bb=yb*1

        lr=0.01
        w=w-lr*wb
        b=b-lr*bb

        if epoch%c==1 and n==0:
            print('w=%6.3f, b=%6.3f' %(w,b))

