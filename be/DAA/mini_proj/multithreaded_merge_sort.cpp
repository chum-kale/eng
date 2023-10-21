#include <algorithm>
#include <thread>
#include <iostream>

using namespace std;

struct MergeSortArgs {
  int *arr;
  int left;
  int right;
};

void merge(int *arr, int left, int mid, int right) {
  int n1 = mid - left + 1;
  int n2 = right - mid;

  int *L = new int[n1];
  int *R = new int[n2];

  for (int i = 0; i < n1; i++) {
    L[i] = arr[left + i];
  }

  for (int j = 0; j < n2; j++) {
    R[j] = arr[mid + 1 + j];
  }

  int i = 0;
  int j = 0;
  int k = left;

  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }

  delete[] L;
  delete[] R;
}

void mergeSortThreaded(MergeSortArgs *args) {
  int *arr = args->arr;
  int left = args->left;
  int right = args->right;

  if (left < right) {
    int mid = (left + right) / 2;

    MergeSortArgs args1;
    args1.arr = arr;
    args1.left = left;
    args1.right = mid;

    MergeSortArgs args2;
    args2.arr = arr;
    args2.left = mid + 1;
    args2.right = right;

    thread thread1(mergeSortThreaded, &args1);
    thread thread2(mergeSortThreaded, &args2);

    thread1.join();
    thread2.join();

    merge(arr, left, mid, right);
  }
}

void multithreadedMergeSort(int *arr, int size) {
  MergeSortArgs args;
  args.arr = arr;
  args.left = 0;
  args.right = size - 1;

  mergeSortThreaded(&args);
}

int main() {
  int size;
  cout << "Enter the size of the array: ";
  cin >> size;

  int *arr = new int[size];

  cout << "Enter the elements of the array: ";
  for (int i = 0; i < size; i++) {
    cin >> arr[i];
  }

  multithreadedMergeSort(arr, size);

  cout << "The sorted array is: ";
  for (int i = 0; i < size; i++) {
    cout << arr[i] << " ";
  }

  cout << endl;

  delete[] arr;

  return 0;
}

