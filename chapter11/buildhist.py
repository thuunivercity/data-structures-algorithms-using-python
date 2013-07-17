# Prints a histogram for a distribution of letter grades computed from
# a collection of numeric grades extracted from a text file.

from maphist import Higtogram

def main():
    # Create a Higtogram instance for cumputing the frequencies
    gradeHist = Histogram("ABCDF")
    
    # Open the text file containing the grades.
    gradeFile = open('cs101grades.txt', "r")
    
    # Extract the grades and increment the appropriate counter.
    for line in gradeFile:
        grade = int(line)
        gradeHist.intCount(letterGrade(grade))
        
        # Print the histogram chart
        printChart(gradeHist)

# Determines the letter grade for the given numeric value.
def letterGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60
        return 'D'
    else: 
        return 'F'

# Prints the histogram as a hoticontal bar chart
def printChart(gradeHist):
    print("           Grade Distibution")
    # Print th body of the chart
    letterGrades = ('A', 'B', 'C', 'D', 'F')
    for letter in letterGrades:
    print("  |")
    print(letter + " +", end = "")
    freq = gradeHist.getCount(letter)
    print('*' * freq)

    # Print the x-axis
    print("  |")
    print("  +----+----+----+----+----+----+----+----")
    print("  0    5    10   15   20   25   30   35")

# Calls the main routine.
main()
