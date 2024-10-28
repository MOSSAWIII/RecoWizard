<div align="center">

# 🎯 RecoWizard
### Your Magical Python Framework for Recommendation Systems

[![PyPI version](https://badge.fury.io/py/recowizard.svg)](https://badge.fury.io/py/recowizard)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![GitHub license](https://img.shields.io/github/license/MOSSAWIII/RecoWizard.svg)](https://github.com/MOSSAWIII/RecoWizard/blob/master/LICENSE)
[![Created by MOSSAWIII](https://img.shields.io/badge/created%20by-MOSSAWIII-blue)](https://github.com/MOSSAWIII)
[![Follow on GitHub](https://img.shields.io/github/followers/MOSSAWIII?label=Follow&style=social)](https://github.com/MOSSAWIII)

<p align="center">
  <strong>🪄 Cast Perfect Recommendations with the Power of AI ✨</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-spellbook">Spellbook</a> •
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-grimoire">Grimoire</a> •
  <a href="#-wizards-guild">Guild</a>
</p>

</div>

## ⚡ Why RecoWizard?

RecoWizard transforms the complex art of recommendations into simple, powerful spells. Whether you're crafting personalized product suggestions, conjuring content recommendations, or divining user preferences, RecoWizard provides the magical tools you need.

## 🌟 Features

### 🎯 Enchanted Algorithms

#### Magic Items Portal
- 🔮 BPRMF Crystal Ball
- 🪄 ItemKNN Wand
- 📚 Content Scroll
- 🎭 UserKNN Mirror
- 🌌 Group Portal
- ⚡ Lightning-fast baselines

#### Rating Divination
- 🌠 Matrix Starlight
- 🌙 SVD Moonstone
- 💫 Non-negative Stardust
- 🎪 Advanced Circus (gSVD++, MSMF)
- 🎨 CoRec Canvas

### 📊 Scrying Tools
- 🔍 Cross-realm validation
- 📈 Precision crystals
- 📉 Recall mirrors
- 🎯 NDCG compass
- ⚖️ Statistical runes

## 💫 Installation

```bash
# Summon with pip
pip install recowizard

# Latest magical version
pip install -U git+git://github.com/MOSSAWIII/RecoWizard.git
```

### Magical Requirements
```bash
pandas      # Data scrolls
scikit-learn # Learning runes
scipy       # Scientific crystals
numpy       # Numerical stones
```

## 🪄 Quickstart

### Prepare Your Spells
```python
from recowizard.utils.portal import Portal

# Open a cross-validation portal
Portal(scroll="dataset.csv", 
       realm="folds/", 
       portals=10).create_crossroads()
```

### Cast Recommendations
```python
from recowizard.spells.items import ItemWand

# Wave the recommendation wand
wand = ItemWand(training_scroll="train.csv", 
                testing_scroll="test.csv")
wand.cast()
```

### Read the Prophecies
```python
from recowizard.divination import ItemDivination

# Interpret the signs
oracle = ItemDivination()
prophecy = oracle.divine_scrolls("predictions.csv", "test.csv")
```

## 📚 Grimoire (Documentation)

Explore our ancient tomes in the [Grimoire](https://github.com/MOSSAWIII/RecoWizard/wiki).

### Scroll Format
- Sacred CSV scrolls with 3 runes
- Example: `wizard_1,item_1,magic_level`

### Common Enchantments
- 🤝 Collaborative Magic
- 📖 Content Divination
- 🎭 Hybrid Spells
- ⭐ Rating Prophecies
- 📊 Item Rankings

## 🧙‍♂️ About the Archmage

<div align="center">

**Mohamed Amine EL MOUSSAOUI**  
Data Archmage & Recommendation Wizard

[![GitHub](https://img.shields.io/badge/GitHub-MOSSAWIII-181717?style=for-the-badge&logo=github)](https://github.com/MOSSAWIII)
[![Email](https://img.shields.io/badge/Magic%20Mail-maelmoussaoui1%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:maelmoussaoui1@gmail.com)

</div>

## 🧙‍♀️ Wizards' Guild (Contributing)

Join our magical community:

1. Clone the spellbook (`git clone`)
2. Create your magic branch (`git checkout -b spell/AmazingFeature`)
3. Commit your enchantments (`git commit -m 'Add AmazingFeature'`)
4. Cast to the realm (`git push origin spell/AmazingFeature`)
5. Open a Magical Portal (Pull Request)

## 📜 Ancient Scrolls (Citation)

To reference our magical arts in your scrolls:

```bibtex
@software{RecoWizard2024,
    author = {EL MOUSSAOUI, Mohamed Amine},
    title = {RecoWizard: A Magical Python Framework for Recommendation Systems},
    year = {2024},
    publisher = {GitHub},
    url = {https://github.com/MOSSAWIII/RecoWizard}
}
```

## ⚖️ Magical License

This spellbook is protected under the MIT License - see the [LICENSE](LICENSE) scroll for the full incantation.

---

<div align="center">

Crafted with 🪄 by Mohamed Amine EL MOUSSAOUI ([@MOSSAWIII](https://github.com/MOSSAWIII))  
Last enchantment: April 15, 2024

</div>