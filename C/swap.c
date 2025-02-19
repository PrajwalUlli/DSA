#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
  int x = 5;
  int y = 7;
  swap(&x, &y);
  printf("x: %d, y: %d\n", x, y);
  return 0;
}

void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}