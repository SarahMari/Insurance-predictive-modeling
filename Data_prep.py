"Program to replace categorical features with binary operator dummy variables in a new CSV file"

"This code specifically transforms the 'gender', 'smoker', and 'region' features in the original data set into new features: "
  "'is_female', 'is_male', 'is_smoker', 'is_northeast', 'is_northwest', 'is_southeast', and 'is_southwest' where 0=no, 1=yes "
  "This code writes a new CSV file where the old features are replaced with these and the features that were already quantitative are unchanged. "
  "The first line of the resulting file contains new labels, but the code is otherwise ready to work with, having no missing data points or features described by strings. "


insurance = open('insurance.csv', 'r')
exp_ins = open('insurance_clean.csv','w')

def expand(insurance, exp_ins):
    exp_ins.writelines(["age,","is_female,","is_male,","bmi,","number_children,","is_smoker,","is_northeast,","is_southeast,","is_southwest,","is_northwest,","charges\n"])
    insurance.readline()
    for line in insurance.readlines():
        new_values = []
        values = line.split(",")
        new_values.append(str(values[0])+",")
        if values[1] == 'male':
            new_values.append("0,")
            new_values.append("1,")
        elif values[1] == 'female':
            new_values.append("1,")
            new_values.append("0,")
        new_values.append(str(values[2])+",")
        new_values.append(str(values[3])+",")
        if values[4] == 'no':
            new_values.append("0,")
        elif values[4] == 'yes':
            new_values.append("1,")
        if values[5] == 'northeast':
            new_values.append("1,")
            new_values.append("0,")
            new_values.append("0,")
            new_values.append("0,")
        elif values[5] == 'southeast':
            new_values.append("0,")
            new_values.append("1,")
            new_values.append("0,")
            new_values.append("0,")
        elif values[5] == 'southwest':
            new_values.append("0,")
            new_values.append("0,")
            new_values.append("1,")
            new_values.append("0,")
        elif values[5] == 'northwest':
            new_values.append("0,")
            new_values.append("0,")
            new_values.append("0,")
            new_values.append("1,")
        new_values.append(str(values[6]))
        exp_ins.writelines(new_values)


expand(insurance, exp_ins)

insurance.close()
exp_ins.close()

