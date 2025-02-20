#include <stdio.h>
#include <string.h>

char *slice(char *str, int start, int end)
{
  if (!str || start < 0 || start > strlen(str) || end < start)
    return NULL;
  else if (end > strlen(str))
    end = strlen(str);

  char copyStr[strlen(str) + 1];
  strcpy(copyStr, str);

  char *ptr = copyStr;
  char *sliced = &ptr[start];
  ptr[end] = '\0';
  ptr = sliced;
  return ptr;
}

int main(void)
{
  char x[] = "JoshMarverks";
  char *res = slice(x, 2, 9);
  printf("%s\n", res);
  printf("%s\n", x);
  return 0;
}

/*
PROBLEMS:
It returns a pointer into a local array (copyStr). Once the function returns, that array goes out of scope, leaving you with a dangling pointer.
*/