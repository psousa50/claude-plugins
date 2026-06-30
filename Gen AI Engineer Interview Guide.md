## **Gen AI Engineer Interview Guide**

### **Intros (\< 5 mins)**

* Introduce interviewers \- flag associate/employee status  
* Candidate introduction  
* Explain interview phases: exercise walkthrough → experience discussion → technical depth → know us

---

### **Exercise Walkthrough (25 mins)**

**Candidate shares screen**

Walk us through your solution as if explaining to another Gen AI engineer. Focus on your key decisions and rationale.

#### **Evaluation Criteria:**

**RAG Pipeline Design**

* Chunking strategy and rationale (size, overlap, simple vs advanced)  
* Retrieval approach ( top-k values, changes on the original prompt )

**Quality & Optimization (Not mandatory but good to see if it’s done well)**

* Any text preprocessing/cleaning approach  
* Some candidates go for a Re-ranking implementation (cross-encoder, hybrid search)  
* Did the candidate change the default temperature value?

**Evaluation & Testing**

* Evaluation tool and metrics used (such as generic metrics: faithfulness, answer relevance, context precision)  
* Look for Evaluation metrics that are not generic  
* How they validated results  
* Iteration process based on evaluation  
* Software Testing approach and coverage

**Engineering Practices**

	**(This should follow the exercise rubric practices)**

* Code organization and modularity  
* Configuration management  
* Error handling  
* Dependency management

Ask about:

* How would you evaluate RAG quality systematically?  
* What would change to handle 10M+ documents with real-time updates?  
* How would you prevent hallucinations and ensure factual accuracy?  
* What monitoring would you implement in production?

---

### **Experience Deep Dive (20 mins)**

Walk us through a Gen AI project you're proud of or found challenging.

#### **Areas to Explore:**

**Problem Definition**

* What was the actual problem? (Watch for AI-for-AI's-sake vs genuine need)  
* Why was Gen AI the right solution vs alternatives?  
* How did they navigate hype vs pragmatism?

**Technical Implementation**

* Architecture decisions (model selection, hosting, orchestration)  
* Prompt engineering approach  
* RAG vs fine-tuning vs both \- why?  
* Agentic Architectures  
* Handling model limitations and failure modes  
* LLM Observability  
* Cost Tracking

**Stakeholder Management**

* How did they set realistic expectations about AI capabilities?  
* Managing non-technical stakeholders' understanding  
* Handling requests for unrealistic features  
* Demonstrating value and ROI

**Trade-offs & Outcomes**

* What would they do differently?  
* How did they measure success?  
* Production challenges encountered

---

### **Getting to Know Us (5-10 mins)**

Candidate questions about Equal Experts

