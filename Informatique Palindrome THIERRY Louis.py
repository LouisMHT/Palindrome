"""Projet informatique n°1 : Palindromes dans 2 bases __ THIERRY Louis"""
"""Programme is_palindrome pour savoir si un décimal est un palindrome"""
def is_palindrome(n:int)->bool:
    n = str(n)
    reverse = n[::-1]

    if n == reverse:
        return True
    return False

"""Lecture du programme is_palindrome"""
n = int(input("Entrez un nombre "))

if is_palindrome(n) == True:
    print("C'est un palindrome, le programme répond True")
else:
    print("Ce n'est pas un palindrome, le programme répond False")

""""Programme conv_bin pour convertir un décimal en binaire"""
def conv_bin(n:int)->int:
    n = (bin(n)[2:])
    return n

"""Lecture de la conversion conv_bin"""
print("La conversion binaire vaut ", conv_bin(n))

"""Programme double_palindrome pour savoir si un entier est un palindrome en décimal et en binaire"""
"""Je n'ai pas réussi à faire le programme avec la boucle et la liste, je vous met mon brouillon  """
"""à la fin du programme."""
def double_palindrome(n:int)->list:
    n = str(n)              # Le programme analyse en base 10.
    reverse = n[::-1]
    if n == reverse:
        x = True
    else:
        x = False
    n = int(n)              # Si c'est un palindrome en base 10 alors il analyse en base 2.
    if x == True:
        n = (bin(n)[2:])
        reverse = n[::-1]
    if n == reverse:
        y = True
    else:
        y = False
    if y == True:
        n = int(n, 2)       # Le programme retransforme le binaire en entier et donne sa réponse.
    return n
# Le programme donne le nombre d'origine si c'est un palindrome dans 2 bases.
print("Le nombre", double_palindrome(n), "est un palindrome dans les 2 bases. (ou si écris en binaire, uniquement en décimal.)")

"""Brouillon fonction complète double_palindrome"""
#def double_palindrome(n:int)->list:
#    L = []
#    while (n >= 0):
#        n = str(n)
#        reverse = n[::-1]
#        if n == reverse:
#            x = True
#        else:
#            x = False
#        n = int(n)
#        if x == True:
#            n = (bin(n)[2:])
#            reverse = n[::-1]
#        if n == reverse:
#            y = True
#        else:
#            y = False
#        if y == True:
#            n = int(n, 2)
#            L.append(n)
#            n = n - 1
#        if x == False:
#            n = n - 1
#    n = L
#    n = list(n)
#    return n
#
#print(double_palindrome(n))//
"""La fonction de la boucle while ne fonctionne pas, je n'arrive pas à faire autrement."""