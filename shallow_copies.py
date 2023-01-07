stats = [{"name":'ABC',"age":30}]
copied_stats= stats[:]
copied_stats[0]['name']= 'XYZ'
print(stats)