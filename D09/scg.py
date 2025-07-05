stude_scores={
    "alamir":81,
    "fqadie":91,
    "temesgen":78,
    "bimrew":71,
    "GHN":56
}
stident_grade={}
for key in stude_scores:
    if stude_scores[key]>=91:
        stident_grade[key]="outstanding!"
    elif stude_scores[key]>=81:
        stident_grade[key]="expectation!"
    elif stude_scores[key]>=71:
       stident_grade[key]="accepted!"
    else:
      stident_grade[key]="Fail!"
print(stident_grade)
