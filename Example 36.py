vowels = ['й','у','е','ы','а','о','э','я','и','ю','Й','Е','Ы','А','О','Э','Я','И','Ю']
phrases = input("Введите стихотворение: ").split()
syllables = []

for phrase in phrases:
    syllables.append(len([char for char in phrase if char in vowels]))

if len(set(syllables)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")