from src.converter import *

assert meter_ke_cm(1) == 100
assert cm_ke_meter(100) == 1
assert km_ke_meter(1) == 1000
assert meter_ke_km(1000) == 1

print("Semua test PASS")