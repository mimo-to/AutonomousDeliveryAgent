# Autonomous Delivery Agent – Report Draft

## 1. Introduction

This project implements an autonomous delivery agent operating on a 2D grid environment.  
The agent must find efficient delivery paths under static and dynamic obstacles using multiple AI search strategies.

Algorithms implemented:

- BFS (uninformed search)
- UCS (cost-sensitive uninformed)
- A\* (informed with Manhattan heuristic)
- Hill Climbing (local search with restarts)
- Simulated Annealing (probabilistic local search)

---

## 2. Environment Model

- Grid world with dimensions (rows × cols).
- Obstacles:
  - `#` = static obstacles.
  - Dynamic obstacles specified as `(time, x, y)` meaning blocked at that time.
- Each move = unit time step.
- Terrain cost = integer ≥ 1 (default = 1).
- Agent can move in 4 directions: up, down, left, right.

---

## 3. Algorithms

### BFS

- Explores level by level.
- Guarantees shortest path in steps, not cost.

### UCS

- Explores by cumulative path cost.
- Guarantees minimum cost solution.

### A\*

- Uses Manhattan heuristic.
- Admissible and efficient for grid navigation.

### Hill Climbing

- Greedy local search.
- Uses restarts/dynamic replanning to avoid failures.

### Simulated Annealing

- Probabilistic acceptance of worse moves.
- Can escape local minima better than hill climbing.

---

## 4. Experimental Setup

- Test maps: `small.txt`, `medium.txt`, `large.txt`, `dynamic.txt`.
- Performance metrics recorded:
  - Path length
  - Path cost
  - Nodes expanded
  - Runtime (seconds)

---

## 5. Results

### Table 1 – Static Search Performance

(From `metrics.csv`)

| Algorithm | Map    | PathLength | Cost | NodesExpanded | Runtime (s) |
| --------- | ------ | ---------- | ---- | ------------- | ----------- |
| BFS       | small  | 4          | 3    | 7             | 0.000051    |
| BFS       | medium | 11         | 10   | 20            | 0.000108    |
| BFS       | large  | 21         | 20   | 93            | 0.000323    |
| UCS       | small  | 4          | 3    | 6             | 0.000076    |
| UCS       | medium | 11         | 10   | 20            | 0.000137    |
| UCS       | large  | 21         | 20   | 93            | 0.000546    |
| A\*       | small  | 4          | 3    | 4             | 0.000063    |
| A\*       | medium | 11         | 10   | 14            | 0.000108    |
| A\*       | large  | 21         | 20   | 89            | 0.000560    |

---

### Table 2 – Local Search on Dynamic Map

(From `run_log.txt`)

| Algorithm           | Success | PathLength | Runtime (s)\* |
| ------------------- | ------- | ---------- | ------------- |
| Hill Climbing       | Yes     | 9          | ~0.0003       |
| Simulated Annealing | Yes     | 79         | ~0.0006       |

\*Runtime is approximated; exact values can be measured by wrapping `agent.move()` with `time.perf_counter()`.

---

## 6. Analysis

- **BFS**: Guarantees shortest path in steps, but ignores cost.
- **UCS**: Optimal cost, but expands more nodes than A\*.
- **A\***: Best balance — fewer nodes expanded, low runtime, cost-optimal.
- **Hill Climbing**: Reached the goal quickly in this case, but risky without replanning.
- **Simulated Annealing**: Much longer wandering path, but still succeeded — shows robustness in escaping local minima.

---

## 7. Conclusion

- For **static maps**, A\* is the most efficient.
- For **dynamic maps**, local search with replanning (Hill Climbing, Simulated Annealing) is essential.
- Future work:
  - Add runtime measurement for dynamic algorithms.
  - Visualization of pathfinding and replanning.
  - Extend movement to diagonals.

---
