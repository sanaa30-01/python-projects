#practicing scope using prime number check

def is_prime(num):
    if num == 1:
        return False
    
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True 

print(is_prime(73))

#steps to commit:
#cd to current folder 
#check git status to see untracked files
#use git add to add the specific files I want
#use git add . to add all files to staging area
#use git commit -m "message" to commit my changes locally to git
#use git push origin main to push my changes and commits to github