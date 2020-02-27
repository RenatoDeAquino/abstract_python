from abc import ABC, abstractclassmethod
import os
class funciona_vai_nunca_te_pedi_nada(ABC):
    @abstractclassmethod
    def Uniao(self,a,b):
        pass
    @abstractclassmethod
    def Intersect(self,a,b):
        pass
    @abstractclassmethod
    def Diferenca(self,a,b):
        pass
    @abstractclassmethod
    def Membro(self,x,a):
        pass
    @abstractclassmethod
    def Cria_conj_vazio(self,a):
        pass
    @abstractclassmethod
    def Insere(self,x,a):
        pass
    @abstractclassmethod
    def Remove(self,x,a):
        pass
    @abstractclassmethod
    def Atribui(self,a,b):
        pass
    @abstractclassmethod
    def Max(self,a):
        pass
    @abstractclassmethod
    def Min(self,a):
        pass
    @abstractclassmethod
    def Igual(self,a,b):
        pass

class Todos(funciona_vai_nunca_te_pedi_nada):
    def Uniao(self,a,b):
        self.a = set(a)
        self.b = set(b)
        return self.a.union(self.b)
    def Intersect(self,a,b):
        self.a = set(a)
        self.b = set(b)
        return self.a.intersection(self.b)
    def Diferenca(self,a,b):
        self.a = set(a)
        self.b = set(b)
        return self.a - self.b
    def Membro(self,x,a):
        if x in a:
            return True
        else:
            return False
    def Cria_conj_vazio(self,a):
        self.a.clear()
        print("vazio filho")
        return self.a
    def Insere(self,x,a):
        a.append(x)
        print("Foi patrao")
    def Remove(self,x,a):
        if x in a:
            a.pop(x)
        else:
            print("numero n se encontra pai")
    def Atribui(self,a,b):
        self.a = set(a)
        self.b = set(b)
        a = b
        return self.a
    def Max(self,a):
        return max(self.a)
    def Min(self,a):
        return min(self.a)
    def Igual(self,a,b):
        self.a = set(a)
        self.b = set(b)
        if (self.a == self.b):
            return True
        else:
            return False

vai = Todos()

menu = 40028922

while(menu != 3):
        menu = int(input("O que deseja fazer milord:\n1)Colocar valores no array\n2)Ver Os arrays\n3)Sair\n\nQual operação deseja fazer\n4)União\n5)Interseção\n6)Diferença\n7)Membro\n8)Esvaziar conjunto\n9)Inserir\n10)Remover\n11)Atribuir\n12)Mínimo\n13)Máximo\n14)Igual\nOpção --> "))
        if(menu == 1):
            array_one_1 = input("Digite os números para a primeira Array -> ")
            array_one = array_one_1.split(" ")
            array_two_1 = input("Digite os números para a segunda Array -> ")
            array_two = array_two_1.split(" ")
            os.system("clear")
            #Finish here
        if(menu == 2):
            os.system("clear")
            print(f"Array 1 --> {array_one}\nArray 2 --> {array_two}")
        if(menu == 4):
            os.system("clear")
            print(vai.Uniao(array_one,array_two))
        if(menu == 5):
            os.system("clear")
            print(vai.Intersect(array_one,array_two))
        if(menu == 6):
            os.system("clear")
            print(vai.Diferenca(array_one,array_two))
        if(menu == 7):
            os.system("clear")
            user = input("Digite o número desejado --> ")
            print("Resultado -> ",vai.Membro(user,array_one))
        if(menu == 8):    
            os.system("clear")
            vai.Cria_conj_vazio(array_one)
        if(menu == 9):
            os.system("clear")
            user_a = input("Digite o valor a ser inserido --> ")
            vai.Insere(user_a,array_one)
        if(menu == 10):
            os.system("clear")
            user_b = input("Digite o valor a ser removido --> ")
            vai.Remove(user_b,array_one)
        if(menu == 11):
            os.system("clear")
            print(vai.Atribui(array_one,array_two))
        if(menu == 12):
            os.system("clear")
            print(vai.Min(array_one))
        if(menu == 13):
            os.system("clear")
            print(vai.Max(array_one))
        if(menu == 14):
            os.system("clear")
            print("Resultado --> ",vai.Igual(array_one,array_two))