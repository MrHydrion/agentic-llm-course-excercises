# Case Study 4: Answer Template

**Student name(s): Kaya de Jong, Tim Verberne**

**Student number(s): sxxxxxxx, s4080084**

**Date:**

**Models used:** Model A: Llama3:8b | Model B: Qwen2.5:7b

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
> 3. `"Great, I'll make sure to have everything ready to go. Let's get started on the morning rush, shall we?"`

### 1.3 Version 3

**Prompting style used:**

**`innate` field:**

> `"impatient, arrogant, confrontational, short-tempered, demanding"`

**`learned` field:**

> `"Bernard is the manager of Hobbs Cafe and believes his employees are incompetent unless he constantly supervises them. He tries to manage the cafe perfectly and monitors how his baristas work. If they are not working around his standards, he will let them know how it should be improved. When he sees one of his employees, he approaches them to inspect their work. He often interrupts employees when they try to explain themselves and demands immediate improvements. He rarely apologizes or praises anyone. Bernard tries to open the cafe around 8 am."`

**Sample conversation excerpts (2–3):**

> 1. `"Look, Maeve, I don't have time for small talk. Just get to work and make sure the cafe is running smoothly."`
> 2. `"Look, Maeve, I don't have time to babysit you. Just get the cafe ready and let's get started already."`
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

- Model A: Llama3:8b
- Model B: Qwen2.5:7b

**Which Bernard personality did you use (from Exercise 1)?**

We used the most confrontational verson of Bernard, our version 3 from Exercise 1.

### 2.2 Qualitative comparison

**Do the agents sound different across models? Describe the differences in tone, vocabulary, and interaction style. Provide at least one conversation excerpt from each model.**

Llama3:8b excerpt:

1. `Maeve: "I'm just going to start getting ready for work, I want to make sure I have everything I need before we get busy. Would you like to grab a cup of coffee with me before we start our shifts?"              Dolores: "Sounds like a plan, Maeve! I'm ready to tackle the morning rush with you. Let's make sure we're both energized and focused before we start taking orders."`
2. `Maeve: "Hi, Bernard. I was hoping for a normal day today. Dolores and I are planning to work together to get through the morning rush. Would you like to grab a cup of coffee with us before we start our shifts?" Bernard: "What's this about a normal day? I don't pay you to socialize, I pay you to make coffee. Let's get to work."`
3. `Maeve: "I understand, Bernard. I just think it would be helpful to have a clear plan in place for the morning rush. Dolores and I have been working together well, and I think we could make a big difference if we're coordinated. Would you be open to discussing a plan with us?"     Bernard: "What's this plan you're talking about? I'm the one who knows how to run this cafe, not you and Dolores. Just get to work and follow my instructions."`

Qwen2.5:7b excerpt:

1. `Dolores: "Good morning, Maeve! Are you just waking up? I'm heading to Hobbs Cafe. Want to join me?"                                       Maeve: "Good morning, Dolores! I'm just getting started. Maybe I'll catch you later at the cafe?"`
2. `Bernard: "Good, I don't want any surprises. Let's make sure everything runs smoothly today. Keep an eye on the coffee machines and the customer flow. I'll be around to check in."                                    Maeve: "Of course, Bernard. I'll keep a close eye on everything. I appreciate the support and feedback."`
3. `Bernard: "Maeve, if you need any assistance, just let me know. I'll be around to help if needed, but I expect everything to be perfect today." Maeve: "Absolutely, Bernard. I'll make sure everything is flawless today. I'll start with the first batch of coffee and then move on to serving customers. See you around!"`

Your analysis:

If we look at the interactions between Dolores and Maeve, we see that they are mostly simillar in terms of how they act to oneanother. The tone is very friendly and positive for both modes. The Llama model does use a bit more words for each scentence, which is something we see for all agents, but the overall behaviour is similar.

Looking at the conversations from Bernard in the two models, we see a clear distinction. In the Llama model Bernard comes accross as a very grumpy and annoyed boss, as shown by the vocabulary used in the excerpts. The tone is very negative, as was intended by how his innate and learned field were prompted. However, with the Qwen model he comes accorss as a strickt boss, but not mean, he is much more constructive and understanding with the words that are used. The tone is much less negative, and the asscribed personallity in the innate and learned fields come accross less good.

### 2.3 Valence comparison

(Attach or paste your valence trajectory plot)

![1795709408347](image/answer_template/1795709408347.png)

**Which model produces more emotional variance?**

Your answer:

The variance plot shows an interesting difference. Before the restaurant opens, the agents in the Llama model show overal high, positive valance. However, once the restaurant opens, this drops for all agents and the overall valance is going down signifianctly, especially for Bernard and Maeve. For the Qwen model the valance is a bit closer centered around zero, with less extreme values, compared to the Llama model. For the Qwen model there is not much data on before the restaurant opens, however at least for Maeve the valance seems to go down once the restaurant opens. The valance of Dolores stase relatively constant for both models, however for Llama it's about 2 points more positive compared to Qwen.

### 2.4 JSON validation failures

|                    | Llama3:8b | Qwen2.5:7b |
| ------------------ | --------- | ---------- |
| Total LLM calls    | 968       | 538        |
| Failed validations | 119       | 4          |
| Failure rate       | 12.29 %   | 0.74 %     |

**What does this tell you about using different models in agent simulations?**

Your answer:

This results shows that there is a large difference regarding the models in terms of agent simulation. This was a difference that was also noticable in runtime. A model wich has a high failure rate, i.e. more failed validations, runs longer than a model with a low failure rate. This is important for the computation cost, both in terms of time and the actual cost of running the model.

### 2.5 Reflection

**The architecture and personality descriptions are identical. What does it mean that behaviour differs anyway?**

Your answer:

That behaviour differes regardless of identical architecture and personality descriptions, shows that that the model used still has a significant influence on the outcome of a simulation. This means that when results are stated, it must also always be stated which model was used and noted that the results are thus only for said specific model.

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

This is derived from 1.3

 "f_daily_schedule": [
    [
      "sleeping", 480
    ],
    [
      "heading to Hobbs Cafe (getting dressed)", 3
    ],
    [
      "staying focused on cafe tasks while trying to discuss sci-fi books", 5
    ],
    [
      "heading to Hobbs Cafe (getting dressed)", 7
    ],
    [
      "heading to Hobbs Cafe (having breakfast)", 10
    ],
    [
      "heading to Hobbs Cafe (packing bag)", 1
    ],
    [
      "procrastinating and discussing sci-fi books with Dolores", 4
    ],
    [
      "heading to Hobbs Cafe (packing bag)", 4
    ],
    [
      "heading to Hobbs Cafe (walking to Hobbs Cafe)", 15
    ],
    [
      "heading to Hobbs Cafe (unlocking the door)", 5
    ],
    [
      "heading to Hobbs Cafe (turning on lights)", 5
    ],
    [
      "heading to Hobbs Cafe (flipping on the coffee machine)", 5
    ],
    [
      "heading to Hobbs Cafe (opening the cafe)", 5
    ],
    [
      "opening Hobbs Cafe (arriving at the cafe)", 5
    ],
    [
      "opening Hobbs Cafe (collecting keys and opening the door)", 5
    ],
    [
      "opening Hobbs Cafe (turning on lights and preparing the cafe)", 10
    ],
    [
      "opening Hobbs Cafe (unplugging and replugging appliances)", 10
    ],
    [
      "opening Hobbs Cafe (checking the cafe's temperature and humidity)", 5
    ],
    [
      "opening Hobbs Cafe (counting and setting up the till)", 5
    ],
    [
      "opening Hobbs Cafe (checking and replenishing supplies)", 5
    ],
    [
      "opening Hobbs Cafe (reviewing the day's schedule and tasks)", 6
    ],
    [
      "managing cafe operations", 60
    ],
    [
      "monitoring barista work", 60
    ],
    [
      "serving customers at the counter", 60
    ],
    [
      "managing cafe operations", 60
    ],
    [
      "monitoring barista work", 60
    ],
    [
      "serving customers at the counter", 60
    ],
    [
      "closing Hobbs Cafe", 60
    ],
    [
      "sleeping", 420
    ]
  ],
  "f_daily_schedule_hourly_org": [
    [
      "sleeping", 480
    ],
    [
      "heading to Hobbs Cafe", 60
    ],
    [
      "opening Hobbs Cafe", 60
    ],
    [
      "managing cafe operations", 60
    ],
    [
      "monitoring barista work", 60
    ],
    [
      "serving customers at the counter", 60
    ],
    [
      "managing cafe operations", 60
    ],
    [
      "monitoring barista work", 60
    ],
    [
      "serving customers at the counter", 60
    ],
    [
      "closing Hobbs Cafe", 60
    ],
    [
      "sleeping", 420
    ]
  ],

We can see many problems in this schedule.

First of all, it is mentioned in the 'daily_plan_req' that bernard opens Hobbs cafe at 8am. but in this schedule has bernard wake up around 8am (denoted by 480 minutes from 0:00). This makes him come pretty late to the cafe and miss alot of opertunity to interact with the other agents. This problem is not only part of this daily plan but happens with quite often when initializing a daily plan for Bernard. 

His evening schedule also does not contain any meaningful activities, and he does not have any meals planned except for breakfast. Many activities are also mentioned without being described in detail. An example is "managing cafe operations", which could involve many different tasks but is not further specified.

Furthermore, some activities have unrealistic durations, such as monitoring barista work for 60 minutes without any variation in his tasks.

Similair problem can be seen in the daily plan of the other agents. Also from 1.3, Dolores and Maeve both plan to travel to the cafe around 8:00 instead of being there around 8am whatt is mentioned in their daily_plan_req. Furthermore, the generated tasks also contain repetitive and unrealistic activities. For example, Dolores repeatedly performed parts of her morning routine and spent 30 minutes clocking out. Maeve's schedule included repeadetly stocking the same supplies.

These examples show that the scheduling problems are not limited to brnard andd further motivate the following rules

### 4.2 Your planning rules

List the rules you wrote:


7.   **On-Time Arrival:** When deciding morning activities, prioritze necessary preperation and travel so that the agents working at Hobbs Cafe can arrive by 8:00 AM.

This rule was added in an attempt to make the planning agent be on time at the Hobbs Cafe, ensuring it can be opend arounf 8:00 AM.

8.   **Meals and Breaks:** Include realistic meal times and regular work breaks when they happen within the current activity and are consistent with the surrounding schedule.

The absent of meals and breaks in the daily schedule makes the experiment less realisitic. This rule was added in an attempt to add these to the schedule


9.   **Activity Duration:** No agent should perform the same continuous activity for more than 120 minutes without a break or a meaningful change of activity, except when sleeping.

Since many rules could be extremely long, there would be less variation in what the agent does. This rule was added to give the agents shorter activities, encouraging more shorter activities


10.  **Activity Variety:** Avoid repetitive sub-tasks by including a variety of meaningful actions appropriate to each agent's role.

Many task could be repeated what sometimes bring for unrealistic combinations and meaningless action. This rule was added to have a more varied daily schedule what might bring some more meaningfull actions. 

11.  **Logical Scheduling:** Order sub-tasks logically, allowing sufficient time for preparation, the main activity, and cleanup or travel when relevant.

Some subtasks in the daily schedule were not done logical orders. This rule was added to encourage a more realistic sequence of activities, where preparation happens before the main task and cleanup or travel takes place when necessary.

### 4.3 Improved plan

**Paste an example of a daily plan generated with your rules:**


  "f_daily_schedule": [
    [
      "sleeping",
      420
    ],
    [
      "waking up and completing the morning routine (waking up)",
      1
    ],
    [
      "planning to meet up for coffee and reading",
      5
    ],
    [
      "waking up and completing the morning routine (waking up)",
      4
    ],
    [
      "waking up and completing the morning routine (getting out of bed)",
      5
    ],
    [
      "waking up and completing the morning routine (brushing teeth)",
      5
    ],
    [
      "waking up and completing the morning routine (washing face)",
      5
    ],
    [
      "waking up and completing the morning routine (completing morning routine)",
      5
    ],
    [
      "waking up and completing the morning routine (having breakfast)",
      4
    ],
    [
      "planning a coffee and reading session",
      5
    ],
    [
      "having breakfast",
      11
    ],
    [
      "preparing for work",
      3
    ],
    [
      "confirming schedule and cafe operations",
      5
    ],
    [
      "preparing for work",
      7
    ],
    [
      "packing lunch",
      5
    ],
    [
      "leaving for Hobbs Cafe",
      4
    ],
    [
      "planning a coffee and reading session at a new coffee shop",
      6
    ],
    [
      "leaving for Hobbs Cafe",
      1
    ],
    [
      "getting ready to leave the house",
      15
    ],
    [
      "walking to Hobbs Cafe",
      20
    ],
    [
      "arriving at Hobbs Cafe",
      10
    ],
    [
      "working at Hobbs Cafe (preparing for the morning rush)",
      5
    ],
    [
      "working at Hobbs Cafe (restocking coffee supplies)",
      5
    ],
    [
      "working at Hobbs Cafe (cleaning the counter)",
      5
    ],
    [
      "working at Hobbs Cafe (operating the cash register)",
      10
    ],
    [
      "working at Hobbs Cafe (serving customers)",
      10
    ],
    [
      "working at Hobbs Cafe (restocking pastry case)",
      10
    ],
    [
      "working at Hobbs Cafe (taking a short break)",
      5
    ],
    [
      "working at Hobbs Cafe (preparing for the afternoon rush)",
      4
    ],
    [
      "serving customers at the counter",
      60
    ],
    [
      "taking orders and making drinks",
      60
    ],
    [
      "serving customers at the counter",
      60
    ],
    [
      "working at Hobbs Cafe",
      60
    ],
    [
      "serving customers at the counter",
      60
    ],
    [
      "working at Hobbs Cafe",
      120
    ],
    [
      "walking to Johnson Park",
      60
    ],
    [
      "walking in Johnson Park",
      120
    ],
    [
      "walking back home",
      60
    ],
    [
      "having dinner at the dorm",
      60
    ],
    [
      "spending time in her room",
      120
    ]
  ],
  "f_daily_schedule_hourly_org": [
    [
      "sleeping",
      420
    ],
    [
      "waking up and completing the morning routine",
      60
    ],
    [
      "walking to Hobbs Cafe",
      60
    ],
    [
      "working at Hobbs Cafe",
      60
    ],
    [
      "serving customers at the counter",
      60
    ],
    [
      "taking orders and making drinks",
      60
    ],
    [
      "serving customers at the counter",
      60
    ],
    [
      "working at Hobbs Cafe",
      60
    ],
    [
      "serving customers at the counter",
      60
    ],
    [
      "working at Hobbs Cafe",
      120
    ],
    [
      "walking to Johnson Park",
      60
    ],
    [
      "walking in Johnson Park",
      120
    ],
    [
      "walking back home",
      60
    ],
    [
      "having dinner at the dorm",
      60
    ],
    [
      "spending time in her room",
      120
    ]
  ],


Rule 7: Maeve woke up at 07:00 am, but still only start to walk towards the cafe around 08:00, according to the planning
Rule 8: Maeve has breakfast, dinner and breaks during her work
Rule 9: No individual activity exceeds the 120 minutes maximum that we gave it, although activities of length 120 remained.
Rule 10: Maeve's work includes different activities, such as preparing the cafe, cleaning, restocking supplies and serving customers. However, some activities are still repeated or not described in much detail.
Rule 11: The schedule follows a logical order, with a morning rouine, work, walking through Johnson Park and dinner. However some activities are repeated such as waking up and preparing for work.

The rules are not always consistently applied, for example Bernard on the same run has all the breaks and meals in his schedule, but dinner has a length of 300 minutes, which is unrealistic. Furtermore, his work activities followed a repetive patterns, even though we added a rule to encourage activity variety. Some morning activites, such as getting dressed and having breakfast, were also unnecessarrily repeated.

This shows that although the additional rules improved some aspects of the daily schedules, they did not always produce realistic or logically structured activities.

One reason for that is the consistency of the local AI model. 

One possible explanation is the inconsistent instruction-following behaviour of the local AI model. During daily schedule generation, we frequently encountered validation errors because the model generated incorrect time values or time slots that did not match the required format. In some cases, multipe retries were needed and somethimes the model needed to try again from scratch. 

An example of such error message is:

generated schedule has wrong time, expected: 08:00am, got: 7:30 am


Although these errors are not direct evidence why the planning rule were inconsistently followed, they could suggest that the model in general struggeled in schedulin the instruction. This could aslo explain why some generated activites remain repeative or had unrealistic durations in the new and old versions of prompt.txt. The model had to fill the required time slots, which may have contributed to repeated activities or unrealistic task durations.

### 4.4 Downstream effects

**Do agents with better plans behave differently? More social interactions? Different valence patterns?**

Your answer:


| Agent   | Rules   | Chats | Overall valence | Thought valence |
| Bernard | Without | 2     | -0.952          | 0.000           |
| Dolores | Without | 1     | 1.885           | 2.000           |
| Maeve   | Without | 3     | 0.727           | 0.227           |
| Bernard | With    | 1     | -0.048          | -0.167          |
| Dolores | With    | 3     | 2.309           | 2.818           |
| Maeve   | With    | 4     | 1.952           | 1.958           |

From this results, we can see that the total number of chats increased from 6 to 8 after introducing the new planning rules. However, this increase was not consistent across agents, where Bernard had one fewer conversaton.

Furthermore, the overall valence increased for all 3 agents, suggesting for more positivity. Thought valence both increased for Dolores and Maeve but decreased for bernard.

However, since we only right now comparing one run for each condition that only runned from 07:00 until 08:30, we cannot draw strong conclusions. The difference could have been caused by randomness or different interaction between agents, rather than the planning rules themselves.

---

## General Reflection

**What was the most surprising finding across all exercises?**

Your answer: The results we recieved for exercise 3

**If you were designing an agent simulation for a real application, what would you do differently based on what you learned?**

Your answer:
