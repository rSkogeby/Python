#!/usr/bin/env python
n = 9
m = 27
#pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOMEi'.center(m, '-')] + pattern[::-1]))
