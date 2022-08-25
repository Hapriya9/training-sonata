number=[2,3,4,5,6,7,8,9]
print(type(number))
def common_member(a,b):
    a_set=set(a)
    b_set=set(b)
    if(a_set & b_set):
        print(a_set & b_set)
    else:
        print("No Common elements")

a = [1, 1, 3, 4, 6, 5, 8, 21, 34, 55, 59, 89, 45]
b = [1, 1, 5, 4, 7, 9, 10, 11, 12, 13, 45, 67, 78, 56,90]
common_member(a,b)

list2=[4,7,9,5,2,3,1]
even_nos=[num for num in list2 if num%==0]
print("Even numbers:" ,even_nos)

h={"Deephi":16/8/2000,"Kavitha":18/06/2000}
print(type(h))