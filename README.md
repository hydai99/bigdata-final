# bigdata-final

> Project for Vanderbilt University, Big Data Scaling
## Problem

Employ two clustering algorithms to analyze a sizable dataset for detecting patterns and similarities, and contrast the dissimilarity in peak memory usage and accuracy using the ARI metric.

## Data

It seems that the dataset pertains to a genomic sequence, where the initial column labeled as 'contigname' denotes the name of the contig, while the following columns, labeled as feat_0 to feat_31, encompass distinct characteristics linked with the said sequence.

The training dataset, named `Data.csv`, consists of 1512372 rows and 33 columns, while the ground truth label Y is provided in the `Label.csv` file, which contains 1074858 rows and 2 columns. This ground truth label Y is used to calculate the ARI.

## Method

To accomplish that, we will use KMeans and BFR algorithms to cluster the data points, evaluate the results using the Adjusted Rand Score metric, which could identify which algorithm consumes less memory, and compare two cluster solutions based on peak memory.

### Kmeans

1. To merge `Data.csv` and `Label.csv` on key contigname, use a Left join.
2. Use numpy arrays to separate the features X and ground truth label Y from Label.csv.
3. Apply Kmeans with 745 clusters to form clusters, and set random_state=2023 for reproducibility.
4. Fit the KMeans model to feature matrix X using the fit method to obtain predicted cluster assignments for each data point.
5. Compute the ARI score using ground truth labels and predicted clusters, excluding items not in Y. The resulting ARI score is 0.26.

### BFR

1. Utilizing Spark, retrieve the data points from `Data.csv`.
2. Initialize K centroids for K-Means using a small random sample of the data points and Euclidean distance as the similarity measurement.
3. Generate DS clusters by applying K-Means to the data points obtained in step 2, and discard the points, keeping only statistics.
4. K centroids have been initialized in DS, resulting in K clusters.
5. Run K-Means on the remaining data points, using a large number of clusters (e.g., 5 times K) to produce CS clusters (with more than one point) and RS clusters (with only one point).
6. Retrieve the next set of data points from `Data.csv`.
7. Calculate the Mahalanobis Distance between new points and the clusters in DS, and assign them to the nearest DS cluster if the distance is less than $\alpha\sqrt{d}$.
8. If new points are not assigned to any DS clusters, calculate their Mahalanobis Distance and assign them to the nearest CS cluster if the distance is less than $\alpha\sqrt{d}$.
9. If new points are not assigned to any clusters in DS or CS, assign them to RS clusters.
10. Combine the points in RS clusters by applying K-Means with a large number of clusters (e.g., 5 times K) to generate CS clusters (with more than one point) and RS clusters (with only one point).
11. Merge CS clusters that have a Mahalanobis Distance less than $\alpha\sqrt{d}$.
12. Repeat above steps for all `Data.csv`.
13. If this is the final iteration (after processing the last chunk of data points), merge CS clusters with DS clusters that have a Mahalanobis Distance less than $\alpha\sqrt{d}$. ($\alpha$ is a hyper-parameter.)

## Result


|        | ARI  | Peak Memory |
|--------|------|-------------|
| Kmeans | 0.26 | 10517988K   |
| BFR    | 0.04 | 9808216K    |


## Repo Directory Structure

Details:

- README.md: overall introduction and information of the project
- milestone1.py: Code for milestone1, using Kmeans algorithm to cluster data (usage: `python milestone1.py`)
- milestone2.py: Code for milestone2, using BFR algorithm to cluster data (usage: `python milestone2.py  inputfile  #_of_cluster   outputfile`)
- cal_ari.py: Code to calculate ari score for milestone2 (usage: `python cal_ari.py`)
- slide.pdf: Slides for final presentation

## Contact Info

- Hongyu Dai hongyu.dai@vanderbilt.edu

- Zihan Fang zihan.fang@vanderbilt.edu

- Jingyuan Wu jingyuan.wu@vanderbilt.edu
