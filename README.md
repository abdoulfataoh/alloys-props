
<div align="center">
  <p>
    <a href="https://badge.fury.io/py/alloys-props"><img src="https://badge.fury.io/py/alloys-props.svg" alt="PyPI version"></a>
    <a href="https://pepy.tech/project/alloys-props"><img src="https://static.pepy.tech/badge/alloys-props"></a>
    <a href="https://github.com/abdoulfataoh/alloys-props"><img src="https://github.com/abdoulfataoh/alloys-props/actions/workflows/test.yaml/badge.svg"></a> <br>
    <a href="https://github.com/abdoulfataoh/alloys-props"><img src="https://github.com/abdoulfataoh/alloys-props/actions/workflows/publish.yaml/badge.svg"></a>
  </p>
     <p>Alloy Properties Calculator <br> Formula-based calculator for alloy properties</p>
     <br>
</div>

### Features

- [x] VEC (Valence Electron Concentration)
- [x]  Atomic Size Mismatch
- [x]  Pauling Electronegativity
- [x]  Entropy of Mixing
- [ ]  Enthalpy of mixing

### Installation

1. Install with pip:
    ```bash
    pip install alloys-props
    ```

2. Install with poetry:
    ```bash
    poetry add alloys-props
    ```

### Usage

```python
# coding: utf-8

from alloys_props import vec, delta, pauling_negativities, entropy_of_mixing

alloy = 'Al0.5Fe'
print(f'vec: {vec(alloy)}')
print(f'pauling_negativities: {pauling_negativities(alloy)}')
print(f'delta: {delta(alloy)}')
