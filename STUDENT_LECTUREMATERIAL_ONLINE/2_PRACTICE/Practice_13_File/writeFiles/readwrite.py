
def sum_number_pairs(input_file, output_filename):
    output_file = open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\\Practice_13_File\\writeFiles\\readwrite.py')
    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair,total)
        output_file.write(new_line)
    output_file.close()

sum_number_pairs(open('STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\Practice_13_File\\writeFiles\\number.pairs.txt','r'),
                 'STUDENT_LECTUREMATERIAL_ONLINE\\2_PRACTICE\Practice_13_File\\writeFiles\\out.txt')