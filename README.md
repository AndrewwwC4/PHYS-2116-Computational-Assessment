# GALAH DR3 Spectroscopic Data Analysis

一个用于分析 GALAH DR3 光谱测量数据的 Python Jupyter notebook。

## 📋 项目描述

这个项目分析 GALAH (Gaia-ESO Spectroscopic Survey) DR3 数据，使用 astropy 读取 FITS 格式的数据文件，并使用 pandas 进行数据处理和分析。

## 📁 文件结构

```
.
├── analysis.ipynb              # 主要分析 notebook
├── test_galah.py               # 测试脚本
├── .gitignore                  # Git 忽略文件配置
├── .venv-1/                    # Python 虚拟环境
└── README.md                   # 本文件
```

## 🔧 所需包

- `astropy` - 读取 FITS 文件
- `pandas` - 数据处理
- `matplotlib` - 数据可视化
- `numpy` - 数值计算

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/AndrewwwC4/PHYS-2116-Computational-Assessment.git
cd PHYS-2116-Computational-Assessment
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
pip install astropy pandas matplotlib numpy
```

### 4. 运行分析
```bash
jupyter notebook analysis.ipynb
```

## 📊 数据文件

原始 FITS 数据文件（由于文件大小 > 100MB，未包含在仓库中）：
- `GALAH_DR3_main_allstar_v2.fits` - 主要星表数据
- `GALAH_DR3_VAC_GaiaEDR3_v2.fits` - Gaia EDR3 交叉匹配数据

可以从以下来源获取：
- [GALAH Survey 官方网站](https://www.galah-survey.org/)
- [ESO 数据档案馆](https://www.eso.org/rm/public/archives/dh)

## 📝 许可证

此项目仅供学习和研究用途。

## ✍️ 作者

AndrewwwC4

---

**课程:** PHYS 2116 Computational Assessment (UNSW Sydney)
