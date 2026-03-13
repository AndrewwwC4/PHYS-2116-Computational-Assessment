# GALAH DR3 Spectroscopic Data Analysis

A Python Jupyter notebook for analysing GALAH DR3 spectroscopic measurement data.

## Project Description

This project analyses GALAH (Gaia-ESO Spectroscopic Survey) DR3 data, utilising astropy to read FITS format data files and pandas for data processing and analysis.

## File structure

```
.
├── analysis.ipynb              # Primary Analysis Notebook
├── test_galah.py               # Test script
├── .gitignore                  # Git file exclusion configuration
├── .venv-1/                    # Python Virtual Environment
└── README.md                   # Project Description
```

## Required packages

- `astropy` - Reading FITS files
- `pandas` - Data processing
- `matplotlib` - Data Visualisation
- `numpy` - Data computation

## Start

### 1. Clone repository
```bash
git clone https://github.com/AndrewwwC4/PHYS-2116-Computational-Assessment.git
cd PHYS-2116-Computational-Assessment
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install astropy pandas matplotlib numpy
```

### 4. Operational Analysis
```bash
jupyter notebook analysis.ipynb
```

## Data file

Raw FITS data files (excluded from the repository due to file size exceeding 100MB)：
- `GALAH_DR3_main_allstar_v2.fits` - Stellar Catalogues
- `GALAH_DR3_VAC_GaiaEDR3_v2.fits` - Gaia EDR3 Cross-matched data

Available from the following sources：
- [GALAH Survey Official Website](https://www.galah-survey.org/)
- [ESO Data Archives](https://www.eso.org/rm/public/archives/dh)

This project is intended solely for educational and research purposes.

## Contributor

AndrewwwC4 [Hei Kan CHAN]

---

**Course:** PHYS 2116 Computational Assessment (UNSW Sydney)
