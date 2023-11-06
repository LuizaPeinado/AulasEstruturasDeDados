class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def _init_(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Função de hash simples para este exemplo
        return len(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            # A posição está vazia, criamos um novo nó
            self.table[index] = Node(key, value)
        else:
            # Lidando com colisões usando lista ligada
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    # Atualiza o valor se a chave já existe
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                # Atualiza o valor se a chave já existe
                current.value = value
            else:
                # Adiciona um novo nó no final da lista
                current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

# Exemplo de uso
hash_table = HashTable(10)
hash_table.insert("Go", "Linguagem de Programação")
hash_table.insert("Swift", "Linguagem de Programação")
hash_table.insert("JavaScript", "Linguagem de Programação")

# Busca um valor
print(hash_table.search("Go"))  # Output: "Linguagem de Programação"

# Remove um valor
hash_table.remove("Swift")
print(hash_table.search("Swift"))  # Output: None (não encontrado)