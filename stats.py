def count(text):
    length=len(text.split())
    return length
def word_counter(text):
    lower_text=text.lower()
    count_dict = {}
    for characters in lower_text:
        if characters in count_dict:
            count_dict[characters] += 1
        elif characters == " ":
            continue
        else:
            count_dict[characters] = 1
    return(count_dict)
def sorted_list(input_dictionary):
    dict_into_list = []
    for key,value in input_dictionary.items():
        temp_dict = {key: value}
        dict_into_list.append(temp_dict)
    dict_into_list.sort(key=lambda d: list(d.values())[0], reverse=True)
    
    for item in dict_into_list:
        for key,value in item.items():
            print(f"{key}: {value}")
