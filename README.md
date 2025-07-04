# Agent Architecture Comparison: ReAct vs Structured Flows

An experimental comparison of two fundamental AI agent paradigms applied to e-commerce sales scenarios.

## 🎯 Overview

This project explores the practical differences between **ReAct agents** (reasoning + acting) and **Structured Workflow agents** (StateGraph-based) in handling customer sales interactions.

**Key Question**: Which architecture performs better for real-world business applications?

## ⚠️ Important Disclaimers

**This is an exploratory experiment, not rigorous research:**

- ❌ **Small sample size** (n=15 test cases)
- ❌ **Single domain** (e-commerce only)
- ❌ **Subjective metrics** (LLM-evaluated)
- ❌ **Limited statistical significance**

**Intended as:**
- ✅ Learning exercise shared publicly
- ✅ Architecture decision exploration
- ✅ Starting point for community discussion
- ✅ Practical comparison methodology

## 🏗️ Architecture Comparison

### ReAct Agent
- **Framework**: LangGraph's `create_react_agent`
- **Approach**: Dynamic reasoning and tool selection
- **Strengths**: Flexibility, handles complex scenarios
- **Weaknesses**: Unpredictable, potentially slower

### Structured Flow Agent  
- **Framework**: StateGraph with defined states
- **Approach**: Fixed pipeline with clear steps
- **Strengths**: Predictable, consistent output
- **Weaknesses**: Less adaptable to edge cases

## 🧪 Experimental Setup

### Test Environment
- **Products**: 27 items across 6 categories
- **Test Cases**: 15 scenarios (basic, ambiguous, multi-product, comparison)
- **Evaluation**: GPT-4 as judge across 5 dimensions
- **Metrics**: Extraction, Information, Process, Communication, Resolution

### Tools Available to Both Agents
- `buscar_producto()` - Product information lookup
- `verificar_stock()` - Stock availability check
- `calcular_precio_total()` - Price calculation with discounts
- `procesar_pedido()` - Order processing

## 📊 Sample Results

*Results vary by test case complexity and type*

| Metric | ReAct | Structured Flow |
|--------|-------|-----------------|
| Success Rate | Variable | Consistent |
| Avg Response Time | Higher variance | Lower variance |
| Complex Cases | Better handling | More rigid |
| Simple Cases | Potential overkill | Efficient |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/agent-architecture-comparison.git
cd agent-architecture-comparison

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your OPENAI_API_KEY to .env

# Run the experiment
python main.py
```

## 📁 Project Structure

```
├── main.py                 # Main experiment runner
├── inventario_completo.json # Product catalog
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
└── README.md              # This file
```

## 🤝 Contributing

This experiment has many opportunities for improvement:

### Easy Improvements
- [ ] Increase test case variety
- [ ] Add more product categories
- [ ] Implement human evaluation baseline
- [ ] Add cost analysis (API calls)

### Advanced Improvements  
- [ ] Statistical significance testing
- [ ] Multi-domain evaluation
- [ ] Latency distribution analysis
- [ ] A/B testing framework

**Pull requests welcome!** Please read our contribution guidelines.

## 💡 Key Insights

*From this limited experiment:*

1. **Context matters more than architecture** - The specific use case drives which approach works better
2. **ReAct excels at complex, ambiguous scenarios** - Better flexibility for edge cases
3. **Structured flows win on consistency** - More predictable behavior and timing
4. **Hybrid approaches may be optimal** - Route simple cases to flows, complex to ReAct

## 🔬 Methodology Limitations

**Statistical Issues:**
- Small sample size limits generalizability
- No confidence intervals or significance testing
- Single evaluator (GPT-4) introduces bias

**Experimental Issues:**
- Toy dataset vs real-world complexity
- Fixed timeout differences between approaches
- No multi-run averaging for stability

**Scope Issues:**
- Single domain (e-commerce) limits applicability
- English-only test cases
- No production environment testing

## 📚 Related Work

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Agent Architecture Patterns](https://blog.langchain.dev/planning-for-agents/)

## 📄 License

MIT License - Feel free to use, modify, and share.

## 🙋‍♀️ About

Created by Aina-lluna as a learning exercise in AI agent architectures. 

**Background**: AI Generative Lead exploring practical implications of different agent paradigms for business applications.

**Contact**: [[mi LinkedIn]](https://www.linkedin.com/in/ainataylor/) 

---

*Made with curiosity, shared for learning* 🧠

**⭐ If this helps your understanding of agent architectures, please star the repo!**
