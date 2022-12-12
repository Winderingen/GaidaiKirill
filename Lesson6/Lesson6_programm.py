def f(S):
    C=S.replace('а','')
    print(len(S)-len(C))    
S=input()
print(f(S))