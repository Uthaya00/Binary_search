# pos for show the index value
pos=1
#function search
def search(list,n):
    # lower value
    l=0
    #upper value
    u=len(list)-1
    while l<u:
        # find middle value
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid;
            return True
        else:
            if list[mid]<n:
                l=mid  #lower value(0) change into mid value
            else:
                u=mid  #upper value(5) change into mid value

list=[1,3,5,77,99,100]
n=99

if search(list,n):
    print("found at",pos)
else:
    print('not found')