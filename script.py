@Made by Sposato Matteo
import csv
with open("insurance.csv") as insurance_file:
  dict_reader = csv.DictReader(insurance_file)
  length_insurance_list = 0
  dict_insurance = {}
  southwest_insurance = []
  northwest_insurance = []
  southeast_insurance = []
  northeast_insurance = []
  for row in dict_reader:
    dict_insurance["Age"] = row["age"]    
    dict_insurance["Sex"] = row["sex"]    
    dict_insurance["BMI"] = row["bmi"]    
    dict_insurance["Number of Children"] = row["children"]    
    dict_insurance["Smoker"] = row["smoker"]    
    dict_insurance["Region"] = row["region"]    
    dict_insurance["Charges"] = row["charges"]
    length_insurance_list += 1
    print(dict_insurance)
    
  #This block of code record categorize insurances by region (using one list for each region)
    
    if dict_insurance["Region"] == "southwest":
      southwest_insurance.append(row)
    elif dict_insurance["Region"] == "northwest":
      northwest_insurance.append(row)
    elif dict_insurance["Region"] == "southeast":
      southeast_insurance.append(row)
    elif dict_insurance["Region"] == "northeast":
      northeast_insurance.append(row)
      
#This block of code categorize region's insurance lists in a dictionary, called "insurances_by_region", 
#with a key for the name of region and a value for list of insurance

#Just below there is a print statement that output the number of records
  
  print(f"\nThe number of recorded insurances is {length_insurance_list}\n")
  insurances_by_region = {}
  insurances_by_region["South-West"] = southwest_insurance
  insurances_by_region["North-West"] = northwest_insurance
  insurances_by_region["South-East"] = southeast_insurance
  insurances_by_region["North-East"] = northeast_insurance
  
  #This block of code print-out first 15 insurances located in South-East 
  #(you can print-out more insurances by changing the max value of count in the while loop, 
  #and you can change region of interest by changing value of the value called in the for loop, 
  #and print statement in while loop; 
  #and then also change number and name of the region in the print statement just below: it will look nicer)
  
  print("First 15 recorded insurances located in South-East are:\n")
  count = 0
  for insurance in insurances_by_region["South-East"]:
    while count <= 14:
      print(str(count) + ") " + str(insurances_by_region["South-East"][count]) + "\n")
      count += 1

  #This block of code find the average age of insurances located in South-East
  
  total_ages = 0
  for insurance in insurances_by_region["South-East"]:
      total_ages += int(insurance["age"])
  print(f"The sum of ages of insurances located in South-East is {total_ages}") 
  avg_age_insur_southeast = int(total_ages / length_insurance_list)
  print(f"The average age of insurances located in South-East is {avg_age_insur_southeast}")
  

