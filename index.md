---

# Welcome to My ePortfolio


[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/james-durk/CS-499)

---

## Table of Contents

- [Professional Self-Assessment](#professional-self-assessment)
- [Code Review](#code-review)
- [Artifact 1: Software Design & Engineering](#artifact-1-software-design--engineering)
- [Artifact 2: Algorithms & Data Structures](#artifact-2-algorithms--data-structures)

---

## Professional Self-Assessment

---

## Code Review

### Overview

As part of the enhancement process for this portfolio, I conducted a code review of the artifacts selected for enhancement. The purpose of this review was to evaluate existing functionality, identify potential areas for improvement, and plan enhancements aligned with the course outcomes of CS-499.

###Code Review Video

[![Watch Code Review](https://img.shields.io/badge/Watch-My_Code_Review-green?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=jpyWzHc7L3M)

### Summary of Review

- **Existing Functionality:** Describes the original purpose and behavior of each artifact before enhancement.
- **Code Analysis:** Identified improvements needed in structure, logic, maintainability, security, and efficiency.
- **Planned Enhancements:** Each enhancement aligned with one of the three categories:
  - Software Design & Engineering
  - Algorithms & Data Structures
  - Databases

---

## Artifact 1: Software Design & Engineering

### Artifact Narrative

The artifact I selected for the Software Design and Engineering category is a Pythonbased text adventure game originally developed in IT-140, Intro to Scripting. The game presents
a menu-driven narrative in which users explore different rooms, interact with the environment,
and collect items to progress toward a goal. The original version was created in 2023 and served
as an introduction to core programming principles such as user input, control flow, and basic
object-oriented design.

I selected this artifact for inclusion in my ePortfolio because it clearly demonstrates my
foundational knowledge of software development and highlights how I’ve grown in my ability to
write cleaner, more maintainable, and modular code. This project is a great representation of how
I’ve applied software design principles in a real-world context. In the enhancement process, I
focused on improving the structure of the code through modularization, adding clear
documentation, and refining how the game handles user input and state transitions. For example,
I refactored repetitive conditional logic into reusable functions and implemented more scalable
data structures to manage rooms and inventory.

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
The artifact I selected for this enhancement is a text-based adventure game originally
developed for IT-140: Introduction to Scripting early in my degree program. The project was
created using Python and involved simple game mechanics such as navigating between rooms,
collecting items, and fulfilling a win condition by collecting all necessary equipment. It was one
of the first projects where I practiced foundational programming concepts like conditionals,
loops, and data storage using Python dictionaries and lists.

I chose this artifact for inclusion in my ePortfolio because it provided a clean, scalable
foundation to demonstrate multiple enhancement categories—including software engineering,
algorithms and data structures, and databases—within a single cohesive program. For the
database enhancement specifically, I saw an opportunity to improve the game’s functionality and
user experience by implementing a persistent save and load system. Originally, the game stored
all progress in memory only; once the program closed, all player data and progress were lost. To
address this limitation, I integrated an SQLite-based solution to allow players to save their
current room, inventory, and room item states and later resume from where they left off.
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
[![View Code](https://img.shields.io/badge/View_Code_on_GitHub-black?style=for-the-badge&logo=github)](https://github.com/james-durk/CS-499/tree/main/enhancements/IT140-algorithms)
---


