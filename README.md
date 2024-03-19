"Two Sum - Using Dictionary" is a topic that involves the use of a dictionary data structure to solve a specific problem.
Solution apporach:
input
nums=[2,7,11,15] target=9 
1. use dictionary to store the value and their index
2. use a for to iterate each number in the arr and also use enumerate iterate through a sequence and keep track of the index of each element-> num -each value in nums
3. create a variable called "ans" to find the value that's relavent to the value present in arr
   eg: ans=target-num -> 9-2=7
   now, ans=7
4. check whether the ans in dictonary
     if ans in dict:
       return [i,dict[ans]] - this means return their index
5. if not their update the value to next i value
    dict[num]=i
