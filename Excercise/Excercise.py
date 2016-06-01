import shlex

def largestCombination():

    n, k = shlex.split(input('Enter n, k: '))  
    n = int(n)
    k = int(k)
    stringer = input('Enter the string composed of "a" and "b": ')    
    
    arr = []
    temp = stringer[0]
    count = 0

    for i in range(0, len(stringer), 1):
        if(temp == stringer[i]):
            count+=1            
        else:
            arr.append(count)
            count = 1
    
        temp = stringer[i]            
    arr.append(count)   

    print("")
    print(arr)

    max = 0
    tempi = 0
    for i in range(0, len(arr)-1, 1):
        tempk = k        
        j = i+1
        count = arr[i]
        while(tempk >= 0 and j <= len(arr)-1):
            if(i%2 == j%2):
                count+=arr[j]
                #print("% " + str(j) + "  " + str(count) + "  " + str(tempk))
            else:
                if(arr[j] <= tempk):
                    count+=arr[j]                    
                    tempk-=arr[j]
                    #print(str(j) + "  " + str(count) + "  " + str(tempk))
                else:                    
                    break    
            j+=1
        if(count > max):
                    max = count
                    tempi = i

    print(str(max) + " - " + str(tempi))     
#abbaabbaababbaaababa
#abbaabbaababbaaabbbb

def main():
    largestCombination()

main()