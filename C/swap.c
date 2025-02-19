#include <stdio.h>

void swap(int *, int *);

void main()
{
  int x = 5;
  int y = 7;
  swap(&x, &y);
  printf("x: %d, y: %d", x, y);
}

void swap(int *x, int *y)
{
  int tmp = *x;
  *x = *y;
  *y = tmp;
}