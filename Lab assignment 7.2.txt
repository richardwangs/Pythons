def student_scores():
    score = (1,2,3,4,5)
    maxscore = max(score)
    minscore = min(score)
    print("The lowest possible score is %s, and the highest possible score is %s" %(minscore,maxscore) )
    for i in score:
        print ("a student can get %i points"% i)
student_scores()
