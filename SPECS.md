# 💻 DecaPuter Technical Specification

## 🧠 CPU Architecture Overview
### 🔢 Registers Detailed Breakdown
#### General Purpose Registers
- 16 Registers (R0 - R15)
  - Each 16-bit wide
  - Multipurpose computational registers
  - Can store data, memory addresses, or intermediate calculation results

#### 🏷️ Special Purpose Registers
- SP (Stack Pointer): 16-bit
  - Tracks the top of the call stack
  - Manages function call context and local variables
- BP (Base Pointer): 16-bit
  - Provides a stable reference point for stack frames
  - Helps in accessing function arguments and local variables
- IP (Instruction Pointer): 16-bit
  - Tracks the current instruction being executed
  - Automatically incremented after each instruction
- BR (Bank Register): 3-bit
  - Selects active memory bank (0-7)
  - Enables bank switching for extended memory access

### 📊 Instruction Set Architecture

#### 🔄 Data Movement Instructions
- `MOV`: Move data between registers
  - Supports register-to-register transfer
  - Immediate value loading
- `LOAD`: Load data from memory to register
- `STORE`: Store register data to memory

#### 🧮 Arithmetic Operations
- `ADD`: Addition (16-bit)
  - Supports register-to-register addition
  - Immediate value addition
- `SUB`: Subtraction (16-bit)
- `MUL`: Multiplication (16-bit)
- `DIV`: Division (16-bit)
  - Includes overflow and remainder handling

#### 🔬 Logical Operations
- `AND`: Bitwise AND operation
- `OR`: Bitwise OR operation
- `XOR`: Bitwise XOR operation
- `NOT`: Bitwise negation
- Bit manipulation and logical comparisons

#### 🚦 Control Flow Instructions
- `JMP`: Unconditional jump
  - Absolute and relative addressing modes
- `JZ`: Jump if zero flag set
- `JNZ`: Jump if zero flag not set
- `CALL`: Function call with stack management
- `RET`: Return from function, restoring stack state

## 💾 Memory Architecture
### 🏦 Memory Bank Design
- 8 independent memory banks
- Each bank: 65,535 bytes (64 KB)
- Total addressable memory: 512 KB
- Bank switching mechanism:
  - BR register selects active bank
  - Seamless bank transition
  - No performance penalty for bank switching

### 🔍 Memory Access Modes
- Direct addressing
- Indirect addressing via registers
- Indexed addressing
- Base+offset addressing

## 🖥️ GPU Specifications
### 📺 Display Characteristics
- Resolution: 640x480 pixels
- Color Modes:
  - Monochrome (1-bit)
  - 4-bit color (16 colors)
  - Optional grayscale rendering

### 🎨 Rendering Capabilities
- Pixel-level manipulation
  - `poke`: Set individual pixel color
  - `peek`: Read pixel color/state
- Character rendering
  - Bitmap font support
  - Fixed-width character display
  - Multiple font sizes (8x8, 8x16)

## 📝 Instruction Encoding
### 16-bit Instruction Format
```
| Opcode (6 bits) | Src Reg (4 bits) | Dest Reg (4 bits) | Immediate/Offset (2 bits) |
```
- Compact instruction representation
- Supports immediate values
- Flexible register addressing

## 🔄 Execution Cycle
1. 🖊️ Fetch instruction from memory
   - Use Instruction Pointer (IP)
   - Retrieve 16-bit instruction
2. 🔍 Decode instruction
   - Parse opcode
   - Identify source/destination registers
3. ⚙️ Execute instruction
   - Perform specified operation
   - Update registers
   - Manage control flow
4. 📊 Update system state
   - Modify IP
   - Handle flags (zero, carry, overflow)
5. 🖼️ Render graphics
   - Update pixel buffer
   - Refresh display

## 🚀 Performance Considerations
- Cycle-accurate simulation
- Minimal overhead design
- Efficient bank switching
- Fast instruction decoding

## 🧪 Error Handling
- Divide by zero protection
- Overflow detection
- Bank access validation
- Instruction range checking
