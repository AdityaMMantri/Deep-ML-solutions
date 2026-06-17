def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_features=len(vectors)
    num_obs=len(vectors[0])

    mean=[]
    for feature in vectors:
        total=0.0
        for val in feature:
            total+=val
        mean.append(total / num_obs)

    cov_matrix = []

    for i in range(num_features):
        row=[]
        for j in range(num_features):
            cov_sum=0.0
            for k in range(num_obs):
                cov_sum+=(vectors[i][k]-mean[i]) * (vectors[j][k]-mean[j])
            row.append(cov_sum /(num_obs - 1))
        cov_matrix.append(row)

    return cov_matrix
