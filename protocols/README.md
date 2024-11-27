# OT-2 Dilution Protocol Scripts

## Overview

This repository contains Python scripts developed to optimize liquid handling for the **Opentrons OT-2 pipetting robot**. These scripts are designed to enhance the accuracy and precision of dilution protocols, achieving a liquid handling accuracy of **95%**. Accurate liquid handling is critical in wet lab workflows, particularly in **SwabSeq**, a high-throughput **COVID-19 diagnostic tool**. SwabSeq pools RNA samples into a single tube, enabling multiple samples to be analyzed simultaneously.

---

## Features

1. **Improved Liquid Handling Accuracy**:
   - Raised pipetting precision to 95%, reducing errors in diagnostic workflows.
2. **Pooling Protocol Enhancements**:
   - Optimized for SwabSeq RNA sample pooling.
   - Prevents air bubbles and minimizes liquid retention on tube edges.

---

## Key Scripts

### 1. `pooling_touch_tip.py`
This script ensures thorough dispensing of liquid by:
- **Touching all four sides** of the pipette tip against the tube after aspirating liquid.
- Ensuring no residual liquid remains in the pipette tip.

### 2. `pooling_final_p20_only.py`
This script calculates the optimal pipetting height to:
- **Prevent air bubbles** and liquid from sticking to tube walls.
- Dispense liquid just above the surface of the existing liquid in the tube.
- Height calculations are based on:
  - Tube dimensions.
  - Expected liquid volume already in the tube.

**Recommendation**: The `pooling_final_p20_only.py` script provides the best performance for SwabSeq workflows.

---

## Tech Stack

- **Python Scripting**: Main programming language.
- **SciPy**: For mathematical calculations and optimizations.
- **NumPy**: For handling numerical computations and array operations.
- **Opentrons API**: For controlling the OT-2 robot.

---

## Importance of Accurate Liquid Handling

In SwabSeq workflows:
- RNA samples from multiple individuals are pooled into a single tube.
- Accurate pooling ensures:
  - Sample integrity.
  - Reliable downstream diagnostic results.

---

## Usage Instructions

### Setting Up the Environment
1. Create a virtual environment using `conda` or `pyenv`.
2. Install the required dependencies:
   ```bash
   pip install opentrons numpy scipy
3. opentrons_simulate.exe my_protocol.py
