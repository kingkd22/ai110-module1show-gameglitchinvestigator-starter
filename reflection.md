# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- When opening the game it was a clean and simple ui with no noticible ui bugs
- When playing the game the hints continuously say either go lower or go higher even though the right score is in the oposite direction
- The new game button does not work properly as well
- When you change the difficulty the UI still reads "Guess a number between 1 and 100" even though the range changes
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

- I used the VSCode Copilot
- I used the AI to explain the logic of the code to be able to understand where the logic breaks
- I rejected some of the refactoring code suggested by AI because it changed the business logic from app.py whihc worked perfectly
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I decided the bug was really fixed after running tests and manually testing the game 
- I tested the check guess via py tests
- AI helped design the tests to have a variety of test cases


## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

- The secret number kept changing because of how Streamlit handles reruns. Every time the user interacted with the app Streamlit would rerun the entire script
- Imagine a recipe that you have to follow completely from start to finish every time someone asks you a question about cooking. Thats how streamlit works
- The fix was the if "secret" not in st.session_state: cgeck. This condistional statement only genereates a new random number the very first time the app runs
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- One strategy I will use moving forward is allowing AI to explain code logic for me
- One thing i would do differently is just letting AI make changes without reading
- This project helped me be more aware of the code AI generates and how it fits in with project.