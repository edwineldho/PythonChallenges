#Task1 Create a float variable for Ringgit and print it as "RM129
amount = 129.0
print(f"RM {amount}")

headcol1 = ["aefquwiefjopeirfjweoprfijwerpofjwerfopij", "bqoeijfqwepofjqwepodiqjwepoi", "cpefojewrfopjwefpowejf"]
numcol1 = [1,1003442,5.32222342]
numcol2 = [5.62233,7.364363,9.32747474342]
numcol3 = [19.26345265,7.866832817,10.781237892798]

print(f"{headcol1[0]:<15} {headcol1[1]:<15} {headcol1[2]:<15}")
for i in range(3):
    print(f"{numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")

