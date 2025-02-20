#include <stdio.h>

int len(char *str)
{
  int counter = 0;

  while (str[counter] != '\0')
  {
    counter++;
  }

  return counter;
}

int main(void)
{
  char x[] = "Hello";

  printf("%d\n", len(x));

  return 0;
}
