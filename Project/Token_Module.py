import convert_to_number1 as ctn

def get_number_tokens(text, model, tokenizer):
   
    tokenized_text=tokenizer.tokenize(text)
    
    number_tokens=[]

    for i in range(len(tokenized_text)):
        tokenized_text[i]=ctn.convert_to_number(tokenized_text[i])
        try:
            number_tokens.append(int(tokenized_text[i]))
        except ValueError:
            pass

    return number_tokens

def get_word_tokens(text, number_tokens, model, tokenizer):
    tokenized_text=tokenizer.tokenize(text)
    tokens=[]
    word_tokens=[]
    replace_numbers=[]

    for i in range(len(tokenized_text)):
        tokens.append(ctn.convert_to_number(tokenized_text[i]))
        if type(tokenized_text[i])==str and type(tokens[i])==int:
            replace_numbers.append(tokens[i])  

    decoded_sentence = tokenizer.decode(tokenizer.convert_tokens_to_ids(tokens))
    words=decoded_sentence.split(' ')

    cnt = 0
    for i in range(len(words)):
        if words[i] == '[UNK]':
            if cnt < len(replace_numbers):
                words[i] = replace_numbers[cnt]
                cnt += 1
    cnt=0
    for i in range(len(words)):
        if cnt>=len(number_tokens):
                break
        if str(words[i]).find(str(number_tokens[cnt]))!=-1:
            words[i]=str(words[i]).replace(str(number_tokens[cnt]),'')
            cnt+=1
            if words[i]=='':
                words.pop(i)
            try:
                word_tokens.append([words[i-1], words[i]])
            except TypeError:
                print("(index때메 버그 뜰수도)오류나는 문제: "+text)
                return None
    return word_tokens