#bill splitter(a wrokshop from freecodecamp-numbers and mathematical operations)
running_total=0
num_of_friends=4
appetizer=37.89
main_courses=57.34
desserts=39.39
drinks=64.21
#calculate bill
running_total+=appetizer+main_courses+desserts+drinks
print('Total bill so far:',running_total)
#to calculate tip
tip=running_total*0.25      #the friends are decided to give 25%tip
print('Tip amount:',tip)
#calculate total bill
running_total+=tip
print('Total with tip:',running_total)
#split the bill among 4 friends equally
final_bill=running_total/num_of_friends
print('Bill per persons:',final_bill)
#use round function because result of final bill gives decimals
each_pays=round(final_bill,2)
print('Each person pays:',each_pays)
