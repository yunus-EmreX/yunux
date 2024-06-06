class MemoryManager:
    def __init__(self):
        self.memory = {}

    def allocate(self, var_name, value):
        self.memory[var_name] = value

    def get(self, var_name):
        return self.memory.get(var_name, None)

if __name__ == "__main__":
    mm = MemoryManager()
    mm.allocate("a", 5)
    print(mm.get("a"))
