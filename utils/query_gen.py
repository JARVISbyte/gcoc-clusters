#!/usr/bin/env python3

from sys import exit, stderr

base_query_gl = """SELECT ra, dec, parallax, phot_g_mean_mag as g_mag, bp_rp FROM gaiadr3.gaia_source
WHERE DISTANCE(POINT(COORD1(IVO_SIMBADPOINT('m6')), COORD2(IVO_SIMBADPOINT('m6'))), POINT(ra, dec)) < obj_angrad/60.0
    AND phot_g_mean_mag IS NOT NULL
    AND bp_rp IS NOT NULL
ORDER BY parallax ASC"""


base_query_op = """SELECT ra, dec, parallax, phot_g_mean_mag as g_mag, bp_rp FROM gaiadr3.gaia_source
WHERE DISTANCE(POINT(COORD1(IVO_SIMBADPOINT('m6')), COORD2(IVO_SIMBADPOINT('m6'))), POINT(ra, dec)) < obj_angrad/60.0
	AND parallax > 0.9*obj_par
	AND parallax < 1.1*obj_par
    AND phot_g_mean_mag IS NOT NULL
    AND bp_rp IS NOT NULL
ORDER BY parallax ASC"""

# print(base_query)

print("This is ADQL generator of queries for specific hackaton purposes")
print("----------------------------------------------------------------")

obj_type = input(f"{'Query type (OC/GC): ':>23}")

if obj_type.upper() == 'OC':
    base_query = base_query_op
elif obj_type.upper() == 'GC':
    base_query = base_query_gl
else:
    print(f"Unknown object type [{obj_type}]. Exiting", file=stderr)
    exit(1)

obj_id = input(f"{'Choose object id: ':>23}")
base_query = base_query.replace("m6", obj_id)
obj_par = input(f"{'parallax [mas]: ':>23}")
base_query = base_query.replace("obj_par", obj_par)
obj_angsize = input(f"{'angular size [arcmin]: ':>23}")
base_query = base_query.replace("obj_angrad", str(round(float(obj_angsize)/2, 3)))

print("\n----------------------------------------------------------------")
print("New query generated\n")
print(base_query)

filename = 'adqlq.txt'
with open(filename, 'w', encoding='utf-8') as file:
    file.write(base_query)

print("\nQuery exported to > " + filename)
