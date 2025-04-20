---

# Welcome to My ePortfolio


[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/james-durk/CS-499)

---

## Table of Contents

- [Professional Self-Assessment](#professional-self-assessment)
- [Code Review](#code-review)
- [Artifact 1: Software Design & Engineering](#artifact-1-software-design--engineering)
- [Artifact 2: Algorithms & Data Structures](#artifact-2-algorithms--data-structures)
- [Artifact 3: Databases](#artifact-3-databases)

---

## Professional Self-Assessment
Over the course of my Computer Science program at Southern New Hampshire University, I’ve developed a strong foundation in core programming principles, algorithms, software engineering, and database systems. This ePortfolio serves not only as a summation of the skills I’ve gained, but also as a demonstration of how I apply those skills to solve real problems with maintainable, scalable, and thoughtful solutions. Completing this capstone and assembling this portfolio has helped me reflect on my growth, solidify my professional values, and prepare to contribute meaningfully to a technical team in the workforce.

Throughout the program, I’ve had the opportunity to work both independently and collaboratively, gaining experience that mirrors professional software development environments. I’ve collaborated on projects that required source control using Git, implemented features based on stakeholder needs, and practiced iterative development to ensure quality results. Working with peers in group assignments taught me how to contribute within diverse team structures, navigate differing communication styles, and meet project deadlines through shared ownership. These collaborative experiences have prepared me to work effectively within agile teams and to communicate clearly across technical and non-technical roles.

One of the most valuable areas of growth during my time in the program has been in applying data structures and algorithms to real problems. Beyond textbook exercises, I’ve learned how to analyze performance trade-offs, refactor code for efficiency, and structure programs using appropriate data models. These skills have proven especially useful in personal projects and workplace scenarios, where clarity and efficiency are often critical to success.
In software engineering coursework, I developed a deeper understanding of the Software Development Lifecycle, from planning and design to implementation and testing. I’ve learned the value of modular design, clean code principles, and version control not just for academic assignments, but as a mindset for building maintainable software. My database coursework gave me hands-on experience working with both SQL and NoSQL systems. I now feel confident designing schemas, writing complex queries, and integrating persistent data storage into full-stack applications.

Security considerations were embedded throughout my coursework, and I’ve come to appreciate the importance of building systems with a proactive security mindset. From input validation to code reviews and secure data handling, I’ve gained an understanding of how to anticipate potential vulnerabilities and design with long-term safety in mind.

The three artifacts included in this portfolio were chosen not only for their individual strengths, but for how they represent my growth across different domains of computer science. By revisiting a project developed early in my degree—a Python-based text adventure game—I was able to enhance it in three meaningful ways. One enhancement focused on software design and modularity, another introduced advanced algorithms and data structures, and the third implemented persistent game-saving using SQLite. These enhancements demonstrate a cohesive narrative of progression: from writing basic scripts to designing scalable systems, implementing intelligent algorithms, and integrating real-world data solutions.

Together, these artifacts showcase my readiness to transition from academic work to professional contributions. They reflect the technical depth I’ve built, the practical tools I’ve learned to use, and the mindset I bring to software development—one that values clarity, collaboration, and continuous improvement. I’m excited to take the next step in my career and apply these skills in ways that drive value for teams, users, and organizations.

---

## Code Review

### Overview

As part of the enhancement process for this portfolio, I conducted a code review of the artifacts selected for enhancement. The purpose of this review was to evaluate existing functionality, identify potential areas for improvement, and plan enhancements aligned with the course outcomes of CS-499.

### Code Review Video

[![Watch Code Review](https://img.shields.io/badge/Watch-My_Code_Review-green?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=jpyWzHc7L3M)

### Summary of Review

- **Existing Functionality:** Describes the original purpose and behavior of the artifact before enhancement.
- **Code Analysis:** Identified improvements needed in structure, logic, maintainability, security, and efficiency.
- **Planned Enhancements:** Each enhancement aligned with one of the three categories:
  - Software Design & Engineering
  - Algorithms & Data Structures
  - Databases

---

## Artifact 1: Software Design & Engineering

### Artifact Narrative

The first artifact I selected for this ePortfolio is a Python-based text adventure game, initially developed during IT-140: Introduction to Scripting. The project features a menu-driven interface in which players navigate rooms, collect items, and pursue an end goal through exploration and interaction. This was my introduction to foundational programming concepts such as user input, conditionals, loops, and basic object-oriented design.

This artifact demonstrates the progression of my skills in software development, particularly in writing modular, maintainable code. For this enhancement, I focused on improving the program’s overall structure and usability. Key improvements included breaking repetitive logic into reusable functions, clarifying input handling, and implementing more scalable data structures to manage room data and inventory. The result is a cleaner, more robust foundation that better supports future development or expansion.

This enhancement directly aligns with the Software Design and Engineering outcome
identified in Module One. Through this work, I demonstrated my ability to apply software
engineering principles and development methods in the construction and evaluation of software
systems. At this time, I do not have any changes to my outcome coverage plans, and this
enhancement serves as a solid foundation toward fulfilling all related outcomes in the course.
The process of revisiting and improving this artifact provided an opportunity for deep learning
and reflection. One key takeaway was the importance of code readability and maintainability—
especially in projects that may be revisited or expanded over time. I also learned how thoughtful
modularization and design decisions can dramatically improve a project’s scalability and ease of
debugging. One challenge I encountered was determining how best to organize the game logic in
a way that avoided duplication without overcomplicating the flow of control. To overcome this, I
leveraged functions and dictionaries in Python to simplify the branching logic and make the code
more intuitive.

Overall, this enhancement not only strengthened the artifact itself but also deepened my
understanding of how strong software design practices contribute to long-term code quality and
collaboration readiness.

### View the Code

[![View Code](https://img.shields.io/badge/View_Code_on_GitHub-black?style=for-the-badge&logo=github)](https://github.com/james-durk/CS-499/tree/main/enhancements/IT140-softwaredesign)

---

## Artifact 2: Algorithms & Data Structures

### Narrative
Narrative – Algorithms and Data Structures Enhancement
The second artifact I enhanced is the same Python-based text adventure game, which originally served as an introduction to core scripting techniques in IT-140. At the time, the game allowed users to move between rooms and collect items, with logic managed via basic dictionary lookups and list operations. While functional, the initial version lacked strategic depth and offered little in terms of algorithmic complexity.

To address this, I enhanced the artifact by implementing a graph-based structure for the game world and introducing a Breadth-First Search (BFS) algorithm to determine and display the shortest path to any item. These changes elevate the project from a basic scripting assignment to one that demonstrates effective use of data structures and algorithmic thinking. This enhancement not only improves gameplay but also highlights my ability to apply graph traversal techniques and modular algorithm design within an existing codebase.

The enhancements I made directly align with the course outcomes I outlined in Module
One. Specifically, I aimed to meet Course Outcome 3, which involves designing and evaluating
computing solutions using algorithmic principles, and Course Outcome 4, which highlights the
use of well-founded techniques and tools in computing practices. I believe I fully met both
outcomes by transforming a static, dictionary-based system into a navigable graph and
implementing an efficient search algorithm to solve the problem of item pathfinding.

Throughout the enhancement process, I learned how to design a modular algorithm that
integrates smoothly into an object-oriented codebase. I practiced working with Python’s deque
data structure for efficient queue operations and gained a deeper appreciation for separating
concerns—by isolating pathfinding into its own module. A key challenge was balancing
gameplay simplicity with functional complexity; I had to decide how much information to
provide to the player without compromising the spirit of the game. Ultimately, I chose to include
directional guidance in the pathfinding output, which required me to track both rooms and
movement directions during traversal. Overcoming these challenges strengthened my problemsolving mindset and gave me hands-on experience applying data structures in a meaningful way.


### View the Code
[![View Code](https://img.shields.io/badge/View_Code_on_GitHub-black?style=for-the-badge&logo=github)](https://github.com/james-durk/CS-499/tree/main/enhancements/IT140-algorithms)

---

## Artifact 3: Databases

### Narrative
For the third enhancement, I once again worked with the Python-based text adventure game created during IT-140. While the original game successfully implemented basic game mechanics, it lacked the ability to preserve progress between sessions. All state information—inventory, player location, room items—was stored only in memory and lost upon exiting the program.

To solve this, I added database functionality using SQLite to support saving and loading game progress. I implemented a SaveManager class that handles persistent storage of player data, including current room, inventory, and dynamic item states in each room. This enhancement demonstrates my ability to integrate real-world database solutions into a scripting-based application. It also marks a major step in evolving the project from a one-time execution script to a more complete, user-friendly game with persistent state.

While I had initially proposed using MongoDB for this enhancement, I pivoted to SQLite
for its simplicity, portability, and built-in support in Python, which made it more appropriate for
this particular project’s scope and technical needs. The enhancement added a new SaveManager
class that handled database initialization, saving player progress, and loading saved game states.
Additionally, I extended the functionality to preserve the state of items in each room—ensuring
that items already collected do not reappear upon loading. This required thoughtful serialization
of room data and seamless integration with existing game logic.

This enhancement directly aligns with the course outcomes I planned to meet in Module
One. Specifically, I demonstrated my ability to apply well-founded techniques and tools in
computing practices (Outcome 4) by implementing database functionality using SQL, file I/O,
and serialization with JSON. I also addressed Outcome 5, which emphasizes developing a
security mindset, by ensuring data validation when loading saved files and removing old saves
before overwriting to maintain data consistency.

Throughout the process of enhancing the artifact, I gained deeper insight into how
persistent data can impact gameplay mechanics and the user experience. One challenge I
encountered was preserving room item states alongside player progress, which required
modifying both the save schema and the game logic to properly reflect changes in room states.
Another challenge was ensuring that the data types used for player inventory remained consistent
after deserialization. I initially used a Python set for efficiency, which does not serialize well into
a database without conversion, so I adjusted the save/load system to convert between data types
smoothly.

This enhancement significantly improves the polish and professionalism of the artifact
while demonstrating my ability to integrate practical database solutions into a Python-based
application. It showcases my growth from basic scripting to more robust software development
practices involving data persistence, user state management, and game design principles.


### View the Code
[![View Code](https://img.shields.io/badge/View_Code_on_GitHub-black?style=for-the-badge&logo=github)](https://github.com/james-durk/CS-499/tree/main/enhancements/IT140-databases)

