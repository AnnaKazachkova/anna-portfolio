# Global Development Clustering: Can the world be split into two groups?

Unsupervised learning on UN country indicators to test the argument in Hans Rosling's *Factfulness* that "rich vs poor" is an outdated view.

**Notebook:** [`un_country_clustering.ipynb`](un_country_clustering.ipynb) (outputs included, loads data directly from the course dataset URL)

## Pipeline
1. Explore the data and handle missing values (drop columns with excessive missingness, median imputation, IQR outlier check, standard scaling).
2. **PCA** to find the structure of the data: PC1 explains 57.6% of variance (health, survival, fertility, literacy) and PC2 11.2% (female economic activity).
3. **K-Means** for k=2 to 8 with elbow and silhouette analysis, on the first 5 principal components.
4. Compare k=2 and k=4 and map clusters back to countries.

## Result
- k=2 has the best silhouette (0.44) but hides the middle of the world.
- k=4 gives a clearer structure and reproduces four income levels: extreme poverty, emerging, transition, high income.
- Conclusion: the data supports *Factfulness*; development is a continuum.

## Run it
```bash
pip install -r ../requirements.txt
jupyter notebook un_country_clustering.ipynb
```

**Data:** `UN.csv` from the PSDMA course repository (`manoelgadi/PSDMA`).
