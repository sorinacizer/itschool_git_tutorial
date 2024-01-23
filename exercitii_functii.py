'''1.	Dureaza mai mult sa adaugi elemente cu append intr-o lista sau sa folosesti list comprehension?
Creeaza 2 functii care returneaza timpul necesar celor 2 operatiuni.
Poti folosi time.time() pentru a obtine timpul curent.'''
# import time
#
#
# def time_append(n):
#     start_time = time.time()
#     lst = []
#     for i in range(n):
#         lst.append(i)
#     end_time = time.time()
#     return end_time - start_time
#
#
# def time_list_comprehension(n):
#     start_time = time.time()
#     new_lst = [i for i in range(n)]
#     end_time = time.time()
#     return end_time - start_time
#
#
# print(time_append(100000))
# print(time_list_comprehension(100000))

'''2.	Se da un string s. Scrie o functie care returneaza suma caracterelor de tip cifra din s.
Modifica functia astfel incat sa returneze suma numerelor din s. Un numar este reprezentat de caractere numerice alaturate. 
ex:
s = 'eu am 33 de ani. in 2 luni va fi ziua mea de nume'
result: 35'''
# def sum_numbers(string: str) -> int:
#     """Returns sum of numbers from a string"""
#     sum = 0
#     for i in string.split():
#         if i.isdigit():
#             sum += int(i)
#     return sum
# s = 'eu am 33 de ani. in 2 luni va fi ziua mea de nume'
# print(sum_numbers(s))

'''3.	Scrieti o functie care primeste un numar variabil de argumente de tip lista si returneaza o lista cu toate elementele argumentelor.'''
# def args_in_list(lista :list) -> list:
#     '''Returns all the args in a list'''
#     return [i for i in str(lista) if i.isalpha()]
#
# print(args_in_list(['bun', 'rau', 'frumos']))

'''4.	 Scrieti o functie care primeste numele unui fisier ca parametreu si returneaza tipul acelui fisier.
ex:
def file_type(file_name):
	pass

file_type(‘20221107.jpeg’) -> imagine
file_type(‘test.txt’’) -> text
file_type(‘music_20221107.mp3’) -> muzica'''

# def file_type(file_name: str) -> str:
# 	dic_fis = {
# 		'.jpeg': 'imagine',
# 		'.txt': 'text',
# 		'.mp3': 'muzica'
# 	}
# 	extensie = file_name[file_name.rfind(".")::]
# 	for k, v in dic_fis.items():
# 		if extensie in k:
# 			return v
# 	return None
#
# print(file_type('music_20221107.mp3'))
# print(file_type('test.txt'))
# print(file_type('20221107.jpeg'))

'''5.	Scrieti o functie care determina daca un cuvant contine litere care nu se repeta (este format din caractere unice)
Functia poate returna True sau False'''
# def unic_characters(string: str) -> bool:
# 	for i in string:
# 		if string.count(i) >= 2:
# 			return False
# 		else:
# 			return True
#
# s = input('Enter your string: ')
# print(unic_characters(s))

'''6.	* Se da un numar. Scrie o functie care returneaza numarul ca un string in urmatorul format:
Input: 37 → output: ‘30 + 7’
Input: 114 → output: ‘100 + 10 + 4’
Input: 30165 → output: ‘30000 + 100 + 60 + 5’'''

# def number_format(s: str) -> str:
# 	rezultat = []
# 	for i, cifra in enumerate(s):
# 		exp_10 = len(s) - i - 1
# 		if cifra != '0':
# 			parte_intreaga = int(cifra) * 10 ** exp_10
# 			rezultat.append(str(parte_intreaga))
# 	return ' + '.join(rezultat)
# print(number_format('37'))
# print(number_format('114'))
# print(number_format('30165'))

'''7.	Scrie o functie care returneaza cuvantul cu scorul cel mai mare.
Scorul unui cuvant este dat de suma pozitiilor literelor cuvantului, din alfabet.
Functia primeste ca argument o lista de cuvinte.
ex: 
a = 1, b = 2, c = 3, d = 4, etc
Word: mama, scor: 13 + 1 + 13 + 1 = 30'''
# import string
#
# def get_word_score(word: list) -> int:
#     '''Return score of a word'''
#     alphabet = string.ascii_lowercase
#     s = 0
#     for char in word:
#         s += alphabet.index(char) + 1
#     return s
#
# def get_highest_score(lista: list) -> int:
#     scores = [get_word_score(i) for i in lista]
#     print(scores)
#     return max(scores)
#
# print(get_highest_score(['mama', 'tata']))

'''8.	Se dau 3 tupluri ca input. Fiecare dintre aceste tupluri contine urmatoarele informatii (nume, varsta, inaltime) Afiseaza cele 3 tupluri, dupa sortarea
 (a-z) si in ordine crescatoare, tinand cont, pe rand, de nume, varsta si inaltime. 
Ex. 
input: (Dan, 33, 170), (Mihai, 20, 180), (Daniel, 40, 173) 
dupa nume: (Dan, 33, 170), (Daniel, 40, 173), (Mihai, 20, 180) 
dupa varsta: (Mihai, 20, 180), (Dan, 33, 170), (Daniel, 40, 173) 
dupa inaltime: (Dan, 33, 170), (Daniel, 40, 173), (Mihai, 20, 180)'''

# def sort_by_age(data: tuple) -> list:
#     ages = tuple(age[1] for age in data)
#     sorted_ages = sorted(ages)
#     lst = []
#     for i in sorted_ages:
#         for j in data:
#             if i == j[1]:
#                 lst.append(j)
#     return lst
#
# def sort_by_height(data: tuple) -> list:
#     heights = tuple(h[2] for h in data)
#     sorted_heights = sorted(heights)
#     lst = []
#     for i in sorted_heights:
#         for j in data:
#             if i == j[2]:
#                 lst.append(j)
#     return lst
#
# if __name__ == "__main__":
#     tuples = [("Dan", 33, 170), ("Mihai", 20, 180), ("Daniel", 40, 173)]
#     print(f'Sortarea dupa nume: {sorted(tuples)}')
#     print(f'Sortarea dupa varsta: {sort_by_age(tuples)}')
#     print(f'Sortarea dupa inaltime: {sort_by_height(tuples)}')

'''9.	Se da o lista de intregi. Pentru fiecare element din lista sa se determine cate numere din cadrul acelei liste sunt mai mici decat acel element. 
Rezultatul se returneaza tot intr-o lista 
Ex. nbs = [3, 7, 8, 5] 
output: [0, 2, 3, 1] 
pentru nbs[0] = 3 nu exista niciun numar mai mic in nbs pentru nbs[1] = 7 exista 2 numere mai mici,  etc'''


# def smaller_numbers(numbers: list) -> list:
#     sorted_numbers = sorted(numbers)
#     ind = {elem: i  for i, elem in enumerate(sorted_numbers)}
#     print(ind)
#     return [ind[num] for num in numbers]
#
#
# if __name__ == "__main__":
#     nbs = [3, 7, 8, 5]
#     print(smaller_numbers(nbs))


'''11.	Fie un string s care contine cuvinte separate de unul sau mai multe spatii. Sa se returneaza un string cu toate cuvintele inversate si separate de un singur spatiu.
Ex. input s = 'python java        javascript'
output: 'javascript java python'''
# def inversed_words(text: str) -> str:
#     new_str_lst = text.split()[::-1]
#     return ' '.join(new_str_lst)
#
# if __name__ == '__main__':
#     s = 'python java        javascript'
#     print(inversed_words(s))

'''10.	* Fie un intreg pozitiv n, dat ca input. Scrie o aplicatie care sa printeze o forma triunghiulara realizata din caracterul '*'.
n reprezinta numarul de randuri ale acestui pattern. Numarul de pe fiecare rand va creste cu 2.'''

def star_tree(n: int):
    for i in range(1, n+1):
        rand = '*' * (2*i - 1)
        print(rand)
    return None

if __name__ == '__main__':
    n = int(input('n = '))
    print(star_tree(n))