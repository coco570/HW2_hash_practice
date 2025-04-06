import matplotlib.pyplot as plt

file = 'hw2_data.txt'

def reading_data():
    with open(file, 'r', encoding = 'utf-8') as data:
        try:
            return data.readlines()
        except IOError:
            print("請排除檔案讀取問題")

def clecking_same_word(lines):
    counting_word = {}
    for line in lines:
        w = line.strip()
        if w in counting_word:
            counting_word[w] += 1
        else:
            counting_word[w] = 1
    return counting_word

def data_sorting(word_count):
    return dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))

def picture_painting_bar(sorted_data):
    categories = list(sorted_data.keys())
    number = list(sorted_data.values())
    data_len = list(range(1, len(number)+1))
    
    plt.figure(figsize=(12, 6))
    plt.bar(data_len, number, width=0.5, edgecolor='black', color='skyblue')
    
    for index in range(len(data_len)):
        plt.text(data_len[index], number[index], str(number[index]), ha='center', va='bottom', fontsize=8)

    plt.title('Word appearing frequency bar picture')
    plt.ylabel('Times/word')
    plt.xlabel('Catergories')
    
    plt.xticks(data_len, categories, rotation=45)
    plt.tight_layout()
    plt.show()

def question_answer(sorted_data):
    print("1. 總共有多少個不重複的英文字：", len(sorted_data))
    print("2. 每一個英文字出現次數如下：")
    for word, count in sorted_data.items():
        print(f"{word}: {count}")

def main():
    lines = reading_data()
    counting_word = clecking_same_word(lines)
    sorted_data = data_sorting(counting_word)
    picture_painting_bar(sorted_data)
    question_answer(sorted_data)

if __name__ == "__main__":
    main()
