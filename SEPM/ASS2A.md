# Assignment 2 Answers

## 1. What are the rules that should be followed when creating the analysis model.

To create an effective analysis model in software engineering, follow these key rules:

1. **Focus on Business Requirements:**
   - Emphasize requirements within the business domain, maintaining a high level of abstraction.

2. **Relevant Elements:**
   - Include elements that contribute to understanding software requirements, covering information, functions, and system behavior.

3. **Delay Infrastructure Details:**
   - Postpone detailed infrastructure and nonfunctional considerations to avoid design delays.

4. **Minimize Coupling:**
   - Keep interconnections between modules (coupling) to a minimum for enhanced modularity.

5. **Stakeholder Value:**
   - Ensure the analysis model provides value to all stakeholders involved in the project.

6. **Simplicity is Key:**
   - Strive for a simple model to facilitate easy understanding and clear communication of requirements.

## 2. Draw DFD up to level 2 for a restaurant management system which has food ordering, food delivering invoice creation and payment subsystem.

![q2l0](./ASS2A_Images/Q2L0.png)
![q2l1](./ASS2A_Images/Q2L1.png)
![q2l2](./ASS2A_Images/Q2L2.png)

## 3. Explain hierarchy of software testing with neat diagram.

Certainly, Dev. The hierarchy of software testing typically involves four levels:

1. **Unit Testing:**
   - Focus: Individual components or modules.
   - Purpose: Verify that each unit of the software performs as designed.
   - Tools: Test frameworks like JUnit, NUnit, or testing libraries in various programming languages.

2. **Integration Testing:**
   - Focus: Interaction between integrated components or systems.
   - Purpose: Validate that units work together as intended.
   - Types: Top-down, bottom-up, and incremental integration testing.
   - Tools: JUnit, TestNG, and specialized tools for APIs or database integration.

3. **System Testing:**
   - Focus: Entire software system as a whole.
   - Purpose: Evaluate the system's compliance with specified requirements.
   - Types: Functional and non-functional testing (performance, security, usability, etc.).
   - Tools: Selenium for web applications, JIRA for test management, and various performance testing tools.

4. **Acceptance Testing:**
   - Focus: Validate if the system meets user expectations and requirements.
   - Types: Alpha testing (internal), Beta testing (external), and User Acceptance Testing (UAT).
   - Purpose: Ensure that the software is ready for release to the end-users.
   - Tools: Often manual testing, but automated tools like Cucumber or Robot Framework can be used for behavior-driven development.

This hierarchical approach ensures that defects are identified and corrected at the earliest possible stage, reducing the cost of fixing issues as the development process progresses. Each level of testing serves a specific purpose in ensuring the quality and reliability of the software.

Certainly, Dev. Imagine a pyramid to visualize the hierarchy of software testing. The pyramid is divided into four layers, representing the four levels of testing:

1. **Base Layer: Unit Testing**
   - At the base of the pyramid, you have Unit Testing.
   - This layer is wide, indicating that unit tests are numerous and form the foundation of the testing process.
   - Each unit (or block) of code is individually tested to ensure its correctness.

2. **Second Layer: Integration Testing**
   - Above Unit Testing, you find the Integration Testing layer.
   - This layer is narrower, indicating that integration tests are fewer in number compared to unit tests.
   - Integration tests verify the interaction and collaboration between different units or modules.

3. **Third Layer: System Testing**
   - Moving higher, you reach the System Testing layer.
   - This layer is narrower than Integration Testing, symbolizing that system tests are more comprehensive but less in number compared to integration tests.
   - System tests evaluate the software as a complete and integrated system.

4. **Top Layer: Acceptance Testing**
   - At the top of the pyramid, you have the Acceptance Testing layer.
   - This layer is the narrowest, emphasizing that acceptance tests are the fewest in number but cover the entire system.
   - Acceptance tests ensure that the software meets user expectations and requirements.

The pyramid shape illustrates that as you move up the levels, the testing becomes more focused on the overall system behavior, and the number of tests generally decreases. This structure reflects the testing strategy of catching and fixing issues at the earliest and most granular level, contributing to a robust and reliable software product.

# 4. Who should perform the validation test. The software developer or the software user? Justify your answer.

The validation testing process is typically performed by individuals or teams who are independent of the software development process. This separation ensures a more objective evaluation of the software's functionality, reliability, and compliance with requirements.

Here's a breakdown of the roles:

1. **Software Developer:**
   - **Responsibility:** Developers are responsible for unit testing and may perform integration testing to ensure that individual components and modules work correctly and integrate smoothly.
   - **Bias:** Developers might have a biased perspective due to their intimate knowledge of the code. They may unintentionally overlook certain scenarios or assume certain conditions that actual users might not.

2. **Software User or Testing Team:**
   - **Responsibility:** Validation testing, including system testing, acceptance testing, and other forms of end-to-end testing, is generally the responsibility of individuals or teams external to the development process.
   - **Objective Perspective:** Users or dedicated testing teams approach the software with a fresh, unbiased perspective. They evaluate it based on user requirements, functionality, and performance, uncovering issues that might not be apparent to developers.

**Justification:**

   - **Independence:** Validation testing by users or a dedicated testing team ensures an independent assessment, reducing the likelihood of overlooking issues present in the software.
   - **Real-world Scenarios:** Users can evaluate the software in real-world scenarios, mimicking actual usage conditions and identifying issues that might not surface during development-focused testing.

In summary, while developers play a crucial role in testing their code, validation testing by users or an independent testing team is essential for a comprehensive and unbiased evaluation of the software's overall quality and suitability for its intended purpose.

## 5. Explain with example how the cyclomatic complexity is calculated.

Certainly, Dev. Cyclomatic complexity is a software metric used to measure the complexity of a program by counting the number of independent paths through the source code. It helps in identifying the number of test cases required for thorough coverage. The formula for cyclomatic complexity is:

\[ M = E - N + 2P \]

Where:
- \( M \) is the cyclomatic complexity.
- \( E \) is the number of edges in the control flow graph.
- \( N \) is the number of nodes in the control flow graph.
- \( P \) is the number of connected components (for a single program, it's usually 1).

Let's consider a simple example:

```python
def example_function(x, y):
    if x > 0:
        print("x is positive")
        if y > 0:
            print("y is positive")
        else:
            print("y is non-positive")
    else:
        print("x is non-positive")

# Control Flow Graph:
#   Nodes: 7 (Start, 2 decision points, 4 print statements)
#   Edges: 8 (7 for decision points, 1 for print statements)

# Applying the formula:
# M = E - N + 2P
# M = 8 - 7 + 2(1) = 3

# So, the cyclomatic complexity of this function is 3.
```

In this example, \( E \) is 8, \( N \) is 7, and \( P \) is 1. Plug these values into the formula, and you get a cyclomatic complexity (\( M \)) of 3. This means there are three independent paths through the code, and you might consider having at least three test cases to achieve good coverage.