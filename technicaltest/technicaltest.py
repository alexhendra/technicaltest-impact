def count_vocal(text: str):
    result = 0
    text_vocal = "aiueo"
    for c in text:
        if c.lower() in text_vocal:
            result+=1

    print(f"Total huruf vocal: {result}")


def print_opensource():
    for x in range(1, 100):
        text = x
        if (x%3 == 0) and (x%7 == 0): 
            text = "OpenSource"
        elif x%7 == 0:
            text="Source"
        elif x%3 == 0:
            text="Open"
        
        print(text)


def find_max_recursive(list_number, cur_idx=0):
    result = list_number[cur_idx]
    if len(list_number) <= 0:
        return
    
    if cur_idx+1 >= len(list_number):
        print("Max number: ", result)
        return
    
    if list_number[cur_idx+1] > list_number[cur_idx]:
        result = list_number[cur_idx+1]
    
    find_max_recursive(list_number, cur_idx+1)
    
    return result


