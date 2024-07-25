import pint

ureg = pint.UnitRegistry()
my_size = 1.74 * ureg.meter
print(my_size)  # 1.74 meter
print(my_size.to(ureg.inch))