from covid import Covid
import matplotlib.pyplot as plt

covid = Covid()
name = input("Enter The Country Name")

virusdata = covid.get_status_by_country_name(name)
print(virusdata)

id=list(virusdata.keys())
value= [str(i) for i in virusdata.values()]

plt.pie(value, labels = id , colors=['r','y','g','b'] ,autopct= '%1.1f%%')
plt.show()