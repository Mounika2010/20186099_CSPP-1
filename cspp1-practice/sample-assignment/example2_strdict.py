d = {}
def search(var):
    L = []
    for k in d:
        if var in d[k]:
            L.append(k)
    return L


def create_dictionary(List,n):
    for i in range(0,len(List),2):
        if str(List[i]) not in d:
            d[str(List[i])] = (List[i+1]).split(",")
    return d

def main():
    n = int(input())
    L = []
    for i in range(n):
        list_input = input().split(" ")
        L.extend(list_input)
    print(create_dictionary(L,n))
main()
print(search(input()))
