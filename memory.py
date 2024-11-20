class Memory:
    def __init__(self, num_banks=8, bank_size=65535):
        self.num_banks = num_banks
        self.bank_size = bank_size
        self.banks = [bytearray(bank_size) for _ in range(num_banks)]
        self.current_bank = 0

    def set_bank(self, bank):
        """Set the current active bank"""
        if 0 <= bank < self.num_banks:
            self.current_bank = bank
        else:
            raise ValueError(f"Invalid bank: {bank}")

    def read_byte(self, address):
        """Read a byte from the current bank"""
        return self.banks[self.current_bank][address]

    def write_byte(self, address, value):
        """Write a byte to the current bank"""
        self.banks[self.current_bank][address] = value & 0xFF

    def read_word(self, address):
        """Read a 16-bit word from the current bank"""
        low = self.read_byte(address)
        high = self.read_byte(address + 1)
        return (high << 8) | low

    def write_word(self, address, value):
        """Write a 16-bit word to the current bank"""
        self.write_byte(address, value & 0xFF)
        self.write_byte(address + 1, (value >> 8) & 0xFF)
