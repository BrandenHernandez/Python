# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal. 
# Example The query_name is 'beta'. beta's average score is (30 + 50 + 70)/3 = 50.00. 
# Input Format The first line contains the integer , the number of students' records. 
# The next lines contain the names and marks obtained by a student, each value separated by a space. 
# The final line contains query_name, the name of a student to query. 
# Constraints 2 <= n <= 10 0 <= marks[i] <= 100 length of marks array = 3 
# Output Format Print one line: The average of the marks obtained by the particular student correct to 2 decimal places. 
# Sample Input 0

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    count = 0
    total = 0.0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for each in (student_marks[query_name]):
        total += student_marks[query_name][count]
        count = count + 1
    format_total = "{:.2f}".format(total/count)
    print(format_total)
# ThanksForLooking 
