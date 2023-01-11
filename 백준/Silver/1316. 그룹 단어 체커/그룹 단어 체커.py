N = int(input())
count_word = 0

for n in range(N):
    char_list = []
    o = 0
    string = input()

    for i in range(len(string)):
        try:
            if string[i] != string[i+1]:
                if string[i] in char_list:
                    o = 1
                    break
                char_list.append(string[i])
        except:
            if string[i] in char_list:
                    o = 1
                    break
            char_list.append(string[i])   
            pass

    if o == 0:    
        count_word += 1

print(count_word)