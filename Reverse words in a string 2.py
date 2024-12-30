def reverse(s):
    s[:]=s[::-1]
    s+=" "
    st=0
    end=0
    for i in range(len(s)):
        if s[i]==" ":
            while st<end:
                s[st],s[end]=s[end],s[st]
                st+=1
                end-=1
            st=i+1
            end=st
        else:
            end+=1
            
    return s[1:]
