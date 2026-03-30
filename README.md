# 🌀 Recursive Visualizations & Fractals
### Data Structures & Algorithms | Python & Turtle Graphics

This repository contains a collection of recursive algorithms implemented to visualize complex geometric fractals and seasonal simulations. Each project explores the power of **recursion**, **mathematical constants**, and **procedural generation**.

---

## 📂 Project Overview

### 1. 📐 Sierpiński Fractals
Exploring the limits of recursive subdivision using triangles and circles.

| Project | Logic | Visualization |
| :--- | :--- | :--- |
| **Sierpiński Triangle** | Uses recursive midpoints to subdivide a master triangle into smaller colored sub-triangles. | `Q1a_Sierpinski_Triangle.py` |
| **Sierpiński Circle** | A unique take on the fractal, calculating tangent points and orbital rotations for overlapping circles. | `Q1b_Sierpinski_Circle.py` |

---

### 2. 🌲 Pythagoras Tree: Seasonal Simulations
A sophisticated implementation of the Pythagoras Tree fractal, integrated with environmental animations to simulate three distinct seasonal themes.

#### 🌌 Midnight (Balanced)
* **Concept:** A symmetrical tree structure representing stability.
* **Features:** Twinkling stars and moving fireflies generated via random coordinate mapping.
* **File:** `Q2_Pythagoras_Tree_Square_Balanced.py`

#### ⛈️ Rainy Night (Left Lean)
* **Concept:** An asymmetrical lean simulating wind and environmental pressure.
* **Features:** Real-time rain animation and randomized lightning strike triggers using `screen.ontimer`.
* **File:** `Q2_Pytheagoras_Tree_Left_Lean.py`

#### ❄️ Winter Frost (Right Lean)
* **Concept:** A frosty, icy aesthetic using cool-tone color palettes.
* **Features:** Continuous particle simulation for falling snowflakes and a glowing lunar background.
* **File:** `Q2_Pytheagoras_Tree_Right_Lean.py`

---

## 🛠️ Technical Implementation

### 🧮 Mathematical Foundations
* **Trigonometry:** Utilized `math.sin()` and `math.cos()` to calculate branch coordinates and lengths for asymmetrical leaning.
* **Pythagorean Theorem:** Used to dynamically scale child nodes relative to parent squares.
* **Recursion Depth:** Optimized for `degree 5-10` to balance visual complexity with Turtle rendering speeds.

### 🎨 Visual Engineering
* **Turtle Module:** Leveraged `tracer(0)` and `update()` for smooth, non-choppy animations.
* **Procedural Generation:** Used `random` libraries for "twinkle" effects and firefly paths, ensuring every execution is unique.

---

## 🚀 How to Run
1. Ensure you have Python installed.
2. Clone the repository.
3. Run any of the seasonal or fractal files:
   ```bash
   python Q2_Pytheagoras_Tree_Left_Lean.py
