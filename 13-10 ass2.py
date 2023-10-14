top=250
pant=350
shoes=400
print('Welcome to max')
cname=input('Enter customer name:')
cphno=input('Enter Phno:')
topq=int(input('Enter no of top'))
pantq=int(input('Enter no of pant'))
shoesq=int(input('Enter no of shoes'))
pc=input('Enter promo code:')
bill=(top*topq)+(pant*pantq)+(shoes*shoesq)
if pc=='HOLI' or pc=='holi':
    disc=bill*50/100
elif pc=='SUNDAY' or pc=='sunday':
    disc==bill*40/100
elif bill>=2000:
    disc=bill*20/100
elif bill>=1000:
    disc=bill*10/100
elif bill>=500:
    disc=bill*5/100
else:
    disc=bill*3/100
tbill=bill-disc
gst=tbill*12/100
obill=tbill+gst
print('customer name:',cname)
print('customer phno:',cphno)
print('bill:',bill)
print('Discount:',disc)
print('Gst 12%:',gst)
print('Bill to be paid:',obill)
print('Thank you!')
