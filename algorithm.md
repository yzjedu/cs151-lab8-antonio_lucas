# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. output program explanation to user 
2. tored as roll_count.

Purpose: prompting user to input the number of times they want to roll dice
name: roll_input  
parameter: none  
return: num_rolls  
algorithm: 
1. prompt the user to input how many times they want to roll the dies stored as num_rolls
3. while num_rolls is not a number
   1. output invalid input
   2. prompt the user to input how many times they want to roll the dies stored as num_rolls
3. return num_rolls

Purpose: roll the die the number of times they want and store in list  
name: roller  
parameter: num_rolls  
return: list_of_values  
algorithm: 
1. set num rolls to roll_input
2. set a count variable to 0
3. make and empty list for list_of_values
4. while count < num_rolls
   1. set roll 1 to random integer between 1 and 6
   1. set roll 2 to random integer between 1 and 6
   1. add roll 1 and roll 2 as sum
   1. apphend sum to list_of_values
   1. add 1 to count
5. return list_of_values
   
Purpose:  count the number of times a value is rolled  
name: times_rolled  
parameter: none  
return:  count_list
algorithm:  
1. set list_of_values to roller function
2. make an empty list of sums
3. set count to 2
3. set sum_count to 0
3. while count is between or equal to 2 and 12
    1. set sum_count to the number of times the number count occurs in the list_of_values
    2. apphend sum_count to list_of_sums
    3. add 1 to count
5. return list_of_sums

Purpose:  output the sum of list with *  
name: sum_chart  
parameter: none  
return:  none  
algorithm:  
1. set count to 2
2. set sum_list to times_rolled function
2. while count < 12
   1. output: "Sum of {count}", "*" * the index count in sum_list
   2. add 1 to count
