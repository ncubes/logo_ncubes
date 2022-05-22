stl_file = open ('model.stl','r')
out_file = open ('modelgood.stl','w')
Lines = stl_file.readlines()
count = 0
for x in Lines:
    line_str = ''
    y = x.split(" ")
    for p in y:
        if p != '':
            try:
                z = float(p)
                line_str += ("{:e}".format(z))
                count += 1
                if count == 3:
                    count = 0
                    line_str += '\n'
                else:
                    line_str += " "
            except ValueError:
                line_str += p
                if (p == 'facet') or (p=='outer') or (p=='solid') or (p=='endsolid'):
                    line_str += ' '
        else:
             line_str += ' '
    out_file.write(line_str)
out_file.close()
stl_file.close()
