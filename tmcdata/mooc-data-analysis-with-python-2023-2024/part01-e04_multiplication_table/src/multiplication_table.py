# #!/usr/bin/env python3


def main():
    i =1
    while i <= 10:
        j=1
        while j<=10:
            result = i *j
            print(f"{result:4}",end="")
            j+=1
        print()
        i +=1
        
    # for i in range(1,11):
    #     for j in range(1,11):
    #         result = i*j
    #         print(f"{result:4}", end="")
    #     print()
                

    
 
 
if __name__ == "__main__":
    main()
