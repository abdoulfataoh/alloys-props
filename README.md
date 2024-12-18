
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

- [x] Valence Electron Concentration (VEC)

    $\text{VEC} = \sum_{i} c_i \cdot \text{VEC}_i$

- [x] Atomic Size Mismatch (delta)

  $\delta = \sqrt{\sum_{i} c_i \left(1 - \frac{r_i}{\overline{r}}\right)^2}$


- [x] Pauling Electronegativity

  $\chi = \sqrt{\sum_{i=1}^{n} c_i \left( \chi_i - \overline{\chi} \right)^2}$

- [x] Entropy of Mixing

    $\Delta S_{\text{mix}} = -R \sum_{i} c_i \ln c_i$


- [ ] Enthalpy of Mixing

    $\Delta H_{\text{mix}} = \sum_{i=1}^n \sum_{j=1, j \neq i}^n 4 c_i c_j \Delta H_{\text{mix}}^{ij}$



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
