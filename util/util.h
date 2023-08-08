// Utility functions, macros, and stuff for C.
// https://github.com/ramdeoshubham/macros/blob/master/macros.h
#define SWAP(x, y) do { int temp = x; x = y; y = temp; } while (0)
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define MAX(x, y) ((x) > (y) ? (x) : (y))
