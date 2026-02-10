#include <stdio.h>
#include <math.h>

// Function to calculate mean
double mean(double x[], int n) {
    double sum = 0;
    for(int i = 0; i < n; i++)
        sum += x[i];
    return sum / n;
}

// Function to calculate variance
double variance(double x[], int n) {
    double m = mean(x, n);  // call mean()
    double var = 0;
    for(int i = 0; i < n; i++)
        var += (x[i] - m) * (x[i] - m);
    return var / n;   // use n-1 if sample variance
}

// Function to calculate correlation
double correlation(double x[], double y[], int n) {
    double mean_x = mean(x, n);
    double mean_y = mean(y, n);

    double numerator = 0, denom_x = 0, denom_y = 0;
    for(int i = 0; i < n; i++) {
        numerator += (x[i] - mean_x) * (y[i] - mean_y);
        denom_x += (x[i] - mean_x) * (x[i] - mean_x);
        denom_y += (y[i] - mean_y) * (y[i] - mean_y);
    }

    return numerator / sqrt(denom_x * denom_y);
}

int main() {
    int n;

    printf("Enter number of values for X and Y: ");
    scanf("%d", &n);

    double x[n], y[n];

    for(int i = 0; i < n; i++) {
        printf("Enter X[%d]: ", i);
        scanf("%lf", &x[i]);
    }

    for(int i = 0; i < n; i++) {
        printf("Enter Y[%d]: ", i);
        scanf("%lf", &y[i]);
    }

    // Call the functions
    double mean_x = mean(x, n);
    double mean_y = mean(y, n);
    double var_x = variance(x, n);
    double var_y = variance(y, n);
    double corr = correlation(x, y, n);

    printf("\nMean of X = %.2f\n", mean_x);
    printf("Mean of Y = %.2f\n", mean_y);
    printf("Variance of X = %.2f\n", var_x);
    printf("Variance of Y = %.2f\n", var_y);
    printf("Correlation between X and Y = %.2f\n", corr);

    return 0;
}
