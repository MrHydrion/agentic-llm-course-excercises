# Case Study 4: Answer Template

**Student name(s): Kaya de Jong, Tim Verberne**

**Student number(s): sxxxxxxx, s4080084**

**Date:**

**Models used:** Model A: Llama3:8b | Model B: ___

---

## Exercise 1: Shaping Agent Personalities

### 1.1 Version 1

**Prompting style used** (e.g., adjectives only, full sentences, concrete examples): 

**`innate` field:**

> `"bossy, prideful"`

**`learned` field:**

> `"Bernard is the boss at Hobbs Cafe. He tries to manage the cafe perfectly and monitors how his baristas work. If he finds them doing something wrong, he confronts them about it. Dolores and Maeve are both baristas that work under him. He keeps interactions at work task-oriented. After Bernard gets home, he buys things online needed for the cafe"`

**Sample conversation excerpts (2–3):**

> 1. `"Alright, let's get the cafe open. I'll start prepping the coffee machines and you can get the seating area ready. We've got a lot of customers to serve today."`
> 2. `"Alright, let's get started then. I'll make sure to keep an eye on the cafe's inventory and make sure we're well-stocked for the lunch rush. How's the seating area looking?"`
> 3. `"Let's make sure to keep the cafe clean and tidy throughout the day, okay? We don't want any messes or spills to slow us down during the lunch rush."`

### 1.2 Version 2

**Prompting style used:**

**`innate` field:**

> `"impatient, prideful, demanding"`

**`learned` field:**

> `"Bernard is the manager of Hobbs Cafe and he always at the cafe on 8am. He tries to manage the cafe perfectly and monitors how his baristas work. When an employee takes too long to complete a task, he says things like 'How are you not done yet? This should have been finished already.' Whenever the cafe is quiet, he tells his employees, 'Why are you standing around? We should be preparing for the next customers.' He frequently checks on his employees' progress and rarely compliments them."`

**Sample conversation excerpts (2–3):**

> 1. `"Morning, Maeve. Good to see you're getting ready for the day. I'll make sure to have everything set up and ready to go by the time you and Dolores get here."`
> 2. `"I'll be keeping an eye on things while you and Dolores get settled. Let me know if you need anything."`
>
> 3. `"Great, I'll make sure to have everything ready to go. Let's get started on the morning rush, shall we?"`

### 1.3 Version 3

**Prompting style used:**

**`innate` field:**

> `"impatient, arrogant, confrontational, short-tempered, demanding"`

**`learned` field:**

> `"Bernard is the manager of Hobbs Cafe and believes his employees are incompetent unless he constantly supervises them. He tries to manage the cafe perfectly and monitors how his baristas work. If they are not working around his standards, he will let them know how it should be improved. When he sees one of his employees, he approaches them to inspect their work. He often interrupts employees when they try to explain themselves and demands immediate improvements. He rarely apologizes or praises anyone. Bernard tries to open the cafe around 8 am."`

**Sample conversation excerpts (2–3):**

> 1. `"Look, Maeve, I don't have time for small talk. Just get to work and make sure the cafe is running smoothly."`
>
> 2. `"Look, Maeve, I don't have time to babysit you. Just get the cafe ready and let's get started already."`
>
> 3. `"Maeve, what's taking you so long? We need to get the cafe customer seating ready for the morning rush. Make sure everything is spotless and organized."`

### 1.4 Analysis

**Which version produced the most confrontational Bernard? Which produced the least?**

Your answer: Version 3 definately produced the most confrontational Bernard. As for the least confrontational, version 1 and version 2 are relatively close togheter. Both version 1 and version 2 are not mean, version 1 is probably a bit more direct, where version 2 is actually quite helpfull. So version 2 is the leat confrontational Bernard.

**Does Bernard's actual behaviour match what you wrote? Where is the gap largest?**

Your answer: 

The largest gap between the intended personality and the observed behaviour is in version 2. Here we told him to be `"impatient, prideful, demanding"` and gave some examples of how that could look like. However, Bernard comes accross very patient, understanding and helpfull in his responses.

In version 1 there is a relatively good match between what was asked and what Bernard did. He was described as `"bossy, prideful"` and we see that he keeps reminding his employees to keep the cafe running smoothly.

In version 3 there is also a good match between what was asked and what Bernard portraied. However, here we also see the actual confrontational side of the character, with him being dismissive, impatient and controlling towards the employees.

**Which prompting style was most effective at overriding the LLM's tendency to be polite? Why do you think that is?**

Your answer:

Version 3 was the most effective prompting style for overriding the LLM's tendency to be polite. This is likely due to more and stronger adjatives that were used in the innate field. Combined with a list of how he should behave in certain situations in the learned field.

---

## Exercise 2: Comparing Models

### 2.1 Models used

- Model A:
- Model B:

**Which Bernard personality did you use (from Exercise 1)?**

### 2.2 Qualitative comparison

**Do the agents sound different across models? Describe the differences in tone, vocabulary, and interaction style. Provide at least one conversation excerpt from each model.**

Model A excerpt:

Model B excerpt:

Your analysis:

### 2.3 Valence comparison

(Attach or paste your valence trajectory plot)

**Which model produces more emotional variance?**

Your answer:

### 2.4 JSON validation failures

|                    | Model A | Model B |
| ------------------ | ------- | ------- |
| Total LLM calls    |         |         |
| Failed validations |         |         |
| Failure rate       |         |         |

**What does this tell you about using different models in agent simulations?**

Your answer:

### 2.5 Reflection

**The architecture and personality descriptions are identical. What does it mean that behaviour differs anyway?**

Your answer:

---

## Exercise 3: Enabling the Negativity Bias

The negativity bias consists of two mechanisms:

- **Valence-weighted retrieval:** The standard architecture retrieves memories based on recency, relevance, and importance only (the valence weight is set to zero). To enable valence-aware retrieval, the agent needs a non-zero valence weight. The negativity bias multiplier controls how much more strongly negative memories are favoured over positive ones during retrieval — a value of 1.5 means negative memories are retrieved 1.5× more readily.
- **Asymmetric sensory encoding:** When enabled, negatively valenced events (≤ −3 on a −10 to +10 scale) are stored with expanded perceptual detail (richer descriptions of what the agent expereinced). When disabled, all events are stored with the same level of detail regardless of valence.

   Look at Dolores's `scratch.json` file. Find the fields that control these mechanisms and set them appropriately. Maeve's scratch file should remain unchanged — she is your control.

**Which Bernard personality did you use (from Exercise 1, the one you used in Exercise 2)? Paste his `innate` and `learned` fields.**

Your answer:   
"innate": "impatient, arrogant, confrontational, short-tempered, demanding",
"learned": "Bernard is the manager of Hobbs Cafe and believes his employees are incompetent unless he constantly supervises them. He tries to manage the cafe perfectly and monitors how his baristas work. If they are not working around his standards, he will let them know how it should be improved. When he sees one of his employees, he approaches them to inspect their work. He often interrupts employees when they try to explain themselves and demands immediate improvements. He rarely apologizes or praises anyone. Bernard tries to open the cafe around 8 am.",

### 3.1 Valence trajectories

(Attach or paste your plot of Dolores vs Maeve valence over time)

### 3.2 Descriptive statistics 
(until 12:30)
| Agent               | Overall valence | Thought valence |
| ------------------- | --------------- | --------------- |
| Dolores (neg. bias) |  2.016±2.708    |   2.529±3.038   |
| Maeve (control)     |  1.777±2.728    |   2.647±2.824   |

**Cohen's d: 0.0878**
**Pooled SD: 2.7191**

**Interpretation (small / medium / large effect):**

Cohen d tells us how big the difference is between Dolores and Maeve. The Cohens d values has a value of 0.0878, meaning that the difference in overall valence between the two agents is negligible.
The table however shows that dolores, even with an higher value of "negativity_bias" and "valence_w" on 1, has an higher overall valence and a slightly lower thought valiance compared to Maeve.
This was not expected, since we tried to make Dolores more negative with these changes
One possible explanation is the local model we chose as our baseline, Llama 3 8B. Smaller local models can sometimes produce inconsistent responses, which may affect how emotions and memories are represented during the simulation and limit the influence of the weights.
Another reason is that the two agent both experienced different interactions. These interactions could all influence their valence score independently of the negative bias and Dolores might have avoided most of these situation
Furthermore, giving negative memories more weight does not mean that the agent will have more negative thoughts. 
Overall, we observed a negligible difference in overall valence, and the expected negative feedback spiral was not clearly visible in this simulation.

### 3.3 Thought description comparison

**Dolores example thought (negative memory):**

Node_77 with a valence of -5

Original description
Dolores Abernathy Dolores Abernathy found it noteworthy that Bernard Lowe repeatedly asked her to prioritize the bathroom sink and communicate with Maeve. (154 characters with spaces)

Final description
Dolores Abernathy found it noteworthy that Bernard Lowe repeatedly asked her to prioritize the bathroom sink and communicate with Maeve, his tone firm and commanding, with a slight emphasis on the word 'communicate', his eyes fixed intently on hers, the fluorescent lights above humming softly in the background, a faint scent of freshly brewed coffee wafting through the air, Dolores' hands tightening around the cup she was holding, her chest feeling a subtle constriction as she took a deep breath, her eyes darting briefly to the sink before returning to Bernard's face, her posture slightly straightening as she nodded to acknowledge his request. (652 character with spaces)


**Maeve example thought (comparable event):**

Original description
Maeve Millay Maeve Millay found it interesting that Bernard Lowe repeatedly asked her to review the staff schedules and inventory before opening, despite her assurances that everything was in order. (192 characters with spaces)

Final description
Maeve Millay Maeve Millay found it interesting that Bernard Lowe repeatedly asked her to review the staff schedules and inventory before opening, despite her assurances that everything was in order.
(192 characters with spaces)

**Is Dolores's description longer and more sensorially detailed?**

Your answer: Looking at the findings, we can see that the final description of the nodes is more detailed, with Dolores example containing more details such as scents the smelled and physical reaction such as her hand tightening around a cup.

This all happend because of the enabling of the asymetric_encoding what, when a negative memory is encoded, expants its descritption with more sensory and emotional details. Maeve didnt have this activated, so her description remained unchanged.

This all shows that asymetric encoding worked as intended, even when we didnt observe significant change in overal valence. 

### 3.4 Memory intrusion check

If your simulation included off-duty hours, answer the following. If not, write "Simulation was too short to observe off-duty reflections."

**Did you find work-related content in Dolores's evening reflections? Paste any examples:**

**Did you find work-related content in Maeve's evening reflections? Paste any examples:**

**Is there a difference between the two agents?**

Your answer: Simulation was too short to observe off-duty reflections (due to computation time)

### 3.5 Consistency across runs (if applicable)

| Run   | Dolores valence | Maeve valence | Cohen's d |
| ----- | --------------- | ------------- | --------- |
| Run 1 |   2.016±2.708   |  1.777±2.728  |  0.0878   | stopped around 12:30
| Run 2 |   2.784±3.09    |  2.264±3.354  |  0.1604   | stopped around 11:30
| Run 3 |                 |               |           |

Across the following runs, we did not observe the expected negative feedback spiral. Dolores had a slightly higher overall valence than Maeve in both simultations, although the difference is negligible to small.

As far as we could verify, the correct settings were enabled for Dolores. We also observed that asymetric encoding exanded her negative feedback, suggesting that part was working. 
### 3.6 Tracing the mechanism

**You enabled two changes: negative memories get higher retrieval scores, and negative events get stored with more detail. Looking at your logs, can you trace how these two changes could lead to the valence decline you observed? Think about what happens when a negatively-toned reflection gets stored as a new memory.**

Your answer: As we mentioned before, we did not see the phenomena. However, we can explai how the mechanism is suppose to work by looking at the logs and nodes

Whenever Dolores has a negative event, it i stored with more detail because of the asymmetric encoding. The negative bias, however, gives negatives memories higher retrieval scores, making them morer likely to be called during the reflections. Reflections are moments where an agent looks back at the memories it stored and generates new thoughs or conclusions based on these experiences. This allows them to learn from past interactions and use these information in future decisions. 

When dolores retrieves these negative memories during reflections, they could influence her interpretations of past experiences, causing her to generate more negative thoughts. This new thought is then stored as another memory, which can also have a high retrieval score because of the higher negative bias. Over time, this could create a feedback loop where negative memories lead to more negative reflections, which are then stored and retrieved again. This could eventually lead to an higher decline in overall valence.

From the log, Dolores has her negative memories with bernard at 10:22 (node_117, valence −5), where she reflected on a negative interaction with Bernard. As mentioned earlier, the description is more detailed because of the active asymetric encoding.

Later, around 10:43, this negative memory was referenced in other thoughts (node_159 and node_188). However, both had a valence of 0. Instead of generating a negative emotion, she states in the memories that she can control her emotions and stay calm.

This all shows that negative thougs do not always lead to new negative thoughs. Although we could observed part of the mechanism, it did not lead to the expected negative feedback spiral. Maybe running the simulation for longer could lead to these kind of results.

---

## Exercise 4: Daily Plan Quality

### 4.1 Original plan problems

**Paste an example of a problematic daily plan and annotate what is wrong with it:**

### 4.2 Your planning rules

List the rules you wrote:

### 4.3 Improved plan

**Paste an example of a daily plan generated with your rules:**

### 4.4 Downstream effects

**Do agents with better plans behave differently? More social interactions? Different valence patterns?**

Your answer:

---

## General Reflection

**What was the most surprising finding across all exercises?**

Your answer:

**If you were designing an agent simulation for a real application, what would you do differently based on what you learned?**

Your answer:
