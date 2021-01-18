class Trie:
    def __init__(self):
        self.root = {}
    
    def insertHelper(self, s, root):
        if s == '':
            root['__end__'] = True
            return
        
        if s[0] not in root:
            root[s[0]] = {}
            self.insertHelper(s[1:], root[s[0]])
        else:
            # if "__end__" in root:
            #     del root["__end__"]

            self.insertHelper(s[1:], root[s[0]])
    
    def insert(self, s):
        self.insertHelper(s, self.root)
    
    def isPresentHelper(self, s, root):
        if s == '':
            if '__end__' in root:
                return True
            else:
                return False
        
        if s[0] in root:
            return self.isPresentHelper(s[1:], root[s[0]])
        else:
            return False
    
    def isPresent(self, s):
        return self.isPresentHelper(s, self.root)
    
    def DFS(self, node, w, res):
        if type(node) == type(True):
            res.append(w.replace("__end__", ""))
            return
        
        for letter in node:
            self.DFS(node[letter], w+letter, res)

    def getWords(self):
        result = []
        self.DFS(self.root, '', result)
        return result 
        

if __name__ == '__main__':
    trie = Trie()
    trie.insert("rohit")
    trie.insert("roh")
    trie.insert("revanth")

    # print(trie.isPresent("rocket"))
    # print(trie.isPresent("rohit"))
    print(trie.getWords())

    # print(trie.root)