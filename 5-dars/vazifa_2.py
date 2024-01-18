def string_farqi(str1, str2):
   farq=set(str1)-set(str2)
   farq2=set(str2)-set(str1)
   umumiy_farq=farq.union(farq2)
   diference_string="".join(umumiy_farq)

   return diference_string
a="salom "
b="salyut"
c=string_farqi(a, b)
print(c)