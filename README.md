## Alloy Properties Calculator

Formula-based calculator for alloy properties

### Features

- **VEC (Valence Electron Concentration)**
- **Atomic Size Mismatch (Δ)**
- **Pauling Electronegativity**
- **Entropy of Mixing**

### Installation

2. Install the dependencies:
    ```bash
    pip install alloys-props
    ```

### Usage

```python
# coding: utf-8

from alloys_props import vec, delta, pauling_negativities, entropy_of_mixing

alloy = 'Al0.5Fe'
print(f'vec: {vec(alloy)}')
print(f'pauling_negativities: {pauling_negativities(alloy)}')
print(f'delta: {delta(alloy)}')
