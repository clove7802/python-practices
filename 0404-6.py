string_a = "{}".format(10)

print(string_a)
print(type(string_a))

#94P
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

#96P
output_a = "{:d}".format(52)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

#조햡하기 97P
output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print("#조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)