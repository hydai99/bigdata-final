# bigdata-final

> Project for Vanderbilt University, Big Data Scaling
## Problem

The problem we are trying to solve is to cluster a dataset using cluster algorithms and identify patterns and similarities within the dataset.

## Data

The dataset appears to represent a genomic sequence. It’s first column 'contigname' is likely the name of the sequence or contig, and the subsequent columns (feat_0 to feat_31) are various features associated with that sequence. 

- Data.csv: 1512372 rows × 33 columns

- Label.csv: 1074858 rows × 2 columns

## Method

To accomplish that, we will use KMeans and BFR algorithms to cluster the data points, evaluate the results using the Adjusted Rand Score metric, which could identify which algorithm consumes less memory, and compare two cluster solutions based on peak memory.

### Kmeans

1. Use Left join to merge the Data.csv and Label.csv on key contigname
2. Separate the ground truth label Y come from label.csv and the features X using numpy arrays.
3. Applied Kmeans with 745 clusters, which means we want to form 745 clusters, and random_state=2023 to ensure the reproducibility of the results.
4. We fit the KMeans model to the feature matrix X using the fit method.
obtain the predicted cluster assignments for each data point.
5. Finally, we compute the ARI score using the ground truth labels and the predicted cluster excluding the items that are not in Y. The ARI is 0.26.

### BFR

1. Reads in a distributed data file using Spark.
2. Processes the data by splitting it into smaller partitions for clustering.
3. Uses the KMeans algorithm to cluster data points into two sets: Dense Set (DS) and Remaining Set (RS).
4. In subsequent rounds, checks if data points belong to DS or RS and updates cluster statistics accordingly.
5. Compressed Set (CS) merges small or close clusters and is repeated until no more merges are possible.
6. Merges final CS and DS and any clusters that are close enough.
7. Finally, the resulting clustering assignments for each data point are outputted.


## Result


|        | ARI  | Peak Memory |
|--------|------|-------------|
| Kmeans | 0.26 | 10517988K   |
| BFR    | 0.04 | 9808216K    |


## Repo Directory Structure

Details:

- README.md: overall introduction and information of the project
- milestone1.py: Code for milestone1, using Kmeans algorithm to cluster data
- milestone2.py: Code for milestone2, using BFR algorithm to cluster data
- cal_ari.py: Code to calculate ari score for milestone2
- slide.pdf: Slides for final presentation

## Contact Info

- Hongyu Dai hongyu.dai@vanderbilt.edu

- Zihan Fang zihan.fang@vanderbilt.edu

- Jingyuan Wu jingyuan.wu@vanderbilt.edu