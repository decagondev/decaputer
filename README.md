# 💻 DecaPuter 🖥️

## 🌟 Overview
A playful Python-based 16-bit computer simulator that brings a custom computing environment to life using Pygame for graphics and rendering.

## 🗂️ Project Structure
```
decaputer/
├── main.py           # 🚀 Entry point for running the simulation
├── cpu.py            # 🧠 CPU implementation
├── memory.py         # 💾 Memory management and bank switching
├── gpu.py            # 🖼️ GPU and rendering logic
├── instruction_set.py # 📋 Definitions for opcodes and instructions
├── program_loader.py  # 📂 Logic to load and parse machine language files
├── utils.py           # 🛠️ Utility functions
└── programs/          # 💾 Example machine language programs
```

## ✨ Key Features
- 🔢 16-bit CPU architecture
- 🏦 8 memory banks of 65,535 bytes each
- 🖥️ 640x480 pixel GPU rendering
- 🧩 Custom instruction set simulator
- 🎮 Pygame-based graphics

## 🛠️ Requirements
- Python 3.8+
- Pygame
- NumPy (recommended)

## 🚧 Development Roadmap
1. 🏗️ Setup and Architecture
2. 🧩 CPU and Memory Operations
3. 🎨 GPU Rendering
4. 📲 Program Loading
5. 🚀 Advanced Features
6. ✅ Testing and Optimization

## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/decagondev/decaputer.git

# Install dependencies
pip install pygame numpy

# Run the simulator
python main.py
```

## 🤝 Contributing
Interested in contributing? Great! 
- Fork the repository
- Create a feature branch
- Submit a pull request

## 📄 License
[MIT](LICENCE)

## 🎮 Simulation Goals
Create a fun, educational simulator that demonstrates:
- Low-level computer architecture
- Custom instruction set design
- Graphics rendering from scratch

## 🧠 Learning Objectives
- Understand CPU fetch-decode-execute cycles
- Explore memory management techniques
- Learn about custom computer architecture design
