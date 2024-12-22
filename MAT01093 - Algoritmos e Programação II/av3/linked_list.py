'''
Código fornecido no link:
https://github.com/djusto/algoritmos2/blob/master/Lista%20desordenada.md
'''
class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

    def __str__(self):
        if self.next==None:
            x='.'
        else:
            x='->'

        return f"{self.data} {x} "

class UList:
    def __init__(self):
        self.head = None

    def add(self,item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp

    def __str__(self):
        res=''
        current = self.head
        while current != None:
            res=res+ current.__str__()
            current = current.next

        return res

    def search(self,item):
        current = self.head
        achou   = False
        while current != None and not achou:
            if current.data == item:
                achou = True
            else:
                current = current.next

        return achou

    def remove(self,item):
        current  = self.head
        previous = None
        achou    = False
        while not achou:
            if current.data == item:
                achou = True
            else:
                previous = current
                current = current.next

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

    '''
    Início das alterações
    '''
    def remove_multiplos(self, n):
        tmp      = Node(0)
        tmp.next = self.head
        current  = tmp

        while current.next is not None:
            if current.next.data % n == 0:
                current.next = current.next.next
            else:
                current = current.next

        self.head = tmp.next

    '''
    A ideia é usarmos 'tmp' como um node auxiliar na 1° posição para percorrer a lista olhando sempre para o próximo node.
    Com isso percorremos com while e verificamos se o valor no next é múltiplo de n.
    Caso for múltiplo passamos o next ao valor seguinte na lista:
    Ex:
    1 -> (3) -> 4 -> 5, n = 2.
    1 -> (3) ->-> 5
    '''

def run_tests():
    # Test case descriptions
    test_cases = [
        {"description": "Lista com múltiplos e não múltiplos de n",
         "input": [9, 8, 3, 6, 4, 7, 5, 18, 1], "n": 2, "expected": [9, 3, 7, 5, 1]},

        {"description": "Todos os elementos são múltiplos de n",
         "input": [2, 4, 6, 8, 10], "n": 2, "expected": []},

        {"description": "Nenhum elemento é múltiplo de n",
         "input": [3, 5, 7, 11, 13], "n": 2, "expected": [3, 5, 7, 11, 13]},

        {"description": "Primeiro e último elementos são múltiplos de n",
         "input": [10, 3, 5, 7, 20], "n": 5, "expected": [3, 7]},

        {"description": "Lista com um único elemento que é múltiplo de n",
         "input": [4], "n": 2, "expected": []},

        {"description": "Lista com um único elemento que não é múltiplo de n",
         "input": [7], "n": 2, "expected": [7]},

        {"description": "Lista vazia",
         "input": [], "n": 3, "expected": []},

        {"description": "Múltiplos consecutivos de n no meio da lista",
         "input": [1, 2, 4, 6, 7, 8, 10], "n": 2, "expected": [1, 7]},

        {"description": "n maior que todos os valores na lista",
         "input": [1, 3, 5, 7], "n": 10, "expected": [1, 3, 5, 7]},

        {"description": "Lista contendo elementos negativos e positivos",
         "input": [-4, -3, -2, 1, 2, 3, 4], "n": 2, "expected": [-3, 1, 3]}
    ]

    passed_count = 0
    failed_count = 0

    # Run tests
    for i, case in enumerate(test_cases):
        print("=====================")
        print(f"Test Case {i + 1}: {case['description']}")
        print(f"Input: {case['input']}, n = {case['n']}")

        # Create the list
        L = UList()
        for value in reversed(case["input"]):  # Add values in reversed order
            L.add(value)

        # Apply remove_multiplos
        L.remove_multiplos(case["n"])

        # Collect the result
        result = []
        current = L.head
        while current:
            result.append(current.data)
            current = current.next

        # Print result and status
        print(f"Output: {result}")
        if result == case["expected"]:
            print("Passed")
            passed_count += 1
        else:
            print("Failed")
            print(f"Expected: {case['expected']}")
            failed_count += 1
        print("=====================")

    # Final summary
    total_tests = len(test_cases)
    print("\n====== TEST SUMMARY ======")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print("===========================")


# Example usage
if __name__ == "__main__":
    run_tests()
