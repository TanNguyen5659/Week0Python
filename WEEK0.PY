def hello_name(user_name):
    # user_name = input("Enter username: ")
    print("Hello " +user_name)

hello_name("Tan")

def first_odds():
    for i in range(1,101):
        if i % 2 !=0:
         print (i)
        i +=1
    return 1
        
first_odds()



def max_num_in_list(a_list):
   max = a_list[0]
   print(a_list)
   for i in range(1,len(a_list)):
      if max < a_list[i]:
        max = a_list[i]
   return max  

print("The max in the list is : " + str(max_num_in_list([51, 52 ,3,7])))


def is_leap_year(a_year):
   if a_year % 400 == 0:
      return True
   elif a_year % 4 == 0 and a_year % 100 != 0:
      return True
   else:
      return False

print(str(is_leap_year(2024)))
   
def is_consecutive(a_list):
   sorted_list = sorted(a_list)
   print(sorted_list)
   for i in range(1,len(sorted_list)):
      if sorted_list[i] != sorted_list[i-1] + 1:  
            return False
   return True


print(str(is_consecutive([20,22,23,25,21])))

