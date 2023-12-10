def convert_to_number(input_str):
    mapping_dict = {"하나": 1, "한": 1, "둘": 2, "두": 2, "셋": 3, "세": 3, "넷": 4, "네": 4, "다섯": 5, "여섯": 6,
                   "일곱": 7, "여덟": 8, "아홉": 9, "열": 10,"열하나": 11,"열한": 11,"열둘": 12,"열두": 12,"열셋": 13,"열세": 13,"열넷": 14,"열다섯": 15,"열여섯": 16,"열일곱": 17,"열여덟": 18,"열아홉": 19,
                   "스물": 20, "스무": 20, "스물하나": 21,"스물한": 21,"스물둘": 22,"스물두": 22,"스물셋": 23,"스물세": 23,"스물넷": 24,"스물다섯": 25,"스물여섯": 26,"스물일곱": 27,"스물여덟": 28,"스물아홉": 29,
                   "서른": 30, "서른하나": 31,"서른한": 31,"서른둘": 32,"서른두": 32,"서른셋": 33,"서른세": 33,"서른넷": 34,"서른다섯": 35,"서른여섯": 36,"서른일곱": 37,"서른여덟": 38,"서른아홉": 39,
                   "마흔": 40, "마흔하나": 41,"마흔한": 41,"마흔둘": 42,"마흔두": 42,"마흔셋": 43,"마흔세": 43,"마흔넷": 44,"마흔다섯": 45,"마흔여섯": 46,"마흔일곱": 47,"마흔여덟": 48,"마흔아홉": 49,
                   "쉰": 50, "쉰하나": 51,"쉰한": 51,"쉰둘": 52,"쉰두": 52,"쉰셋": 53,"쉰세": 53,"쉰넷": 54,"쉰다섯": 55,"쉰여섯": 56,"쉰일곱": 57,"쉰여덟": 58,"쉰아홉": 59, "육십": 60, "칠십": 70, "팔십": 80, "구십": 90, "백": 100, "이백": 200
}
    return mapping_dict.get(input_str, input_str)
# 59까지만

# nm=["하나","한","둘","두","셋","세","넷","다섯","여섯","일곱","여덟","아홉"]
# ten=["열","스물","서른","마흔","쉰"]
# a=[]
# cnt=1
# for i in ten:
#     one=[1,1,2,2,3,3,4,5,6,7,8,9]
#     o=0
#     for j in nm:
#         a.append(f'"{i}{j}": {cnt}{one[o]},')
#         o+=1
#     cnt+=1
# print(''.join(a))