import numpy as np

class CPU:
    def __init__(self, memory, gpu):
        self.registers = np.zeros(16, dtype=np.uint16)  # R0-R15
        
        self.SP = np.uint16(0)     # Stack Pointer
        self.BP = np.uint16(0)     # Base Pointer
        self.IP = np.uint16(0)     # Instruction Pointer
        self.BR = np.uint8(0)      # Bank Register
        
        self.zero_flag = False
        self.carry_flag = False
        self.overflow_flag = False
        
        self.memory = memory
        self.gpu = gpu
        
        self.instruction_set = {
            # Data Movement
            0x01: self.mov,
            0x02: self.load,
            0x03: self.store,
            
            # Arithmetic
            0x10: self.add,
            0x11: self.sub, 
            0x12: self.mul,
            0x13: self.div,
            
            # Logical
            0x20: self.and_op,
            0x21: self.or_op,
            0x22: self.xor_op,
            0x23: self.not_op,
            
            # Control Flow
            0x30: self.jmp,
            0x31: self.jz,
            0x32: self.jnz,
            0x33: self.call,
            0x34: self.ret,
            
            # Stack Operations
            0x40: self.push,
            0x41: self.pop,
            
            # Bank Management
            0x50: self.bank_switch
        }

    def fetch(self):
        """Fetch next instruction from memory"""
        self.memory.set_bank(self.BR)
        instruction = self.memory.read_word(self.IP)
        self.IP += 2
        return instruction

    def decode(self, instruction):
        """Decode instruction into components"""
        opcode = (instruction >> 10) & 0x3F
        src_reg = (instruction >> 6) & 0x0F
        dest_reg = (instruction >> 2) & 0x0F
        immediate = instruction & 0x03
        
        return opcode, src_reg, dest_reg, immediate

    def execute(self, opcode, src_reg, dest_reg, immediate):
        """Execute decoded instruction"""
        if opcode in self.instruction_set:
            return self.instruction_set[opcode](src_reg, dest_reg, immediate)
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    def cycle(self):
        """Fetch-Decode-Execute Cycle"""
        try:
            instruction = self.fetch()
            opcode, src_reg, dest_reg, immediate = self.decode(instruction)
            self.execute(opcode, src_reg, dest_reg, immediate)
        except Exception as e:
            print(f"CPU Error: {e}")

    
    def mov(self, src_reg, dest_reg, immediate):
        """Move data between registers or load immediate"""
        if immediate:
            
            self.registers[dest_reg] = (src_reg << 8) | immediate
        else:
            self.registers[dest_reg] = self.registers[src_reg]

    def load(self, src_reg, dest_reg, immediate):
        """Load value from memory to register"""
        address = self.registers[src_reg]
        self.memory.set_bank(self.BR)
        self.registers[dest_reg] = self.memory.read_word(address)

    def store(self, src_reg, dest_reg, immediate):
        """Store register value to memory"""
        address = self.registers[dest_reg]
        self.memory.set_bank(self.BR)
        self.memory.write_word(address, self.registers[src_reg])


    def add(self, src_reg, dest_reg, immediate):
        """Add two registers"""
        result = self.registers[dest_reg] + self.registers[src_reg]
        

        self.overflow_flag = result > 0xFFFF
        self.zero_flag = result == 0
        self.carry_flag = result > 0xFFFF
        
        self.registers[dest_reg] = result & 0xFFFF

    def sub(self, src_reg, dest_reg, immediate):
        """Subtract two registers"""
        result = self.registers[dest_reg] - self.registers[src_reg]
        

        self.carry_flag = result < 0
        self.zero_flag = result == 0
        
        self.registers[dest_reg] = result & 0xFFFF

    def mul(self, src_reg, dest_reg, immediate):
        """Multiply two registers"""
        result = self.registers[dest_reg] * self.registers[src_reg]
        

        self.overflow_flag = result > 0xFFFF
        self.zero_flag = result == 0
        
        self.registers[dest_reg] = result & 0xFFFF

    def div(self, src_reg, dest_reg, immediate):
        """Divide two registers"""
        if self.registers[src_reg] == 0:
            raise ValueError("Division by zero")
        
        result = self.registers[dest_reg] // self.registers[src_reg]
        remainder = self.registers[dest_reg] % self.registers[src_reg]
        

        self.zero_flag = result == 0
        self.registers[dest_reg] = result
        

        self.registers[0] = remainder


    def and_op(self, src_reg, dest_reg, immediate):
        """Bitwise AND"""
        result = self.registers[dest_reg] & self.registers[src_reg]
        self.zero_flag = result == 0
        self.registers[dest_reg] = result

    def or_op(self, src_reg, dest_reg, immediate):
        """Bitwise OR"""
        result = self.registers[dest_reg] | self.registers[src_reg]
        self.zero_flag = result == 0
        self.registers[dest_reg] = result

    def xor_op(self, src_reg, dest_reg, immediate):
        """Bitwise XOR"""
        result = self.registers[dest_reg] ^ self.registers[src_reg]
        self.zero_flag = result == 0
        self.registers[dest_reg] = result

    def not_op(self, src_reg, dest_reg, immediate):
        """Bitwise NOT"""
        result = ~self.registers[src_reg] & 0xFFFF
        self.zero_flag = result == 0
        self.registers[dest_reg] = result

    # Control Flow Instructions
    def jmp(self, src_reg, dest_reg, immediate):
        """Unconditional jump"""
        self.IP = self.registers[dest_reg]

    def jz(self, src_reg, dest_reg, immediate):
        """Jump if zero flag is set"""
        if self.zero_flag:
            self.IP = self.registers[dest_reg]

    def jnz(self, src_reg, dest_reg, immediate):
        """Jump if zero flag is not set"""
        if not self.zero_flag:
            self.IP = self.registers[dest_reg]

    def call(self, src_reg, dest_reg, immediate):
        """Function call with stack management"""

        self.SP -= 2
        self.memory.write_word(self.SP, self.IP)

        self.IP = self.registers[dest_reg]

    def ret(self, src_reg, dest_reg, immediate):
        """Return from function"""

        self.IP = self.memory.read_word(self.SP)
        self.SP += 2


    def push(self, src_reg, dest_reg, immediate):
        """Push register value to stack"""
        self.SP -= 2
        self.memory.write_word(self.SP, self.registers[src_reg])

    def pop(self, src_reg, dest_reg, immediate):
        """Pop value from stack to register"""
        self.registers[dest_reg] = self.memory.read_word(self.SP)
        self.SP += 2


    def bank_switch(self, src_reg, dest_reg, immediate):
        """Switch active memory bank"""
        self.BR = self.registers[src_reg] & 0x07

    def debug_state(self):
        """Print current CPU state for debugging"""
        print("CPU State:")
        for i, reg in enumerate(self.registers):
            print(f"R{i}: {reg}")
        print(f"IP: {self.IP}")
        print(f"SP: {self.SP}")
        print(f"BR: {self.BR}")
        print(f"Flags: Z={self.zero_flag}, C={self.carry_flag}, O={self.overflow_flag}")
