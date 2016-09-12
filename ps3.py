
state={"UP":'000',"Raj":'001',"MP":'010',"AP":'011'}
city={"lucknow":'111',"jaipur":'110',"bhopal":'101',"Amravati":'100'}
district={"IET lucknow":'000',"NIT jaipur":'001',"mnnit":'010',"NIT warangal":'011'}
print "1.add  2.delete 3.modify"
a=input("Changes you want")
if a==1:
    s=raw_input("state name")
    m=raw_input("code name you for state")
    state.update({s:m})
    c=raw_input("city name")
    n=raw_input("code name for city")
    city.update({c:n})
    d=raw_input("district name")
    q=raw_input("code name for district")
    district.update({d:q})
   
if a==2:   
    b=raw_input("state to be deleted\n")
    if b in state.keys():   
        del state[b]
    else :
        print "invalid key"
    b=raw_input("city to be deleted\n")
    if b in city.keys():   
        del city[b]
    else :
        print "invalid key"
    b=raw_input("district to be deleted\n")
    if b in district.keys():   
        del district[b]
    else :
        print "invalid key"
if a==3:
    t1=raw_input("state code to be modified\n")
    t11=raw_input("enter the new code\n")
    if t1 in state.keys():
        state.update({t1:t11})
    else :
        print 'invalid state'
    t2=raw_input("district code  to be modified\n")
    t21=raw_input("enter the new code\n")
    if t2 in district.keys():
        district.update({t2:t21})
    else :
        print 'invalid district'
    t3=raw_input("city code to be modified\n")
    t31=raw_input("enter the new code\n")
    if t3 in city.keys():
        city.update({t3:t31})
    else :
        print 'invalid city'
else :
    l1=raw_input("enter the customer name\n")
    l2=raw_input("enter the customer district\n")
    l3=raw_input("enter the customer city\n")
    l4=raw_input("enter the customer state\n")
   
